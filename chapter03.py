


def collatz(number):
    if(number == 1):
        return 1
    elif(number % 2 == 0):
        print number // 2
        return collatz(number // 2)
    elif(number % 2 == 1):
        print 3*number+1
        return collatz(3*number+1)


collatz(3)
