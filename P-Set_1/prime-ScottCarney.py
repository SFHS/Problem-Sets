import random
import time
import turtle


def draw_square(x):
    for d in range(4):
        turtle.forward(x)
        turtle.left(90)
def draw_smile(x):
    draw_square(100)
    turtle.up()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.down()
    draw_square(5)
    turtle.forward(5)
    turtle.up()
    turtle.forward(40)
    turtle.down()
    draw_square(5)
    turtle.forward(5)
    turtle.right(90)
    turtle.up()
    turtle.forward(60)
    turtle.right(45)
    turtle.down()
    turtle.forward(7)
    turtle.right(45)
    turtle.forward(42)
    turtle.right(45)
    turtle.forward(7)
    turtle.up()
    turtle.forward(150)
def ln(x):
    n = 100000000
    return n * ((x ** (1/n)) - 1)


def log(x):
	k = (ln(10))**(-1)
	return ln(x)*k


def frequency_of_primes(x):
	return x*(log(x)**(-1))




while 1==1:
    print('')
    wait = input('Press Enter')
    n= input('Which prime number would you like? ')
    n= int(n)
    pList = []
    a = 1
    c = 0
    s = 0
    w = 0
    q = 0
    m = 0
    b = 10000000000
    v = 0
    if n == 0:
        print('')
        print('I do not know')
        print('')
        print('Dividing by zero...')
        time.sleep(2)
        for t in range(1000):
            r = random.randrange(0,10000000)
            print(r)
        print('')
        print('Overload')
        quit()
    if n == 1:
        print('')
        print('2')
        print('done')
    if n == 2:
        print('')
        print('3')
        print('done')
    if n > 2:
        for z in range(2, n):
            l = int(frequency_of_primes(z))
            m = m + l
        for i in range(m+1):
            pList.append(i+2)    
        for x in range(1, m):
            q = pList[x]
            s=0
            if a < n:
                for y in range(a):
                    w = pList[y]
                   # print (w)
                   # print ('w')
                    if q%w != 0:
                        s = s+1
                    if s == a:
                        s = 0
                        pList[a] = q
                        a = a + 1
                    if a == n:
                        print('')
                        print(pList[n-1]);
                        print('done')
                        draw_smile(100)


