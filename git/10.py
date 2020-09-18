num = int(input())
max = 0
i = 0
string_num = str(num)
while i < len(string_num):
    int_num = int(string_num[i])
    if int_num > max:
        max = int_num
    i +=1
print(max)