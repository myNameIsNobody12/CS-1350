
def looPrint(t):
    if t > 0:
        print("Howdy CS2")
        looPrint(t - 1)
i =int(input('lets get the show started '))
looPrint(i)
print(' the end :)')

def fact(n):
    f = 1
    for i in range(1, n+1):
        f= f*i
    return f
print(fact(5))
def looFact(n): # number of times
    if n == 0:
        return 1
    else:
        return n * looFact(n - 1)
print(looFact(5))
def power(n, i):
    n1 = n
    for i in range(1 , i):
        n *= n1
    return n
print(power(5,4))
def looPow(n, i): # coefficent, power
    if i == 0:
        return 1
    else:
        return n * looPow(n, i-1)
print(looPow(5, 4))

li = [5,6,-2,4,10,13,11] #list for  looSum
def looSum(l, s, e):# list start end
    if e < s: # base case
        return 0
    else:
        return l[s] + looSum(l, s+1, e) # 5 + (6 + (-2 +...11)) think dominos 
print(looSum(li,0,6))

