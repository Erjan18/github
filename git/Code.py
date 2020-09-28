# import sendgrid
# from sendgrid import Mail,Email,Content
# sendgrid_api_key = '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'
# SUBJECT = 'code'
# sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
# def sendgrid_email(code,email):
#     body = 'your code = '+code
#     message = Mail(
#         from_email='maximneveraa@gmail.com',
#         to_emails=email,
#         subject=SUBJECT,
#         plain_text_content=body)
#     response = sg.send(message)
# def registration(username,password,check_password):
#     global code
#     code = '123456'
#     if password == check_password:
#         sendgrid_email(code,'emma.apigrid@gmail.com')
#     else:
#         return 'Повторите попытку'
# username = 'username'
# password = 'password'
# check_password = 'password'
# registration(username=username,password=password,check_password=check_password)
def check_code(code):
    if check_code == code:
        print(check_code)
    else:
        print(code)
code = '123456'
check_code(code=123456)
strings = ['Samsung j5',
           'samsung galaxy',
           'iphone 10',
           'iphone 5S',
           'samsung a9',
           'ASUS-Roc',
           'Acer HyperX',
           'Macbook Air 18',
           'Macbook Pro 18',
           'geforce gtx460',
           'HDD 1TB',
           'SSD Adata 3100/1400mbs',
           'HDD 2TB',
           'Mac 19',
           'amd Ryzen 490',
           'GeForce TI 2020',
           'SSD Kingston 512 gb',
           'SSD Adata 1TB',
           'Acer zenbook',
           'Asus razer'
           ]
def write_to(strings):
    with open('map.txt','a') as f1:
        for sentence in strings:
            f1.write(sentence.lower() + '\n')
print(write_to(strings))
def phones():
    with open('map.txt','r') as f1:
        pro = f1.readlines()
        for i in pro:
            if i.startswith('samsung j5') or i.startswith('samsung galaxy') or i.startswith('iphone 10') or i.startswith('iphone 5S') or i.startswith('samsung a9'):
                with open('phones.txt', 'a') as f2:
                    f2.write(i)
            elif i.startswith('asus-roc') or i.startswith('acer hyperx') or i.startswith('macbook air 18') or i.startswith('macbook pro 18') or i.startswith('mac 19') or i.startswith('acer zenbook') or i.startswith('asus razer'):
                with open('Computer.txt','a') as f3:
                    f3.write(i)
            elif i.startswith('geforce gtx460') or i.startswith('geForce ti 2020') or i.startswith('amd ryzen 490'):
                with open('videocart.txt','a') as f4:
                    f4.write(i)
            elif i.startswith('hdd 1tb') or i.startswith('hdd 2tb') or i.startswith('ssd kingston 512 gb') or i.startswith( 'ssd adata 1tb'):
                with open('HDD.txt','a') as f5:
                    f5.write(i)
phones()
def open_file(filename):
    with open(filename,'r') as f1:
        var = f1.readlines()
    return var


username = input('Введите категорию:')
if username == 'phones':
    print(open_file('phones.txt'))
elif username =='Computer':
    print(open_file('Computer.txt'))
elif username == 'Videocart':
    print(open_file('Videocar.txt'))
elif username == 'HDD':
    print(open_file('HDD.txt'))
