def chislo(num):
    dell = 0
    for i in range(2,num-1):
        if num % i ==0:
            dell +=1
    if dell == 0:
        return True
    else:
        return False
