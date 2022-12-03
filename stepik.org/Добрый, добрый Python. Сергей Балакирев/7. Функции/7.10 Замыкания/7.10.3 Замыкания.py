def get_tag(st):
    def get_tag_name(tag):
        return f'<{tag}>{st}</{tag}>'
    return get_tag_name

print(get_tag('Balakirev')('h1'))
