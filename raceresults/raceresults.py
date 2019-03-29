import pandas as pd
import os

data_dir = os.getcwd()
results_file = data_dir+'\\racessummary20190329.xlsx'


def main():
    dfraceresults = pd.read_excel(results_file, encoding='ISO-8859-1')
    print(dfraceresults.head())
    print("results file:", results_file)


if __name__ == "__main__":
    main()