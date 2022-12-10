
def get_tag(tag='h1'):
    def outer(func):
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'

        return wrapper
    return outer


@get_tag('div')
def get_lower_string(s):
    """Приводит строку к нижнему регистру"""
    return s.lower()


print(get_lower_string('ДЕКОРАТОРЫ'))
