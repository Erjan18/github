def auth(login,password):
    if len(login) < 20 and not password.isalpha() and not password.isdigit():
        return True
    else:
        return False
login = 'user'
password = 'ewr234'

def counter(money,tovar):
    if money > tovar:
        result = money - tovar
        return result
    else:
        return 'У вас недостаточно средств'
catalogue = {'microphone':1500,'air-pods':4000,'beats':8000,
             'samsung a5': 10500,'Acer ASPIRE e15': 30000,
             'hard drive':6400,'iphone 8s': 16000,'iphone X': 40000,
             'mouse RX7':8000,'hikvision laland':2280,'kocom': 3990,
             'HIKVISION DS-KD-DIS': 5410, 'commaX cdv':9560,
             'TP-LINK TL-WR841N':1450,'hoco m60': 120,
             'SVEN ap':290,'panasonic': 32460,'Falcon sdd ADATA':6650,
             'Apple Watch':8000}

a = []
num = 2
def cartage():
    for i in range(2):
        product = input('Введите товар для покупки:')
        a.append(product)
    return a
purchace = cartage()

login = 'user123'
password = 'ewr234'
user_check = input('имя')
password_check = input('пароль')
def buy(purchace):
    if auth(login=login, password=password):
        money = int(input())
        total_money = money
        for let in purchace:
            if let in catalogue:
                key_price = catalogue[let]
                money = counter(money,key_price)
                result = total_money - money
        return result
    else:

        return 'Войдите в систему'

print(buy(purchace))




