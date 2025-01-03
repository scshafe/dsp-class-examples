
'''
This file highlights the commutative nature of convolution
'''



import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation


def conv_index(sequence, n, k):
    # return s[n-k] or 0 if out of index
    if n-k < 0 or n-k >= len(sequence):
        return 0
    return sequence[n-k]

'''
This function creates the convolution:

y[n] = \sum_k x[k] * h[n-k] 

x corresponds to s1
h corresponds to s2

output sequence will be length of s1

the "impulse response" (aka s2) is padded with 0's
'''
def create_convolution(s1, s2):
    output = np.zeroes(len(s1))
    for n in range(len(s1)):
        inner_product = 0
        # tmp is the inverted, shifted impulse response h[n-k]
        for k in range(len(s1)):
            inner_product += s1[k] * conv_index(s2, n, k)
        output[n] = inner_product
    return output


def create_convolution_algorithm_animation(s1, s2):
    conv = create_convolution(s1, s2)
        








sequence_lengths=10

# input sequence length 10
input_sequence = np.array([0,0,0,3,5,0,2,0,0,0])
assert(len(input_sequence) == sequence_lengths)

# impulse response is exponential decay
alpha = 0.9
impulse_response = np.array(alpha**x for x in range(sequence_lengths))


print(impulse_response)

plt.figure(figsize=(9,7))
plt.subplot(311)
plt.stem([i for i in range(10)], input_sequence, basefmt='b')
plt.subplot(312)
plt.stem([i for i in range(10)], input_sequence, basefmt='b')
plt.subplot(313)
plt.stem([i for i in range(10)], input_sequence, basefmt='b')

plt.show()