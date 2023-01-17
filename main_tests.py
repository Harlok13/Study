sec_in = 3721
h, minutes = divmod(sec_in, 3600)
m, s = divmod(minutes, 60)
print(f'{h}:{m:02d}:{s:02d}')
