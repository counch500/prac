import sys

# Шаг 1: Считываем входные данные как байты
data = sys.stdin.buffer.read()

# Шаг 2: Декодируем входные данные из UTF-8 (с неправильной интерпретацией Latin1)
decoded_utf8 = data.decode("utf-8", errors="replace")

# Шаг 3: Преобразуем их в байты Latin1
encoded_latin1 = decoded_utf8.encode("latin1", errors="replace")

# Шаг 4: Декодируем байты Latin1 в текст, интерпретируя их как CP1251
decoded_cp1251 = encoded_latin1.decode("cp1251", errors="replace")

# Шаг 5: Кодируем результат обратно в UTF-8 и выводим
sys.stdout.buffer.write(decoded_cp1251.encode("utf-8"))
