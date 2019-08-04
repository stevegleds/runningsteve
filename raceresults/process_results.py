import pandas as pd
import numpy as np
from html_code import html_string


def pace(time):
    return pd.to_timedelta(time) / 2


def get_race_results(results, webpage, runners):
    dfraceresults = pd.read_csv(results, encoding='ISO-8859-1')
    dfraceresults = format_dataframe(dfraceresults)
    if runners == 'mine':
        print('producing my race results columns list')
        cols = ['Date', 'Course', 'Miles', 'Pace', 'Time', 'Gradient %', 'Climb FT', 'Effort', 'Notes', 'Datetime']
    else:
        print('Producing other race results columns list')
        cols = ['Name', 'Date', 'Course', 'Notes', 'Time', 'Pace', 'Age Grade', 'Gradient %', 'Climb FT', 'Miles',    
                'Category', 'Overall #', 'Runners', 'Datetime']
    print(cols)
    # dfraceresults = dfraceresults[cols]
    if runners == 'mine':
        print('Starting results for me')
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
        print('Ending my results')
        # dfraceresults = dfraceresults.groupby(["Course"]).apply(lambda x: x.sort_values(["Pace"], ascending = True)).reset_index(drop=True)
    else:
        print('starting other results')
        dfraceresults = dfraceresults.sort_values(by='Datetime', ascending=False)
        # dfraceresults = dfraceresults.groupby(["Name"]).apply(lambda x: x.sort_values(["Pace"], ascending = True)).reset_index(drop=True)
        print(dfraceresults.head())
        # dfraceresults = dfraceresults.sort_values(by='Name')
    create_html_pages(dfraceresults, runners, cols, webpage)
    return dfraceresults


def format_dataframe(dfraceresults):
    '''
    formats dataframe data
    Replace 'na' with '-1' or '' to prevent type errors
    Create a Datetime field from the date in the csv to use in sorting / delta etc
    Then use the new Datetime field to replace 'Date' with required format for displaying
    Only need Climb Ft and Effort to whole numbers
    Create 'Pace' field from time and miles and format as mm:ss
    Gradient is % of climb over total distance    
    '''
    dfraceresults['Effort'] = dfraceresults['Effort'].fillna(-1)
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].fillna(-1)
    dfraceresults['Datetime'] = pd.to_datetime(dfraceresults['Date'])
    dfraceresults['Date'] = dfraceresults['Datetime'].dt.strftime("%d %b %y")
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].round(0).astype(int)
    dfraceresults['Effort'] = dfraceresults['Effort'].round(0).astype(int)
    dfraceresults['Pace'] = (pd.to_timedelta(dfraceresults.Time) / dfraceresults.Miles)
    dfraceresults['Pace'] = pd.to_datetime(dfraceresults['Pace']).dt.strftime("%M:%S")
    dfraceresults['Gradient %'] = dfraceresults['Climb FT'] / dfraceresults['Miles'] / 5280 * 100
    dfraceresults['Notes'] = dfraceresults['Notes'].fillna(value='')
    return dfraceresults


def create_html_pages(dfraceresults, runners, cols, webpage):
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
        # Summary
        summarywebpage = 'summary_'+webpage
        dfraceresultssummary_html = dfraceresults_html.groupby(['Name']).head(1)
        dfraceresultssummary_html.to_html(summarywebpage, classes='mystyle')
        with open(summarywebpage, 'w') as f:
            f.write(html_string.format(table=dfraceresultssummary_html.to_html(classes='mystyle')))
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
        