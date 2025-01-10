
'''
This file highlights the commutative nature of convolution
'''



import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation



input_sequence = np.array([])
impulse_response = np.array([])

output = np.zeros(len(input_sequence))

# tmp is the time-inverted and shifted impulse response at each step of the convolution
tmp = np.zeros(len(input_sequence))


def animate_convolution_step(i):
    return




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


'''
function to call for each frame of the animation. There are 3 plots:
1. The input sequence 
2. The inverse-shifted impulse response (which slides over each iteration)
3. The output calculated (done incrementally at each step)
'''
def create_convolution_algorithm_animation(s1, s2):
    sequence_lengths = len(s1)
    conv = create_convolution(s1, s2)

    plt.figure(figsize=(9,7))
    plt.subplot(311)

    plt.stem([i for i in range(sequence_lengths)], s1, basefmt='b')
    plt.subplot(312)
    plt.stem([i for i in range(sequence_lengths)], s2, basefmt='b')
    plt.subplot(313)
    plt.stem([i for i in range(sequence_lengths)], conv, basefmt='b')

    plt.show()
        








sequence_lengths=20

input_unpadded = np.array([0,0,0,2,3,1])
input_sequence = np.pad(input_unpadded, [0, sequence_lengths - len(input_unpadded)])
# print(input_sequence)
assert(len(input_sequence) == sequence_lengths)

# impulse response is exponential decay
alpha = 0.9
impulse_response = np.array([(alpha**x) for x in range(sequence_lengths)])


create_convolution_algorithm_animation(input_sequence, impulse_response)


from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation  
   
# initializing a figure in  
# which the graph will be plotted 
fig = plt.figure()  
   
# marking the x-axis and y-axis 
axis = plt.axes(xlim =(0, 4),  
                ylim =(-2, 2))  
  
# initializing a line variable 
line, = axis.plot([], [], lw = 3)  
   
# data which the line will  
# contain (x, y) 
def init():  
    line.set_data([], []) 
    return line, 
   
def animate(i): 
    x = np.linspace(0, 4, 1000) 
   
    # plots a sine graph 
    y = np.sin(2 * np.pi * (x - 0.01 * i)) 
    line.set_data(x, y) 
      
    return line, 
   
anim = FuncAnimation(fig, animate, init_func = init, 
                     frames = 200, interval = 20, blit = True) 
  
   
anim.save('continuousSineWave.mp4',  
          writer = 'ffmpeg', fps = 30) 