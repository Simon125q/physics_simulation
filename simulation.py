import math
import matplotlib.pyplot as plt
A = 1.0
H = 150.0
L = 150.0
frequency = 600.0
omega = frequency * 2 * math.pi
time = 60.0
time_period = 0.0001
current_time = 0.0
x_axis_data = []
y_axis_data = []
wave_length = 340.0 /frequency
k = 2 * math.pi / wave_length
y = -3000.0


while(current_time<time):
    x1 = math.sqrt(pow(L/2-y, 2) + pow(H, 2))
    x2 = math.sqrt(pow(L/2+y, 2) + pow(H, 2))
    a1 = 1.0/x1
    a2 = 1.0/x2
    z = a1*math.cos(omega*current_time - k*x1) + a2*math.cos(omega*current_time - k*x2)
    x_axis_data.append(current_time)
    y_axis_data.append(z)
    print(z)
    print(current_time)
    y += 0.01
    current_time += time_period

plt.scatter(x_axis_data, y_axis_data, marker=',')

plt.xlabel('time')
plt.ylabel('y axis')

plt.title('Graph')

plt.show()

