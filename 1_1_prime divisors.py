"""
This script finds the number with the maximum number of prime divisors.

Author: Mojtaba Hassanzadeh
Date: March 6, 2024
"""
def divisors(num):
    divs = [d for d in range(2,num+1) if num%d==0]
    return divs

def isprime(num):
    divs = divisors(num)
    if len(divs)==2:
        return True
    else:
        return False

def divisors(num):
    return [d for d in range(1,num+1) if num%d==0]
   
def isprime(num):
    return len(divisors(num))==2
    # divs = divisors(num)
    # if len(divs)==2:
    #     return True
    # else:
    #     return False

# numlist = []
# for i in range(10):
#     num = int(input())
#     numlist.append(num)
numlist = [int(input()) for _ in range(10)]

primeCount = []
for num in numlist:
    primeCount.append(sum(1 for div in divisors(num) if isprime(div)))
    # pr = 0
    # divs = divisors(num)
    # for div in divs:
    #     if isprime(div):
    #         pr+=1
    # primeCount.append(pr)




max_val = max(primeCount)
max_ind = primeCount.index(max_val)

max_value, max_index = max((value, index) for index, value in enumerate(primeCount))
print(f'The number {numlist[max_index]} has {max_value} prime divisors')

max_indices = [index for index, value in enumerate(primeCount) if value==max_val]
print(max_indices)
print(f'The numbers {[numlist[index] for index in max_indices]} has {max_val} prime divisors')

