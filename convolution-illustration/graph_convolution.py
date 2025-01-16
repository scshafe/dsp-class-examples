
'''
This file highlights the commutative nature of convolution
'''



import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation


save_gifs = True if input("would you like to save GIFs? [y]") == "y" else False


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

empty = np.array([0 for i in range(sequence_lengths)])






class ConvolutionAnimator:

    def __init__(self, input_sequence, impulse_response):
        self.s1 = input_sequence
        self.s2 = impulse_response
        self.output = np.zeros(sequence_lengths)
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(12, 10))

        self.ax3.set_ylim(0,5)

    def animation_init(self):
        self.ax1.set_title("input sequence")
        self.ax2.set_title("inverted shifted impulse response")
        self.ax2.se
        self.ax3.set_title("output")
        markerline1, stemlines1, baseline1 = self.ax1.stem(x, empty, '-.')
        markerline2, stemlines2, baseline2 = self.ax2.stem(x, empty, '-.')
        markerline3, stemlines3, baseline3 = self.ax3.stem(x, empty, '-.')
        return markerline1, stemlines1, baseline1, markerline2, stemlines2, baseline2, markerline3, stemlines3, baseline3
        # return line1, line2, line3

    '''
    Function to call for each frame of the animation. There are 3 plots:
    1. The input sequence 
    2. The inverse-shifted impulse response (which slides over each iteration)
    3. The output calculated (done incrementally at each step)
    '''
    def create_convolution_algorithm_animation(self, frame_num):
        # print(frame_num)

        self.ax1.cla()
        self.ax2.cla()
        self.ax3.cla()

        self.ax1.set_title("input sequence")
        self.ax2.set_title("inverted shifted impulse response")
        self.ax3.set_title("output")

        self.ax2.set_ylim(0,1.1)
        # self.ax2.set_
        self.ax3.set_ylim(0,6)

        tmp = np.array(self.s2[frame_num::-1])
        tmp = np.pad(tmp, [0, len(self.s1) - len(tmp)])

        inner_product = np.sum(self.s1 * tmp)

        # print(inner_product)
        self.output[frame_num] = inner_product


        # markerline1, stemlines1, baseline1 = ax1.stem(x, self.s1, '-.')
        # markerline2, stemlines2, baseline2 = ax2.stem(x, tmp, '-.')
        # markerline3, stemlines3, baseline3 = ax3.stem(x, output, '-.')

        markerline1, stemlines1, baseline1 = self.ax1.stem(x, self.s1, '-.')
        markerline2, stemlines2, baseline2 = self.ax2.stem(x, tmp, '-.')
        markerline3, stemlines3, baseline3 = self.ax3.stem(x, self.output, '-.')
        # return line1, line2, line3
        return markerline1, stemlines1, markerline2, stemlines2, markerline3, stemlines3



# anim = FuncAnimation(fig, create_convolution_algorithm_animation, #init_func = init, 
#                      frames = 20, interval = 1, blit = True) 


# the regular convolution
ca = ConvolutionAnimator(input_sequence, impulse_response)

anim = FuncAnimation(ca.fig, ca.create_convolution_algorithm_animation, #init_func=ca.animation_init,
                     frames = 20, interval = 200) 
if save_gifs:
    anim.save("convolution.gif")

# ~~~~~ THE COMMUTATIVE CONVOLUTION
commutative_animator = ConvolutionAnimator(impulse_response, input_sequence)

anim = FuncAnimation(commutative_animator.fig, commutative_animator.create_convolution_algorithm_animation, 
                     frames = 20, interval = 200)
if save_gifs:
    anim.save("commutative-convolution.gif")
# plt.show()


