import argparse
import sys

"""
Build a Data Process class, contains a global minimum -- initiate to be a very big number -- keeping track of the minimum that has been seen
function  caculate_min_spread processes the dat file line by line to calucate the temperature spread for each month, compare it with the global minimum and make modification accordingly
function return the global minimum
"""

class DataProcess:
    min_spread = sys.maxsize

    def caculate_min_spread(self, file_path):
        with open(file_path, 'r') as file:
            # skipping the first few lines that are headers, line changes
            for _ in range(6):
                next(file)

            for line in file:
                line = line.split()
                # filter the lines that do not contain the correct format of data
                if len(line) > 3 and line[0] != 'mo':
                    day_number, max_temp, min_temp = line[0], line[1].strip("*"), line[2].strip("*")
                    spread = int(max_temp) - int(min_temp)
                    if spread < self.min_spread:
                        self.min_spread = spread
                        min_spread_day = day_number

        print("The smallest temperature spread in this month's date on day:", min_spread_day, "which is:", self.min_spread)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='a small program to process the wheather data')
        parser.add_argument('-i', '--infile', help='the file name to be processed')
        args = parser.parse_args()

        ans = DataProcess()
        if args.infile:
            file_path = args.infile
            ans.caculate_min_spread(file_path)
        else:
            file_path = 'w_data (5).dat'
        ans.caculate_min_spread(file_path)
