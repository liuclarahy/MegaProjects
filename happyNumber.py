"""
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
"""

def calculate ( input_number ):
    #print "in calculate, input_number: ", input_number
    sumOfSquare = 0
    for i in str(input_number):
        sumOfSquare = sumOfSquare + int(i)**2

    #print "out calculate, sumOfSquare: ", sumOfSquare
    return sumOfSquare


def isHappyNumber( numberInQ ):
    sumOfSquare = 0
    count = 0
    input_number = numberInQ

    """ 
    print numberInQ
    print sumOfSquare
    print count
    print input_number
    """ 

    while sumOfSquare != 1 :
        #print ("in while loop")
        sumOfSquare = calculate (input_number)
        input_number = sumOfSquare
        #print "sumOfSquare: ", sumOfSquare

        count += 1
        #print "count: ", count
        if count == 1000:
            return sumOfSquare
            #return (str(numberInQ) + " is an unhappy number")

    
    # when sumOfSquare == 1, happy number found
    #return (str(numberInQ) + " is a happy number")
    return sumOfSquare


######################
# test number from 1 to 1000 for happy number, break when first 8 are identified
######################
happyNumberList = []
for x in range(1,1000): 
    sumOfSquare = isHappyNumber(x)
    if sumOfSquare == 1:
        happyNumberList.append(x)
        if len(happyNumberList) == 8:
            break

print happyNumberList
