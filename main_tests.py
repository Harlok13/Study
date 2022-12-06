lst_in = ['0230',
'0456',
'789',
'1023456789']
gen = (list(i) for i in lst_in)


print(True for i in lst_in if lst_in[0][0] in list(gen))
