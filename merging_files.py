import os


def merge_files(file_list, output_file):
    files_data = []

    # Считываем данные из каждого файла
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_data.append((file_name, len(lines), lines))

    # Сортируем файлы по количеству строк
    files_data.sort(key=lambda x: x[1])

    # Записываем результат в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in files_data:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)
            out_file.write("\n")  # Пустая строка между файлами


# Пример использования:
file_list = ['1.txt', '2.txt', '3.txt']  # Замените на ваши файлы
merge_files(file_list, 'result.txt')
result_file_list = 'result.txt'
print(f"Содержимое объединено в файл '{result_file_list}'")