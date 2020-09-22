def regiztration(username,password,check_passw,):
    with open('test.txt', 'a') as f1:
        f1.write(username)
        f1.write(password)
    if password == check_passw:
        return ['Вы успешно зарегались',username,password]
    else:
        return 'Данные введены неверно'
username = 'username'
password = 'passw'
check_password = 'passw'
def autorization(login,passw):
    with open('test.txt','r') as f2:
        read_file = f2.read()
        check_login = read_file[:len(username)]
        check_password = read_file[len(password)]
    if login == username and passw == password:
        return 'Вы успешно авторизавались'
    else:
        return 'Вы ввели неверные данные'
login = 'username'
passw = 'password'
print(regiztration(username=username,password=password,check_passw=check_password))
print(autorization(login=login,passw=password))