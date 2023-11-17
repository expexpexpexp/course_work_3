from utils import load_datetime, formatted_executed, mask_number, load_json


def main():
    """"""
    filename = 'operations.json'
    operations_list = load_json(filename)
    last_5_operations = formatted_executed(operations_list)  # Вывод последних 5 операций
    for operation in last_5_operations:  # Вывод информации о последних 5 операциях
        date = load_datetime(operation['date'])
        description = operation['description']
        from_account = mask_number(operation.get('from', ''))
        to_account = f"Счет **{operation['to'][-4:]}"
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}")
        print()


if __name__ == "__main__":
    main()
