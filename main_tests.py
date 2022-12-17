"""
1y = 31 536 000
1d = 86400s
1h = 3600s
1m = 60s
"""


def format_duration(sec):
    t = __import__('time').gmtime(sec)
    y, d, h, m, s = t.tm_year - 1970, t.tm_yday, t.tm_hour, t.tm_min, t.tm_sec
    years = (f'{y} years ', f'{y} year ')[y == 1]
    days = (f'{d - 1} days ', f'{d - 1} day ')[d == 1]
    hours = (f'{h} hours ', f'{h} hour ')[h == 1]
    minutes = (f'{m} minutes ', f'{m} minute ')[m == 1]
    seconds = (f'{s} seconds', f'{s} second')[s == 1]
    res = ('', years)[bool(y)] + ('', days)[bool(d - 1)] + \
          ('', hours)[bool(h)] + ('', minutes)[bool(m)] + \
          ('', seconds)[bool(s)]
    r = [f'{v},' if k % 2 else v for k, v in enumerate(res.split())]
    if len(r) > 2:
        r[-2] = f'and {r[-2]}'
        r[-3] = r[-3].rstrip(',')
    return ' '.join(r).rstrip(',')


s1 = 1
s2 = 457
s3 = 1252
s4 = 3532
s5 = 4379
s6 = 31_535_999
s7 = 31_536000
s8 = 98543345
print(format_duration(s8))

# l = len(res.split())
# lst = []
# for k, v in enumerate(res.split(),1):
#     try:
#         if int(v):
#             lst.append(v)
#     except Exception:
#         lst.append(f'{v},')

# r = [v if  for k, v in enumerate(res.split())]
def format_duration(sec):
    t = time.gmtime(sec)
    y, d, h, m, s = t.tm_year - 1970, t.tm_yday, t.tm_hour, t.tm_min, t.tm_sec
    years = (f'{y} years ', f'{y} year ')[y == 1]
    days = (f'{d - 1} days ', f'{d - 1} day ')[d == 1]
    hours = (f'{h} hours ', f'{h} hour ')[h == 1]
    minutes = (f'{m} minutes ', f'{m} minute ')[m == 1]
    seconds = (f'{s} seconds', f'{s} second')[s == 1]
    res = ('', years)[bool(y)] + ('', days)[bool(d-1)] + \
          ('', hours)[bool(h)] + ('', minutes)[bool(m)] + \
          ('', seconds)[bool(s)]
    r = [f'{v},' if k % 2 else v for k, v in enumerate(res.split())]
    if len(r) > 2:
        r[-2] = f'and {r[-2]}'
        r[-3] = r[-3].rstrip(',')
    print(r)
    print(y)
    return ' '.join(r).rstrip(',')
