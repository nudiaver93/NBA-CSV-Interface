# CS 327E Spring 2016
# Professor Cohen
# King Troup - Navin Udiaver, Sheryar Ali, Steven Coleman

import pymysql
import csv
stats = []
f = open('players.csv', 'r')
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
            future = 'INSERT INTO player (player_name, position, age, team_name, num_of_games) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(future, (stats[i][0], stats[i][1], int(stats[i][2]), stats[i][3], int(stats[i][4])))

    connection.commit()

finally:
    connection.close()

f.close()