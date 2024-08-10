# main.py

from logic import DatabaseManager

def main():
    db_manager = DatabaseManager()
    db_manager.create_tables()
    print("Таблицы успешно созданы")

if __name__ == "__main__":
    main()
