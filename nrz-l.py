import matplotlib.pyplot as plt
import numpy as np

bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'

# تابع پیاده سازی NRZ-L
def nrz_l_encode(bitstream):
    return [1 if bit == '1' else -1 for bit in bitstream]

# نمودار NRZ-L
def plot_signal(signal, title):
    plt.figure(figsize=(10,2))
    plt.plot(signal, drawstyle='steps-pre')
    plt.title(title)
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.show()

encoded_signal = nrz_l_encode(bitstream)
plot_signal(encoded_signal, "NRZ-L Encoding")
