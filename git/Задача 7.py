def Prime(x):
    i = 1
    while x % i != 0:
        i +=1
    if x == i:
        return True
    return False
print(Prime(9))