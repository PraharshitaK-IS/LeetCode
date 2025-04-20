#https://leetcode.com/problems/happy-number/

#Happy number is a happy number is the sum of squares of the digits eventually turn out to be one
#The process is repeated until you reach a single digit
#If the single digit is 1 : Happy number
#Process Sum(Square of Digits)

def isHappy(n):
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1
