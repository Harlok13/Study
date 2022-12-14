"""
__setattr__(self, key, value)__ – автоматически вызывается при изменении свойства key класса;
__getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
__getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
__delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).
"""
