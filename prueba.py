import re
a=[m.start() for m in re.finditer('test', 'test test test test')]
b= [m.start() for m in re.finditer('(?=sps)', 'spsps sps sps')]

print(b)

print(f'hola {b}')