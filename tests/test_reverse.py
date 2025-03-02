from reverse import process_files


input_file = 'input.txt'
output_file = 'output.txt'

process_files(input_file, output_file)

def test_reverse():
    test_input = 'test_input.txt'
    test_output = 'test_output.txt'
    
    # Создаём тестовый файл
    with open(test_input, 'w') as file:
        file.write("Привет, мир!")
    
    # Запускаем процесс
    process_files(test_input, test_output)
    
    # Проверяем результат
    with open(test_output, 'r') as file:
        result = file.read()
    
    assert result == "!рим ,тевирП", "Тест не пройден"
    print("Тест пройден успешно!")