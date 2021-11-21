# import sqlite3
# with sqlite3.connect("card.s3db") as conn:
#     cur = conn.cursor()
#
#     # Executes some SQL query
#     cur.execute("""CREATE TABLE IF NOT EXISTS card (
#         id INTEGER,
#         number TEXT,
#         pin TEXT,
#         balance INTEGER DEFAULT 0
#         )""")

    # cur.execute("""INSERT INTO card (
    #    id, number, pin, balance) VALUES
    #    (6, 4000006858501223, 3506, 78099)""")
    #
    # conn.commit()
    # print("Records inserted........")

    # cur.execute("""SELECT * FROM card WHERE balance < 50000 ORDER BY balance DESC LIMIT 3""")
    # result = cur.fetchone()
    # print(result)

    # cur.execute("""SELECT * FROM card WHERE balance < 50000 ORDER BY balance DESC LIMIT 3""")
    # result = cur.fetchall()
    # print(result)

    # cur.execute("""UPDATE card SET balance = 0 WHERE id = 4""")
    # print("Table updated...... ")

    # cur.execute("""DELETE FROM card WHERE id = 6""")
    # print("Contents of the table after delete operation")

    # Commit your changes in the database
    # conn.commit()

