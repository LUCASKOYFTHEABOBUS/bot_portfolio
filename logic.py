import sqlite3
from config import DATABASE

class DatabaseManager:
    def __init__(self, db_name=DATABASE):
        self.db_name = db_name

    def create_tables(self):
        connection = sqlite3.connect(self.db_name)
        with connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS status (
                    status_id INTEGER PRIMARY KEY,
                    status_name TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS skills (
                    skill_id INTEGER PRIMARY KEY,
                    skill_name TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    project_id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    url TEXT,
                    status_id INTEGER,
                    FOREIGN KEY (status_id) REFERENCES status (status_id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS project_skills (
                    project_skill_id INTEGER PRIMARY KEY,
                    project_id INTEGER NOT NULL,
                    skill_id INTEGER NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects (project_id),
                    FOREIGN KEY (skill_id) REFERENCES skills (skill_id)
                )
            ''')
            connection.commit()

# Запуск создания таблиц при прямом запуске файла
if __name__ == '__main__':
    manager = DatabaseManager(DATABASE)
    manager.create_tables()
    print("Таблицы успешно созданы")