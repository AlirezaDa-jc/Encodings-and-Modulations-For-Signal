import matplotlib.pyplot as plt
import numpy as np

# پیکربندی‌های فرکانس و زمان برای مدولاسیون
bit_rate = 1000  # تعداد نقاط نمونه‌برداری در ثانیه برای هر بیت
f1 = 10  # فرکانس برای بیت 1
f0 = 5  # فرکانس برای بیت 0
duration_of_bit = 0.1  # مدت زمان به ثانیه برای هر بیت

# نمایش دنباله باینری به عنوان یک بیت‌استریم
bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'

# تابع برای تولید نمودار مدولاسیون FSK
def plot_fsk(bitstream, bit_rate, f1, f0, duration_of_bit):
    t = np.linspace(0, duration_of_bit, int(bit_rate * duration_of_bit), False)
    modulated_signal = np.array([], dtype=np.float32)

    for bit in bitstream:
        if bit == '1':
            waveform = np.sin(2 * np.pi * f1 * t)
        else:
            waveform = np.sin(2 * np.pi * f0 * t)
        modulated_signal = np.concatenate((modulated_signal, waveform))

    plt.figure(figsize=(15, 5))
    plt.plot(modulated_signal)
    plt.title('FSK Modulated Signal of "Happy Yalda Night"')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.show()

# نمایش نمودار مدولاسیون FSK
plot_fsk(bitstream, bit_rate, f1, f0, duration_of_bit)




