"""
Задача:

Необходимо провести верификацию введенных пользователем данных. 
Проверяются ключи на предмет соответствия написания с определенными в list_keys значениями, а также наличие открывающих и закрывающих скобок.
"""


def validate_text(test_text, list_keys):
    # Проверка на наличие открывающих и закрывающих скобок
    if test_text.count('{') != test_text.count('}'):
        return "Ошибка: несоответствие количества открывающих и закрывающих скобок."

    # Извлечение всех ключей из текста
    keys_in_text = set()
    start = 0
    while True:
        start = test_text.find('{', start)
        if start == -1:
            break
        end = test_text.find('}', start)
        if end == -1:
            return "Ошибка: несоответствие количества открывающих и закрывающих скобок."
        keys_in_text.add(test_text[start + 1:end])
        start = end + 1

    # Проверка на соответствие ключей из текста с ключами из списка
    for key in keys_in_text:
        if key not in list_keys:
            return f"Ошибка: некорректный ключ '{key}'."

    return test_text


if __name__ == "__main__":
    Test_text = '''{name}, ваша запись изменена:

    ⌚️ {day_month} в {start_time}

    👩 {master}

    Услуги:

    {services}'''

    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

    result = validate_text(Test_text, list_keys)
    print(result)
