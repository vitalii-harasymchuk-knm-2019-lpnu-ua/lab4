import math
from math import *

print('Please enter variable:')
varZ = input('z = ')
varZ = int(varZ)

if varZ >= 1:
    x = math.sqrt(pow(varZ,3))
else: 
    x = varZ

result = -math.pi * x + pow(cos(pow(x,3)),2) + pow(cos(pow(x,2)),3)
 
print('x = ', x)
print('y = ', round(result, 2))
input('')
