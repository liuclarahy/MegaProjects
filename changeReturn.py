"""
Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""

def changeReturn (in_amount):
    bills = [ 5, 1, 0.25, 0.1, 0.05, 0.01 ]
    results = {}

    
    def calculate_change ( amount, billValue ):
        numOfBills = int( amount / billValue )
        remainder = amount % billValue
    
        return remainder, numOfBills



    remainder = in_amount
    for b in bills:
        remainder, numOfBills = calculate_change( remainder, b )  
        results [b] = numOfBills

    return results

results = changeReturn(19.89)
for r in sorted(results, reverse=True):
    print "$%s: %s" % (r, results[r])
