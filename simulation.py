import math
import matplotlib.pyplot as plt

height = 0.5
distance = 1.3
frequency = 2000.0
is_another_source = False
angular_frequency = frequency * 2 * math.pi
simulation_time = 20
data_frequency = 10000
time_period = 1 / data_frequency
current_time = 0.0
x_axis_data = []
y_axis_data = []
wave_length = 340.0 / frequency
wave_number = 2 * math.pi / wave_length
initial_position1 = -3.0
initial_position2 = -3.5
speed = 0.4

source2_amplitude = 0

decision = input("Do you want to simulate 2 sources? Y/N \n")
if decision.upper() == "Y":
    is_another_source = True

decision = input("Do you want to provide your data? Y/N \n")
if decision.upper() == "Y":
    simulation_time = float(input("Simulated time (seconds): \n"))
    data_frequency = float(input("How many measurements per second: \n"))
    time_period = 1 / data_frequency
    frequency = float(input("Sound Frequency (Hz): \n"))
    initial_position1 = float(input("Starting position ('-' to the right, 0 exactly between microphones) (meters): \n"))
    speed = float(input("Speed of movement of the object (m/s): \n"))
    if is_another_source:
        initial_position2 = float(
            input("Starting position of the 2nd source ('-' to the right, 0 exactly between microphones) (meters): \n"))

while current_time < simulation_time:
    distance1 = math.sqrt(pow(distance / 2 - initial_position1, 2) + pow(height, 2))
    distance2 = math.sqrt(pow(distance / 2 + initial_position1, 2) + pow(height, 2))
    amplitude1 = 1.0 / distance1
    amplitude2 = 1.0 / distance2
    sound_wave1 = amplitude1 * math.cos(angular_frequency * current_time - wave_number * distance1)
    sound_wave2 = amplitude2 * math.cos(angular_frequency * current_time - wave_number * distance2)
    sound_intensity = sound_wave1 + sound_wave2

    if is_another_source:
        distance3 = math.sqrt(pow(distance / 2 - initial_position2, 2) + pow(height, 2))
        distance4 = math.sqrt(pow(distance / 2 + initial_position2, 2) + pow(height, 2))
        amplitude3 = 1.0 / distance3
        amplitude4 = 1.0 / distance4
        sound_wave3 = amplitude3 * math.cos(angular_frequency * current_time - wave_number * distance3)
        sound_wave4 = amplitude4 * math.cos(angular_frequency * current_time - wave_number * distance4)
        source2_amplitude = sound_wave3 + sound_wave4

    sound_intensity += source2_amplitude
    sound_intensity = pow(sound_intensity, 2)

    x_axis_data.append(current_time)
    y_axis_data.append(sound_intensity)

    initial_position1 += (speed / data_frequency)
    initial_position2 += (speed / data_frequency)
    current_time += time_period

plt.plot(x_axis_data, y_axis_data, marker=',')

plt.xlabel('Time (s)')
plt.ylabel('Sound Intensity')
plt.title('Graph')

plt.show()
