import sqlite3

conn = sqlite3.connect('.db')

cursor = conn.cursor()
cursor.execute('SELECT * FROM app_info;')
data = cursor.fetchall()
cursor.close()
conn.close()

print("data is =>", data)
print("data type => ", type(data))
print("data[0] type => ", type(data[0]))

for i in data:
    print(i)
    app_id, app_anme, app_ver, app_author, app_date, app_remark = i
    print("id =>", app_id)
    print("name =>", app_anme)
    print("version =>", app_ver)
    print("author =>", app_author)
    print("date =>", app_date)
    print("remark =>", app_remark)

