'''
Sam and Polly are perfectly logical mathematicians. A student walks in and says: “I’m thinking of two numbers x and y, with 3 <= x <= y <= 97. I’ll tell their sum to Sam, and their product to Polly.” She does so, then leaves, and the following conversation takes place:
Sam (to Polly): You can’t know what x and y are.
Polly (to Sam): That was true, but now I know.
Sam (to Polly): Now I know too.
Find x and y.

python solution:
'''
def outputDivisors(number):
    pair = []
    for i in range(3,number):
        if 3<=i and i<=97:
            other_number = number/i
            if number%i ==0 and 3<= other_number and other_number<= 97:
                tobeadded = sorted([i,other_number])
                if tobeadded not in pair:
                    pair.append(tobeadded)
    return pair
def outputPairFromSum(Sum):
    pair = []
    for i in range(3,(Sum+3)/2):
        if 3<=i and i<=97:
            other_number = Sum-i
            if 3<= other_number and other_number<= 97:
                tobeadded = sorted([i,other_number])
                if tobeadded not in pair:
                    pair.append(tobeadded)
    return pair

def main():
    minbound = 3
    maxbound = 97
    Hashoutputpairsfromsum = {}
    Sam1stArgument = []
    
    for sum in range(minbound*2,maxbound*2+1,1):
        Hashoutputpairsfromsum[sum] = outputPairFromSum(sum)
    for sum in range(minbound*2,maxbound*2+1,1):
        pairs = Hashoutputpairsfromsum[sum]
        boolean = True
        for pair in pairs:
            product = pair[0]*pair[1]
            divisors = outputDivisors(product)
            if len(divisors) < 2:
                boolean = False
        if boolean ==True:
            Sam1stArgument.append(sum)
    
    for sum in Sam1stArgument:
        pairs = Hashoutputpairsfromsum[sum]
        Allpairs = []
        for pair in pairs:
            product = pair[0]*pair[1]
            divisors = outputDivisors(product)
            Polly2ndArg = 0
            for divisor in divisors:
                if (divisor[0]+divisor[1]) in Sam1stArgument:
                    Polly2ndArg += 1
            if Polly2ndArg == 1:
                Allpairs.append(pair)
        if len(Allpairs) ==1:
            print Allpairs
print main()

