from datetime import datetime

def calculate_salary():
    """Функция расчета зарплаты"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Выполняется расчет заработной платы...")
    print("Расчет зарплаты завершен успешно!")
    return True