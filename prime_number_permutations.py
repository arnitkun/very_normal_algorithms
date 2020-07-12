
import itertools

number = 935

def digitize(n):
    i = []
    while(n):
        i.append(n%10)
        n //= 10
    return i

# print(digitize(number))

perms = itertools.permutations(digitize(number))

permlist = []
for p in perms:
    permlist.append(list(p))

# print(permlist)

places = len(permlist[0])
places = 10**places//10
# print(places)

nums = []

for p in permlist:
   
    # print(p)
    
    current_place = places
    
    n = 0
    
    for i in range(len(p)):
        n += current_place*(p[i])
        current_place = current_place//10
    if n not in nums:
            nums.append(n)

# print(nums)

def sieve(n):
    largest = max(n)
    print(largest)
    prime = [True for i in range(largest+1)]
    p = 2
    
    while p*p <= largest:
        if prime[p] == True:
            for i in range(p*p, largest+1, p):
                prime[i] = False
        p += 1
    
    for number in n:
        print(prime[number])
    print(len(prime))

sieve(nums)


    

