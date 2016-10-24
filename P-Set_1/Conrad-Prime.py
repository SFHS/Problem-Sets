import time

while 0 == 0:

    test = 4
    a = 0
    y = 0
    amount = input("What number prime would you like? ")
    time4 = time.clock()
    if int(amount) == 0:
        print("No.")
    elif int(amount) == 1:
        print("2 is your prime, fool.")
    elif int(amount) == 2:
        print("3 is your prime, fool.")
    elif int(amount) == 3:
        print("5 is your prime, fool.")
    else:
        amount = float(amount) - float(1)
        while y != 1:
            c = 0
            for i in range(2,int((test)/2)):
                p = test%i
                if p == 0:
                    c = c + 1
            if c == 0:
                a = a + 1
            if float(a) == float(amount):
                y = y + 1
                time2 = time.clock()
                time3 = time2 - time4
                print(str(test) + " is your prime, fool.")
                print(str(time3))
            test = test+1



        
    


    
    
    
