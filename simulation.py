import math
import matplotlib.pyplot as plt
H = 0.5
L = 1.3
frequency = 2000.0
another_source = False
omega = frequency * 2 * math.pi
time = 20
data_freq = 10000
time_period = 1 / data_freq
current_time = 0.0
x_axis_data = []
y_axis_data = []
wave_length = 340.0 /frequency
k = 2 * math.pi / wave_length
y = -3.0
y2 = -3.5
speed = 0.4

z2=0

deciton = input("Do you want to simulate 2 sources? Y/N \n")
if(deciton.upper() == "Y"):
    another_source = True
deciton = input("Do you want to provide your data? Y/N \n")
if(deciton.upper() == "Y"):
    time = float(input("Simulated time (secounds): \n"))
    data_freq = float(input("How many measurements for 1 secound: \n"))
    time_period = 1/data_freq
    frequency = float(input("Sound Frequency (Hz): \n"))
    y = float(input("starting positon ('-' to the right, 0 excatly between microphones) (meters): \n"))
    speed = float(input("speed of movement of the object (m/s): \n"))
    if another_source:
        y = float(input("starting positon of 2nd source ('-' to the right, 0 excatly between microphones) (meters): \n"))


while(current_time<time):
    x1 = math.sqrt(pow(L/2-y, 2) + pow(H, 2))
    x2 = math.sqrt(pow(L/2+y, 2) + pow(H, 2))
    a1 = 1.0/x1
    a2 = 1.0/x2
    z = a1*math.cos(omega*current_time - k*x1) + a2*math.cos(omega*current_time - k*x2)
    if another_source:
        x12 = math.sqrt(pow(L/2-y2, 2) + pow(H, 2))
        x22 = math.sqrt(pow(L/2+y2, 2) + pow(H, 2))
        a12 = 1.0/x12
        a22 = 1.0/x22
        z2 = a12*math.cos(omega*current_time - k*x12) + a22*math.cos(omega*current_time - k*x22)
    z = z+z2
    z = pow(z, 2)
    x_axis_data.append(current_time)
    y_axis_data.append(z)
    #print(z)
    #print(current_time)
    y += (speed / data_freq)
    y2 +=(speed / data_freq)
    current_time += time_period

plt.plot(x_axis_data, y_axis_data, marker=',')


plt.xlabel('time (s)')
plt.ylabel('Sound Intensity')

plt.title('Graph')

plt.show()

