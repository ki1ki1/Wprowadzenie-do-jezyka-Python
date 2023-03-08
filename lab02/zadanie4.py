from datetime import datetime
print('{:10.5}'.format("xylophone"))
print(f'{"xylophone":10.5}')

print('{:f}'.format(3.141592653589793))
print(f'{3.141592653589793:f}')

print('{:{align}{width}}'.format('test', align='^', width='10'))
print(f'{"test":{"^"}{10}}')

print('{:>10}'.format("test"))
print(f'{"test":>10}')

print('{:10}'.format("test"))
print(f'{"test":10}')

print('{:%Y-%m-%d %H:%M}'.format(datetime.now()))
print(f'{datetime.now():%Y-%m-%d %H:%M}')