class Person:
    employ_count = 0
    def __init__(self,name,last_name,email,password,otchestvo='Ivanov'):
        self.name = name
        self.surname = last_name
        self.fathername = otchestvo
        self.employ_count +=1
        self.email = email
        self.password = password


    def __str__(self):
        return str(self.name)+' '+str(self.surname)+' '+str(self.fathername)

    def register(self,check_password):
        if self.password == check_password:
            return 'Вы зарегались'
        return 'Неверные данные'

    def auth(self,email,password):
        if self.email == email and self.password == password:
            return 'Вы авторизировались'
        return 'Вы ввели неверные данные'

    def write_to(self):
        with open('text.txt','a')as f1:
            f1.write(self.email+self.password)
        return f1

    def write_to_dict(self):
        dict_person = dict(name=self.name,lastname=self.surname,email=self.email)
        return dict_person

new_user = Person(name='Mary',last_name='Jane',email='spiderman@g.com',password='qwert')
register_user = new_user.register(check_password='qwert')
user_auth=new_user.auth('spiderman@g.com','qwert')
print(new_user.write_to_dict())






















