password = input()
with open('../text.txt', 'w') as f1:
    f1.write(password + '\n')
if len(password) > 6:
    print(True)
    with open('../text.txt', 'w') as f1:
        f1.write('true')
else:
    print('False')
    with open('../text.txt', 'w') as f1:
        f1.write('False')