text = 'Hello World its pytgon programmsit im new here'
space = text.index(' ')
print(text[:space])
with open('../text.txt', 'w') as f1:
    f1.write(text[:space])
