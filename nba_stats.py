# CS 327E Spring 2016
# Professor Cohen
# King Troup - Navin Udiaver, Sheryar Ali, Steven Coleman

import pymysql
import csv
stats = []
f = open('stat_totals.csv', 'r')
csv_f = csv.reader(f)
for row in csv_f:
  stats.append(row)
for i in range(len(stats)):
    for j in range(len(stats[i])):
        if stats[i][j].isdigit():
            stats[i][j] = int(stats[i][j])
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='2121',
                             db='nba',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        for i in range(len(stats)):
            future = 'INSERT INTO stats (player_name, field_goal_made, field_goal_attempt, three_point_made, three_point_attempt, free_made, free_throw_attempt, rebounds, assists, steals, blocks, turnovers, \
            points, year, win_share, player_efficiency, personal_fouls) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(future, ((stats[i][0]), int(stats[i][1]), int(stats[i][2]), int(stats[i][3]), int(stats[i][4]), int(stats[i][5]), int(stats[i][6]), int(stats[i][7]), int(stats[i][8]), int(stats[i][9]), int(stats[i][10]), int(stats[i][11]), int(stats[i][12]), (stats[i][13]), float(stats[i][14]), float(stats[i][15]), int(stats[i][16])))



    connection.commit()

finally:
    connection.close()

f.close()