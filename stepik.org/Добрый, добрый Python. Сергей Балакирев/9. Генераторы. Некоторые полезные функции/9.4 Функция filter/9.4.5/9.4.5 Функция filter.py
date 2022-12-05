
email = 'abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'
result = __import__('re').findall(r'[a-zA-Z0-9_]+?@[a-zA-Z]+\.[a-z]+', email)
print(result)
