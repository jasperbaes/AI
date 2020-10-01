def extended_euclidean(b, n):
    # We calculate gcd(b, n)
    # At each iteration we perform the following steps:
    # - the new value of b is the old value of n
    # - the new value of n is the remainder of b/n
    # - we call the quotient q = b/n
    #
    # For the extended euclidean algorithm, we also 
    # # calculate these formulas:
    # x(1) = x(i-2) - q(i) * x(i-1) 
    # # y(i) = y(i-2) 9(i) * y(i-1)
    #
    # x0 is x(i-2), yo is y(i-2)
    # xi is x(i-1), yi is y(i-1) 
    # q is q(i)
    #
    # the final values of x0, y0 are the resulting x,y 

    print('\n {}\t{}\t{}\t{}'.format("Ri", "Qi", "Xi", "Yi"))
    print(" =================================")
    
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n 
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1 
        # print(q, b, n, x1, y1)
        # print('{}\t{}\t{}\t{}\t{}'.format(q, b, n, x1, y1))
        print(' {}\t{}\t{}\t{}'.format(n, q, x1, y1))
    return b, x0, y0

def gcd(a, b):
    g, x, y = extended_euclidean(a, b)
    return g

def mulinv(b, n):
    # the extended euclidean algorithm also
    # calculates x, y such that gcd(b,n) = b*x + n*y
    #
    # if we calculate in modulo n
    # gcd(b, n) = b*x + n*y = b*x
    # and we know b and n are relatively prime
    # so gcd(b,n) = 1 = b*x
    # so x = multiplicative inverse of b modulo n
    g, x, y = extended_euclidean(b, n)
    if g == 1:
        return x % n


print("Input parameters for x1 modx2")
x1 = input(" x1: \t")
x2 = input(" x2: \t")
extended_euclidean(int(x1), int(x2))