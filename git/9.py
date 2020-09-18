spisok = [1,2,3,4,5,6,7]
if len(spisok) > 1:
    spisok.insert(len(spisok),spisok[0])
    spisok.pop(0)
    print(spisok)
elif len(spisok) == 0 or len(spisok) == 1:
    print(spisok)