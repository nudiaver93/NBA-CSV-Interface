# CS 327E Spring 2016
# Professor Cohen
# King Troup - Navin Udiaver, Sheryar Ali, Steven Coleman

import pymysql
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='2121',
                             db='nba',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# connection is not autocommit by default. So you must commit to save
# your changes.
try:
    print("1996 and 2016 NBA Stats Comparison")
    print()
    choice = 1
    while choice != 5:
        # Prompt the user with the menu and their input
        print("What would you like to know?")
        print("  1. Show points, name, and rebounds and assists for a player")
        print("  2. Highest win-share average by position for both seasons")
        print("  3. Average points by age")
        print("  4. Player efficiency by position")
        print("  5. Quit")
        choice = int(input("Please enter 1, 2, 3, 4, or 5: "))
        print()

        if choice == 1:
            name = (input("Enter in a player name : "))
            with connection.cursor() as cursor:
                # Read a single record

                ps = "SELECT player.player_name, assists, rebounds, points FROM stats INNER JOIN player on stats.player_name = player.player_name WHERE stats.player_name = %s"

                cursor.execute(ps, (name,))
                result = cursor.fetchone()
                for key, value in result.items():
                    print(value)
                print()

        elif choice == 2:
            with connection.cursor() as cursor:
                winshare = "SELECT win_share, year, position FROM stats INNER JOIN player on stats.player_name = player.player_name Group by position order by year;"
                cursor.execute(winshare)
                result = cursor.fetchone()
                for key, value in result.items():
                    print(value)
                print()

            continue

        elif choice == 3:
            option = 1
            while option < 20 or option > 40:
                option = eval(input("Enter in an age: "))
            with connection.cursor() as cursor:
                pa = "Select points, age From Stats INNER JOIN player on stats.player_name=player.player_name WHERE age = %s"
                cursor.execute(pa, (option,))
                result = cursor.fetchone()
                for key, value in result.items():
                    print(value)
                print()

            continue

        elif choice == 4:
            pos = ["C", "PF", "SF", "PG", "SG"]
            postion_input = (input("Enter a position (C, PF, SF, PG, SG): "))
            while postion_input not in pos:
                postion_input = (input("Enter a position: "))
            with connection.cursor() as cursor:
                pe = "Select player_efficiency, position From stats INNER JOIN player on stats.player_name= player.player_name where position = %s"
                cursor.execute(pe, (postion_input,))
                result = cursor.fetchone()
                for key, value in result.items():
                    print(value)
                print()

        elif choice == 5:
            print("Bye!")
            break
        else:
            print("That is not a valid input. Please try again.")
            print()

finally:
    connection.close()

