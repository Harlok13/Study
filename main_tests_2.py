placeholder = 'placeholder'
x = [True, 'zzz', 123, True]
temp = str(x).replace('True', placeholder)
print(1 in eval(temp))
