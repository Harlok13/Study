def read_and_count(file: str) -> str:
    """
    Открывает файл и считает кол-во слов.
    Текст приводится к списку, содержащий слова в нижнем регистре,
    исключающий символы.
    Возвращает значения ключей одной строкой через пробел.
    Пример return: '2 3 1 1 5'
    """
    with open(file, 'r') as f:
        text = f.read().lower().split()
        text_strip = list(map(lambda x: x.strip('.,!?;:()-_—'), text))
        cnt_words = __import__('collections').Counter(text_strip)
        return ' '.join(map(str, dict(cnt_words).values()))
