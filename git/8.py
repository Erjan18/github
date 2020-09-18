#Проверить все ли символы в строке являются заглавными.
#Если строка пустая или в ней нет букв - программа должна вернуть True.
text = input()
if text.isupper():
    print(text)
elif len(text) == 0 or not text.isalpha():
    print(True)
