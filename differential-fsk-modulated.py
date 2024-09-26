import numpy as np
import matplotlib.pyplot as plt

# افزایش نرخ نمونه‌برداری و فرکانس‌ها برای دقت بیشتر در مثال
bit_rate = 100  # تعداد نقاط نمونه‌برداری در ثانیه برای هر بیت
f1 = 5  # فرکانس برای بیت 1
f0 = 1  # فرکانس برای بیت 0
duration_of_bit = 1  # مدت زمان به ثانیه برای هر بیت

# دنباله باینری
bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'

def differential_encoder(bitstream):
    last_bit = '0'
    encoded_stream = ''
    for bit in bitstream:
        encoded_bit = str(int(bit) ^ int(last_bit))  # XOR با بیت قبلی
        encoded_stream += encoded_bit
        last_bit = encoded_bit
    return encoded_stream

def generate_fsk_signal(bitstream, bit_rate, f1, f0, duration_of_bit):
    t = np.linspace(0, duration_of_bit, int(bit_rate*duration_of_bit), False)
    modulated_signal = np.array([], dtype=np.float32)

    for bit in differential_encoder(bitstream):
        if bit == '1':
            waveform = np.sin(2 * np.pi * f1 * t)
        else:
            waveform = np.sin(2 * np.pi * f0 * t)
        modulated_signal = np.concatenate((modulated_signal, waveform))

    return modulated_signal

modulated_signal = generate_fsk_signal(bitstream, bit_rate, f1, f0, duration_of_bit)

plt.figure(figsize=(15, 5))
plt.plot(modulated_signal[:bit_rate*10])  # نمایش 10 بیت اول
plt.title('Differential FSK Modulated Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()