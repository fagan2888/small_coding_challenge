file_name = 'soccer.dat'

with open(file_name, 'r') as file:
    for _ in range(3):
        next(file)
    min_difference = 1000000
    for line in file:
        line = line.split()
        if len(line) > 5:
            team_name, for_score, against_score = line[1], line[6], line[8]
            score_difference = abs(int(for_score) - int(against_score))
            if score_difference < min_difference:
                min_difference = score_difference
                min_team = team_name

print("The team with the smallest difference in ‘for’ and ‘against’ goals is:", min_team, ", with score difference of", min_difference)
