import sqlite3


def main():
    name = input()
    sql_cond_1 = input()
    sql_cond_2 = input()
    sql_sort_column = input()

    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    sql_command = "SELECT condition " \
                  "FROM Talks " \
                  "WHERE {} AND {} " \
                  "ORDER BY {} ASC".format(sql_cond_1,
                                           sql_cond_2,
                                           sql_sort_column)

    cursor.execute(sql_command)
    solution = cursor.fetchall()
    for item in solution:
        print(item[0])


if __name__ == '__main__':
    main()
