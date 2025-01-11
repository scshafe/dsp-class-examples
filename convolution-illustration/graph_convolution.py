
'''
This file highlights the commutative nature of convolution
'''



import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation


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



sequence_lengths=20
input_unpadded = np.array([1,2,3])
input_sequence = np.pad(input_unpadded, [0, sequence_lengths - len(input_unpadded)])

alpha = 0.9
impulse_response = np.array([(alpha**x) for x in range(sequence_lengths)])

x = np.array([i for i in range(sequence_lengths)])

output = np.zeros(sequence_lengths)


# Create figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))


# Line objects for each plot
ax1.stem(x, input_sequence)
ax2.stem(x, impulse_response)
ax3.stem(x, output)

line1 = ax1.stem(x, input_sequence)
line2 = ax2.stem(x, impulse_response)
line3 = ax3.stem(x, output)

# Animation update function
# def animate(i):
#     y1 = np.sin(x + i / 10)
#     y2 = np.cos(x + i / 10)
#     y3 = np.tan(x + i / 10)

#     line1.set_ydata(y1)
#     line2.set_ydata(y2)
#     line3.set_ydata(y3)

#     return line1, line2, line3


def init():
    return line1, line2, line3

'''
Function to call for each frame of the animation. There are 3 plots:
1. The input sequence 
2. The inverse-shifted impulse response (which slides over each iteration)
3. The output calculated (done incrementally at each step)
'''
def create_convolution_algorithm_animation(frame_num):
    print(frame_num)

    tmp = np.array(impulse_response[frame_num::-1])
    tmp = np.pad(tmp, [0, len(input_sequence) - len(tmp)])

    inner_product = np.sum(input_sequence * tmp)

    print(inner_product)
    output[frame_num] = inner_product

    line1.set_data(x, input_sequence)
    line2.set_data(x, tmp)
    line3.set_data(x, output)

    return line1, line2, line3
    # line2.set_ydata(tmp)
    # line3.set_ydata(output)


# anim = FuncAnimation(fig, create_convolution_algorithm_animation, #init_func = init, 
#                      frames = 20, interval = 1, blit = True) 

anim = FuncAnimation(fig, create_convolution_algorithm_animation,
                     frames = 20, interval = 1, blit = True) 
