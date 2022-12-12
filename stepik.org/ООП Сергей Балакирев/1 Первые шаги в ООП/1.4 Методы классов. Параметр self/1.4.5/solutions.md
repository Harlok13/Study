```
class Translator:
    def __init__(self):
        self.d = {}
        
    def add(self, eng, rus):
        lst = self.d.setdefault(eng, [])
        if not rus in lst:
            lst.append(rus)

    def remove(self, eng): 
        if eng in self.d:
            del self.d[eng]

    def translate(self, eng):
        return self.d.get(eng, [])

tr = Translator()
for pair in ('tree - дерево', 'car - машина', 'car - автомобиль', 'leaf - лист', 
              'river - река', 'go - идти', 'go - ехать', 'go - ходить', 'milk - молоко'):
    tr.add(*pair.split(' - '))
    
tr.remove('car') 
print(*tr.translate('go'))
```
```
class Translator:
    WORDS = dict()
    
    def add(self, eng, rus):
        self.WORDS.setdefault(eng, []).append(rus)
    
    def remove(self, eng):
        del self.WORDS[eng]
    
    def translate(self, eng):
        return self.WORDS[eng]


eng_words = ("tree", "car", "car", "leaf", "river", "go", "go","go", "milk")
rus_words = ("дерево", "машина", "автомобиль", "лист", "река", "идти", "ехать", "ходить", "молоко")

tr = Translator()
for eng, rus in zip(eng_words, rus_words):
    tr.add(eng, rus)

tr.remove("car")
print(*tr.translate("go"))
```
