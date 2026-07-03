from datetime import datetime

def get_employees():
    """Функция получения списка сотрудников"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Получение данных о сотрудниках из базы данных...")
    employees = ["Иван Петров", "Мария Сидорова", "Алексей Иванов", "Елена Смирнова"]
    print(f"Найдено сотрудников: {len(employees)}")
    for emp in employees:
        print(f"  - {emp}")
    return employees