file_name = 'w_data (5).dat'

with open(file_name, 'r') as file:
        for _ in range(6):
            next(file)
        min_spread = 100000000
        for line in file:
            line = line.split()
            if len(line) > 3 and line[0] != 'mo':
                day_number, max_temp, min_temp = line[0], line[1].strip("*"), line[2].strip("*")
                spread = int(max_temp) - int(min_temp)
                if spread < min_spread:
                    min_spread = spread
                    min_spread_day = day_number

print("The smallest temperature spread in this month's date on day:", min_spread_day, "which is:", min_spread)
