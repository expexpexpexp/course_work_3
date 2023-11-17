import json

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_datetime(date):
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)."""
    date_list = date.split('T')[0].split('-')
    return '.'.join(date_list[::-1])


def formatted_executed(data):
    """Последние 5 выполненных (EXECUTED) операций выведены на экран."""
    operations_executed = [op for op in data if op.get('state') == 'EXECUTED']
    operations_executed_sorted = sorted(operations_executed, key=lambda x: x['date'], reverse=True)[:5]
    return operations_executed_sorted


def mask_number(number):
    """Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX """
    return f"{number[:4]}{number[4:8]}** **** {number[-4:]}"

