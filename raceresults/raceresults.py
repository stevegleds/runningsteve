import pandas as pd
import numpy as np
import os

data_dir = os.getcwd()
results_file = data_dir+'\\MyRaces.csv'
results_page = 'my_race_results.html'
others_results_file = data_dir+'\\OtherRaces.csv'
others_results_page = 'others_race_results.html'

pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head><title>Race Results</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Results</th>
      <th>Sort By Pace</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="my_race_results.html">My Race Results</a></td>
      <td><a href="pace_my_race_results.html">Sorted by Pace</a></td>
    </tr>
        <tr>
      <td><a href="others_race_results.html">Other Race Results</a></td>
      <td><a href="pace_others_race_results.html">Sorted by Pace</a></td>
    </tr>
  </tbody>
</table>
  <body>
    {table}
  </body>
</html>.
'''


def pace(time):
    return pd.to_timedelta(time) / 2


def get_race_results(results, webpage, runners):
    dfraceresults = pd.read_csv(results, encoding='ISO-8859-1')
    dfraceresults['Effort'] = dfraceresults['Effort'].fillna(-1)
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].fillna(-1)
    # Create a Datetime field from the date in the csv to use in sorting / delta etc
    # Then use the new Datetime field to replace 'Date' with required format for displaying
    dfraceresults['Datetime'] = pd.to_datetime(dfraceresults['Date'])
    dfraceresults['Date'] = dfraceresults['Datetime'].dt.strftime("%d %b %y")
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].round(0).astype(int)
    dfraceresults['Effort'] = dfraceresults['Effort'].round(0).astype(int)
    # print(dfraceresults.dtypes)
    # print(dfraceresults.head())
    print("results file:", results_file)
    dfraceresults['Pace'] = (pd.to_timedelta(dfraceresults.Time) / dfraceresults.Miles)
    dfraceresults['Pace'] = pd.to_datetime(dfraceresults['Pace']).dt.strftime("%M:%S")
    dfraceresults['Notes'] = dfraceresults['Notes'].fillna(value='')
    if runners == 'mine':
        cols = ['Date', 'Course', 'Miles', 'Pace', 'Time', 'Climb FT', 'Effort', 'Notes', 'Datetime']
    else:
        cols = ['Name', 'Date', 'Course', 'Miles', 'Pace', 'Time', 'Climb FT', 'Age Grade', 'Notes',
                'Category', 'Overall #', 'Runners', 'Datetime']
    print(cols)
    # dfraceresults = dfraceresults[cols]
    if runners == 'mine':
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
    else:
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
        dfraceresults = dfraceresults.sort_values(by='Name')
    dfraceresults_html = dfraceresults.round({"Climb FT": 0, "Miles": 2})
    dfraceresults_html = dfraceresults_html[cols[:-1]]
    dfraceresults_html.to_html(webpage)
    with open(webpage, 'w') as f:
        f.write(html_string.format(table=dfraceresults_html.to_html(classes='mystyle')))
    dfraceresults_html = dfraceresults.sort_values(by=['Pace'])
    dfraceresults_html = dfraceresults_html[cols[:-1]]
    webpage = 'pace_'+webpage
    dfraceresults_html.to_html(webpage, classes='mystle')
    with open(webpage, 'w') as f:
        f.write(html_string.format(table=dfraceresults_html.to_html(classes='mystyle')))


if __name__ == "__main__":
    get_race_results(results_file, results_page, 'mine')
    get_race_results(others_results_file, others_results_page, 'others')
