import os
from process_results import get_race_results

dir = os.getcwd()
data_dir = dir+'\\raceresults\\'
os.chdir(data_dir)
print('Data dir is: ', data_dir)
results_file = data_dir+'MyRaces.csv'
results_page = 'my_race_results.html'
others_results_file = data_dir+'OtherRaces.csv'
others_results_page = 'others_race_results.html'

if __name__ == "__main__":
    get_race_results(results_file, results_page, 'mine')
    get_race_results(others_results_file, others_results_page, 'others')
