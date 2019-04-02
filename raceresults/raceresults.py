import pandas as pd
import os

data_dir = os.getcwd()
results_file = data_dir+'\\racessummary20190329.xlsx'


def pace(time):
    return pd.to_timedelta(time) / 2


def main():
    dfraceresults = pd.read_excel(results_file, encoding='ISO-8859-1')
    print(dfraceresults.head())
    print("results file:", results_file)
    dfraceresults.to_html("raceresults.html")
    response = input("Calculate pace? Y/y \n")
    if response.lower() == 'y':
        dfraceresults['Pace'] = pd.to_timedelta(dfraceresults.Time) / dfraceresults.Miles
        dfraceresults.to_html("raceresults.html")


if __name__ == "__main__":
    main()