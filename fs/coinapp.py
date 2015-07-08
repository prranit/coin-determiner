#This script contains the algorithm to coin determiner

def coin(num):

    b = int(num)
    
    coins = [1, 5, 7, 9, 11]

    if b in coins:
        a = 1

    # minimum number of coins for specific change values x
    min_amounts= [-1] * (b+1)
    

    # zero produces 0 amount of coins
    min_amounts[0] = 0

    # keep adding to minimum, storing in min_amounts
    for x in range(1, b+1):
        minimum = -1
        
        for i in coins:
            index = x - i

            if index >= 0:

                if (min_amounts[index] < minimum) or (minimum == -1):
                    minimum = min_amounts[index]
            else:
                break
        
        min_amounts[x] = 1 + minimum
       
    #aggregate of all the minimums
    a = min_amounts[b]

    return a


print coin(11)
