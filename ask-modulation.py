import matplotlib.pyplot as plt
import numpy as np

bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'

# تابع پیاده سازی ASK modulation
def ask_modulate(bitstream, carrier_frequency, sampling_rate, bitrate):
    bit_time = 1/bitrate
    time = np.linspace(0, len(bitstream)*bit_time, num=int(sampling_rate*bit_time)*len(bitstream))
    signal = np.zeros_like(time)
    for i, bit in enumerate(bitstream):
        start = int(i*sampling_rate*bit_time)
        end = start + int(sampling_rate*bit_time)
        if bit == '1':
            signal[start:end] = np.cos(2 * np.pi * carrier_frequency * time[start:end])
    return time, signal

# نمایش نمودار ASK
def plot_modulated_signal(time, signal, title):
    plt.figure(figsize=(10,2))
    plt.plot(time, signal)
    plt.title(title)
    plt.grid(True)
    plt.show()

# پارامترهای modulation
carrier_frequency = 2  # فرکانس حامل
sampling_rate = 100   # نرخ نمونه برداری
bitrate = 1           # نرخ بیت

# modulation
t, modulated_signal = ask_modulate(bitstream, carrier_frequency, sampling_rate, bitrate)
plot_modulated_signal(t, modulated_signal, "ASK Modulation")


