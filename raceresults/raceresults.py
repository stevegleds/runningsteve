import pandas as pd
import numpy as np
import os
dir = os.getcwd()
data_dir = dir+'\\raceresults\\'
os.chdir(data_dir)
print('Data dir is: ', data_dir)
results_file = data_dir+'MyRaces.csv'
results_page = 'my_race_results.html'
others_results_file = data_dir+'OtherRaces.csv'
others_results_page = 'others_race_results.html'

pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head>
      <!-- Start Mui boilerplate code - used for mui css -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- load MUI -->
      <link href="//cdn.muicss.com/mui-0.9.39/css/mui.min.css" rel="stylesheet" type="text/css" />
      <script src="//cdn.muicss.com/mui-0.9.39/js/mui.min.js"></script>
      <!-- End mui boilerplate code -->
  <title>Race Results</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  </head>
  <body>
      <div class="mui-panel">Steve
        <button class="mui-btn mui-btn--raised"><a href="my_race_results.html">Sort by Date</a></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="pace_my_race_results.html">Sort by Pace</a> </button>
        
    </div>
    <hr>
          <div class="mui-panel">Others
        <button class="mui-btn mui-btn--raised"><a href="others_race_results.html">Sort by Date</a></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="pace_others_race_results.html">Sort by Pace</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="#"></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="baylee_pace_others_race_results.html">Baylee</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="taylor_pace_others_race_results.html">Taylor</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="aimee_pace_others_race_results.html">Aimee</a> </button>
    </div>
    <hr>
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
    # print("results file:", results_file)
    dfraceresults['Pace'] = (pd.to_timedelta(dfraceresults.Time) / dfraceresults.Miles)
    dfraceresults['Pace'] = pd.to_datetime(dfraceresults['Pace']).dt.strftime("%M:%S")
    dfraceresults['Notes'] = dfraceresults['Notes'].fillna(value='')
    if runners == 'mine':
        print('producing my race results columns list')
        cols = ['Date', 'Course', 'Miles', 'Pace', 'Time', 'Climb FT', 'Effort', 'Notes', 'Datetime']
    else:
        print('Producing other race results columns list')
        cols = ['Name', 'Date', 'Course', 'Notes', 'Time', 'Pace', 'Age Grade', 'Climb FT', 'Miles',    
                'Category', 'Overall #', 'Runners', 'Datetime']
    print(cols)
    # dfraceresults = dfraceresults[cols]
    if runners == 'mine':
        print('Starting results for me')
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
        print('Ending my results')
    else:
        print('starting other results')
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
        print('finished other results')
        # dfraceresults = dfraceresults.sort_values(by='Name')
    dfraceresults_html = dfraceresults.round({"Climb FT": 0, "Miles": 2})
    dfraceresults_html = dfraceresults_html[cols[:-1]]
    dfraceresults_html.to_html(webpage)
    with open(webpage, 'w') as f:
        f.write(html_string.format(table=dfraceresults_html.to_html(classes='mystyle')))
    dfraceresults_html = dfraceresults.sort_values(by=['Pace'])
    dfraceresults_html = dfraceresults_html[cols[:-1]]
    webpage = 'pace_'+webpage
    dfraceresults_html.to_html(webpage, classes='mystyle')
    with open(webpage, 'w') as f:
        f.write(html_string.format(table=dfraceresults_html.to_html(classes='mystyle')))
    #  create filter pages
    if runners != 'mine':
        # Baylee
        personalwebpage = 'baylee_'+webpage
        dfraceresultsbaylee_html = dfraceresults_html[dfraceresults_html['Name'] == 'Baylee'].sort_values(by=['Pace'])
        dfraceresultsbaylee_html.to_html(personalwebpage, classes='mystyle')
        with open(personalwebpage, 'w') as f:
            f.write(html_string.format(table=dfraceresultsbaylee_html.to_html(classes='mystyle')))
        # Taylor
        personalwebpage = 'taylor_'+webpage
        dfraceresultstaylor_html = dfraceresults_html[dfraceresults_html['Name'] == 'Taylor'].sort_values(by=['Pace'])
        dfraceresultstaylor_html.to_html(personalwebpage, classes='mystyle')
        with open(personalwebpage, 'w') as f:
            f.write(html_string.format(table=dfraceresultstaylor_html.to_html(classes='mystyle')))
        # Aimee
        personalwebpage = 'aimee_'+webpage
        dfraceresultsaimee_html = dfraceresults_html[dfraceresults_html['Name'] == 'Aimee'].sort_values(by=['Pace'])
        dfraceresultsaimee_html.to_html(personalwebpage, classes='mystyle')
        with open(personalwebpage, 'w') as f:
            f.write(html_string.format(table=dfraceresultsaimee_html.to_html(classes='mystyle')))


if __name__ == "__main__":
    get_race_results(results_file, results_page, 'mine')
    get_race_results(others_results_file, others_results_page, 'others')
