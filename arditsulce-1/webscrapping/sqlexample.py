import sqlite3

connection = sqlite3.connect('webscrapping.db')
cursor = connection.cursor()

def get_data():
    cursor.execute('SELECT * FROM events')
    result = cursor.fetchall()
    return result

new_rows = [('Mouse', 'Michigan', '2023.05.12'), ('Mice', 'Florida', '2023.05.11')]
def insert_data(newrows):
    cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
    connection.commit()
    get_data()

if __name__ == '__main__':
    print(get_data())
    insert_data(new_rows)

