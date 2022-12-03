def get_name_tag(tag):
    def get_tag(s):
        return f'<{tag}>{s}</{tag}>'
    return get_tag

tag, s = 'div', 'Сергей Балакирев'
print(get_name_tag(tag)(s))
