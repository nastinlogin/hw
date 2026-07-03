from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    """Основная функция программы"""
    print("="*50)
    print("ПРОГРАММА БУХГАЛТЕРИЯ")
    print(f"Текущая дата и время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print("="*50)
    
    print("\n1. Загрузка данных о сотрудниках:")
    get_employees()
    
    print("\n2. Расчет заработной платы:")
    calculate_salary()
    
    print("\n" + "="*50)
    print("Программа завершена успешно!")
    print("="*50)

if __name__ == '__main__':
    main()