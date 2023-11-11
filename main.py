import json


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


filename = 'operations.json'
operations_list = load_json(filename)


"""Последние 5 выполненных (EXECUTED) операций выведены на экран."""
def formatted_executed(data):
    operations_executed = [op for op in data if op.get('state') == 'EXECUTED']
    if len(operations_executed) >= 5:
        last_5_executed_operations = operations_executed[-5:]
        operations_executed_sorted = sorted(last_5_executed_operations, key=lambda x: x['date'], reverse=True)[:5]
        return operations_executed_sorted


"""Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)."""
def load_datetime(date):
    date_list = date.split('T')[0].split('-')
    return '.'.join(date_list[::-1])


"""Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX """
def mask_number(number):
    return f"{number[:4]} {number[4:8]}** **** {number[-4:]}"


"""Вывод последних 5 операций"""
last_5_operations = formatted_executed(operations_list)


"""Вывод информации о последних 5 операциях"""
for operation in last_5_operations:
    date = operation['date'][:10]
    description = operation['description']
    from_account = mask_number(operation.get('from', ''))
    to_account = f"Счет **{operation['to'][-4:]}"
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    print(f"{date} {description}")
    print(f"{from_account} -> {to_account}")
    print(f"{amount} {currency}")
    print()
