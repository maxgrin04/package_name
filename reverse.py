def reverse(string):
    return string[::-1]


def process_files(input_file, output_file):
    try:
        # Чтение текста из входного файла
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Проверка, что текст успешно прочитан
        assert text, f"Файл '{input_file}' пустой или не прочитан."
        
        # Переворот текста
        reversed_text = reverse(text)
        
        # Запись результата в выходной файл
        with open(output_file, 'w') as file:
            file.write(reversed_text)
        
        print(f"Текст успешно перевёрнут и сохранён в '{output_file}'")
    
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")