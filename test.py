run = True
while run:
    a = int(input('введи целое число: '))
    if a < 1000:
        i = (a/2) + (a/a)
        print(i)
    if a >= 1000:
        run = False
        print('меньше 1000')    