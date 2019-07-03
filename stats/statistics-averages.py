''' 
    Averages and measures of central location
    
    These functions calculate an average or typical value from a population or sample.
'''
from statistics import (mean, harmonic_mean, median, 
    median_low, median_high, median_grouped, mode)


# Sample data
sample = [1, 7, 3, 9, 7]

# mean() Arithmetic mean (“average”) of data.
print(mean(sample)) #5.4

# harmonic_mean() Harmonic mean of data or subcontrary mean: the reciprocal of the arithmetic mean() of the reciprocals of the data
print(harmonic_mean(sample)) #2.8899...

# median() Median (middle value) of data.
print(median(sample)) #7

# median_low() Low median of data.
print(median_low(sample)) #7

# median_high() High median of data.
print(median_high(sample)) #7

# median_grouped() Median, or 50th percentile, of grouped data.
print(median_grouped(sample)) #6.75

# mode() Mode (most common value) of discrete data.
print(mode(sample)) #7
