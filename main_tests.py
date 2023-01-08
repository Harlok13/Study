from collections import Counter
def find_secret_message(p):
    res = dict(Counter(p.lower().replace('.', '').split()))
    return ' '.join([k for k, v in res.items() if v > 1])

print(find_secret_message('This is a test. this test is fun.'))
