''' 
    Measures of spread

    These functions calculate a measure of how much the population or 
    sample tends to deviate from the typical or average values.
'''
from statistics import (pstdev, pvariance, stdev, variance)
from decimal import Decimal as D
from fractions import Fraction as F
# Sample data
sample = [1, 7, 3, 9, 7]

# pstdev() Population standard deviation of data.
print(pstdev(sample)) #2.9393...

# pvariance() Population variance of data.
print(pvariance(sample)) #8.64

# stdev() Sample standard deviation of data.
print(stdev(sample)) #3.2863...

# variance() Sample variance of data.
print(variance(sample)) #10.7999...

#Decimals and fractions are also supported
decimal_sample = [D("3.33333"), D("2.47"), D("6.36")]
print(pvariance(decimal_sample)) #2.7820...

fraction_sample = [F(2, 3), F(1, 4), F(3, 4)]
print(pvariance(fraction_sample)) # F(31, 648)
