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
    my_race_results = get_race_results(results_file, results_page, 'mine')
    other_race_results = get_race_results(others_results_file, others_results_page, 'others')
    my_best_results = my_race_results.groupby(["Course"]).apply(lambda x: x.sort_values(["Pace"], ascending = True)).reset_index(drop=True)
    # print(my_best_results.groupby(['Course']).head(1))
    other_best_results = other_race_results.groupby(["Name"]).apply(lambda x: x.sort_values(["Pace"], ascending = True)).reset_index(drop=True)
    print(other_best_results.groupby(['Name']).head(1))
    