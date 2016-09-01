'''
Martin Gardner - Persistence
A number's persistence is :
The number of steps required to reduce it to a single digit by multiplying all its digits to obtain a second number
Then multiplying all the digits of that number to obtain a third number, and so on until a one-digit number is obtained.
For example : 77 has a persistence of four because it requires four steps to reduce it to one digit: 77-49-36-18-8.
The smallest number of persistence one is 10
The smallest of persistence two is 25
The smallest of persistence three is 39
The smaller of persistence four is 77
What is the smallest number of persistence five?

python solution:(brute force with dynamics programming):
'''
Lookup = []
for i in range(0,10,1):
    Lookup.append(0)
Found = False
index = 9
while Found==False:
    index += 1
    strindex = str(index)
    mult = 1
    for i in strindex:
        mult *= int(i)
    prevPersistence = Lookup[mult]
    numberPersistence = prevPersistence + 1
    Lookup.append(numberPersistence)
    if numberPersistence == 5:
        print index
        Found = True
