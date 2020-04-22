import argparse
import sys

"""
Build a Data Process class, contains a global minimum -- initiate to be a very big number -- keeping track of the minimum that has been seen
function  caculate_min_score_difference processes the dat file line by line to calucate the absolution difference between A and F for each team, compare it with the global minimum and make modification accordingly
function return the global minimum
"""

class DataProcess:
    min_difference = sys.maxsize

    def caculate_min_score_difference(self, file_path):
        with open(file_path, 'r') as file:
            #skip the first few lines which are headers and line changes
            for _ in range(3):
                next(file)

            for line in file:
                line = line.split()
                # filter the lines that do not contain the correct data format
                if len(line) > 5:
                    team_name, for_score, against_score = line[1], line[6], line[8]
                    score_difference = abs(int(for_score) - int(against_score))
                    if score_difference < self.min_difference:
                        self.min_difference = score_difference
                        min_team = team_name

        print("The team with the smallest difference in ‘for’ and ‘against’ goals is:", min_team, ", with score difference of", self.min_difference)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='a small program to process the wheather data')
        parser.add_argument('-i', '--infile', help='the file name to be processed')
        args = parser.parse_args()

        ans = DataProcess()
        if args.infile:
            file_path = args.infile
            ans.caculate_min_spread(file_path)
        else:
            file_path = 'soccer.dat'
        ans.caculate_min_score_difference(file_path)
