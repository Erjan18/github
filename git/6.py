list_1 = list(map(int,input().split()))
num = int(input())
j = 0
if num in list_1:
    index_num = list_1.index(num)
    while j < index_num:
        list_1.pop(0)
        j +=1
    print(list_1)
elif num not in list_1:
    print(list_1)
elif len(list_1) == 0:
    print(list_1)