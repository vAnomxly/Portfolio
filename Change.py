
def get_input():

    not_float = 1
    second = 1
    D = [0]

    while not_float != 0 and second != 0:
        mon = input("Type in any amount of money, cents included (__.__) :")
        try:
            float(mon)
            if "." in mon:
                result = mon.index('.')
                print("You have this much money : $"+mon)
                cents=(mon[result+1] + mon[result+2])
                not_float = 0
                second = 0


            elif "." not in mon:
                print("Please type any amount of money in this format __.__ ")
                not_float = 1
        
                
        except ValueError:
            print("Please type any amount of money in this format __.__ ")
            not_float = 1


        except IndexError:
            print("Please type any amount of money in this format __.__ ")
            second = 1


    dig = 0
    amt = 0

    for y in range(0, len(mon)):
    
        if (result>dig):
            amt=amt+1
        dig = dig + 1

    dig = 0
    D = [0]*amt
    for x in range(0, len(mon)):
    
        if (result>dig):
            dollars = mon[dig]
            D[dig] = dollars
        dig = dig + 1


    print("Dollars :", end='')
        
    gawk = str("")
    for i in D:
        gawk = gawk + (i)
    print(gawk)

    return cents, gawk


def get_change():
    cents, gawk = get_input()
    dollars = int(gawk)
    
    
    print("Cents :" + cents)
    cents = int(cents)
    
    h = 0
    f = 0
    t = 0
    ten = 0
    five = 0
    one = 0
    Q = 0
    D = 0
    N = 0
    P = 0
    
    while dollars%100 != dollars:
        dollars = dollars-100
        h = h+1
    while dollars%50 != dollars:
        dollars = dollars-50
        f = f+1
    while dollars%20 != dollars:
        dollars = dollars-20
        t = t+1
    while dollars%10 != dollars:
        dollars = dollars-10
        ten = ten+1
    while dollars%5 != dollars:
        dollars = dollars-5
        five = five+1
    
    one = dollars

    while cents%25 != cents:
        cents = cents-25
        Q = Q+1
    while cents%10 != cents:
        cents = cents-10
        D = D+1
    while cents%5 != cents:
        cents = cents-5
        N = N+1
    P = cents
    
    h = str(h)
    f = str(f)
    t = str(t)
    ten = str(ten)
    five = str(five)
    one = str(one)
    Q = str(Q)
    D = str(D)
    N = str(N)
    P = str(P)
    print("Hundred dollar bills : "+h)
    print("Fifty dollar bills : "+f)
    print("Twenty dollar bills : "+t)
    print("Ten dollar bills : "+ten)
    print("Five dollar bills : "+five)
    print("One dollar bills : "+one)
    print(" ")
    print("Quarters : "+Q)
    print("Dimes : "+D)
    print("Nickles : "+N)
    print("Pennies : "+P)
    



get_change()





    

