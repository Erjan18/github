x = int(input())
i = 0
a =[]
if x >= 1 and x <= 100:
    while i < x:
        word = input()
        if len(word) > 10:
            lenght = len(word) - 2
            string = word[0]+str(lenght)+word[-1]
            a.append(string)
        else:
            a.append(word)
        i =+1
for string in a:
    print(string)