from functions import *
import matplotlib as plt
from plotter import *


data = load_openpose("arms_output")

def subplot_3(joint, data):
    angles = [angle_from_frame(joint, frame) for frame in data]
    # plots the x and y coordinates of the pixels in blue cirlces
    fig, axs = plt.subplots(1, 3)
    axs[0].plot(angles)
    axs[0].set_title("Graph of Angle of " + JOINTS[joint] + " Over Time")
    axs[0].set_xlabel("Frame")
    axs[0].set_ylabel("Angle of " + JOINTS[joint] + " (degrees)")
    plt.show()

subplot_3(L_ELBOW, data)

