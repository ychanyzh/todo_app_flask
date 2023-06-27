import sqlite3

DATABASE = 'todo.db'

def create_tasks_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        completed INTEGER DEFAULT 0
                    )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tasks_table()
