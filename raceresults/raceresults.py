import pandas as pd
import numpy as np
import os

data_dir = os.getcwd()
results_file = data_dir+'\\racessummary20190410.xlsx'


def pace(time):
    return pd.to_timedelta(time) / 2


def get_race_results():
    dfraceresults = pd.read_excel(results_file, encoding='ISO-8859-1')
    dfraceresults['Effort'] = dfraceresults['Effort'].fillna(-1)
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].fillna(-1)
    dfraceresults['Date'] = pd.to_datetime(dfraceresults['Date']).dt.strftime("%d %b %y")
    dfraceresults['Climb FT'] = dfraceresults['Climb FT'].round(0).astype(int)
    dfraceresults['Effort'] = dfraceresults['Effort'].round(0).astype(int)
    print(dfraceresults.dtypes)
    print(dfraceresults.head())
    print("results file:", results_file)
    response = input("Calculate pace? Y/y \n")
    if response.lower() == 'y':
        dfraceresults['Pace'] = (pd.to_timedelta(dfraceresults.Time) / dfraceresults.Miles)
        dfraceresults['Pace'] = pd.to_datetime(dfraceresults['Pace']).dt.strftime("%M:%S")
    dfraceresults_html = dfraceresults.round({"Climb FT": 0, "Miles": 2})
    dfraceresults_html.to_html("raceresults.html")


if __name__ == "__main__":
    get_race_results()
