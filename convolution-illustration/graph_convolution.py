
'''
This file highlights the commutative nature of convolution
'''



import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation


'''
This function creates the convolution:

y[n] = \sum_k x[k] * h[n-k] 

x corresponds to s1
h corresponds to s2

output sequence will be length of s1
'''
def create_convolution(s1, s2):
    output = np.zeroes(len(s1))







sequence_lengths=10

# input sequence length 10
input_sequence = np.array([0,0,0,3,5,0,2,0,0,0])
assert(len(input_sequence) == sequence_lengths)

# impulse response is exponential decay
alpha = 0.9
impulse_response = np.array(alpha**x for x in range(sequence_lengths))


print(impulse_response)
