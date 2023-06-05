import psycopg2

connection = psycopg2.connect(user='postgres',
                              password = 'q9896',
                              host = '127.0.0.1',
                              port = '5432',
                              database = 'artlesscoder')

cursor = connection.cursor()

cursor.execute('SELECT*FROM employee;')
result = cursor.fetchall()
print(result)

for employee in result:
    print(employee)

cursor.close()
connection.close()
