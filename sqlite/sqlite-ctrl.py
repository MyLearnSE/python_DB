import sqlite3

conn = sqlite3.connect('.db')
cursor = conn.cursor()

appDesc = """
Please input action code :
1 - Insert data
2 - Update data
3 - Delete data
--- --- ---
0 - exit
"""

while True:
    cursor.execute('SELECT * FROM app_info;')
    data = cursor.fetchall()
    
    print("目前app_info table 的內容:")
    for i in data:
        print(f"id={i[0]}, name={i[1]}, version={i[2]}, authoe={i[3]}, date={i[4]}, remark={i[5]}")

    ctrl = input(appDesc)

    if ctrl == "0":
        break
    elif ctrl == "1":
        sql = """
        INSERT INTO app_info(name, version, author, date, remark)
        VALUES('APP', '1.0.1', 'Amy', '2022-10-19', 'DEMO');
        """
        cursor.execute(sql)
        conn.commit()
    elif ctrl == "2":
        row_id = input ("id = ? :")
        sql = """
        UPDATE app_info SET name='XXX', version='1.1.9' WHERE id={};
        """.format(row_id)
        cursor.execute(sql)
        conn.commit()
    elif ctrl == "3":
        row_id = input("id = ? :")
        sql = """
        DELETE FROM app_info WHERE id={};
        """.format(row_id)
        cursor.execute(sql)
        conn.commit()

cursor.close()
conn.close()


