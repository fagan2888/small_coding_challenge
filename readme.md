This folder contains two py files:
1. the program `min_temp_spread.py` process designated data file (use --infile argument) that contains weather data and print out the day number with the minimal temperture spread of the month's data, and the minimal temperture spread for verification later. Without specification of infile, the program processes with default file name `w_data (5).dat`

Run the program by the following command in your bash shell

```
python3 min_temp_spread.py
```
The program prints out:
"The smallest temperature spread in this month's date on day: 14 which is: 2"

2. the program `min_difference_score.py ` process designated data file (use --infile argument) that contains soccer match performances and print out the team name with the smallest difference between the for score and against score. Without specification of infile, the program processes with default file name `soccer.dat`

Run the program by the following command in your bash shell

```
python3 min_difference_score.py
```
The program prints out:
"The team with the smallest difference in ‘for’ and ‘against’ goals is: Aston_Villa , with score difference of 1"
