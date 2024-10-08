"""
Задача:

Сгрупировать по уникальности пары id, version в list_version
"""


def count_elements(list_version):
    # Словарь для хранения пар и их счетчиков
    count_dict = {}

    # Подсчет пар
    for id, version in list_version:
        if (id, version) in count_dict:
            count_dict[(id, version)] += 1
        else:
            count_dict[(id, version)] = 1

    # Формирование результата
    result = [[id, version, count] for (id, version), count in count_dict.items()]

    return result


if __name__ == "__main__":
    list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]
    result = count_elements(list_version)
    print(result)
