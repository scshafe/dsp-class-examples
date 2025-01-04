
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

the "impulse response" (aka s2) is padded with 0's
'''
def create_convolution(s1, s2):
    output = np.zeros(len(s1))
    print(s2)
    for n in range(len(s1)):
        inner_product = 0
        # tmp is the inverted, shifted impulse response h[n-k]
        tmp = np.array(s2[n::-1])
        tmp = np.pad(tmp, [0, len(s1)-len(tmp)])
        inner_product = s1 * tmp


        output[n] = np.sum(inner_product)
    return output



def create_convolution_algorithm_animation(s1, s2):
    conv = create_convolution(s1, s2)
        








sequence_lengths=20

input_unpadded = np.array([0,0,0,2,3,1])
input_sequence = np.pad(input_unpadded, [0, sequence_lengths - len(input_unpadded)])
# print(input_sequence)
assert(len(input_sequence) == sequence_lengths)

# impulse response is exponential decay
alpha = 0.9
impulse_response = np.array([(alpha**x) for x in range(sequence_lengths)])
# print(impulse_response)

conv = create_convolution(input_sequence, impulse_response)

print(impulse_response)

plt.figure(figsize=(9,7))
plt.subplot(311)
plt.stem([i for i in range(sequence_lengths)], input_sequence, basefmt='b')
plt.subplot(312)
plt.stem([i for i in range(sequence_lengths)], input_sequence, basefmt='b')
plt.subplot(313)
plt.stem([i for i in range(sequence_lengths)], conv, basefmt='b')

plt.show()