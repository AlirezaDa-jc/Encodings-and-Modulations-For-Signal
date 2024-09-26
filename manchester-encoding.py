import matplotlib.pyplot as plt
import numpy as np

bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'

# تابع پیاده سازی Manchester encoding
def manchester_encode(bitstream):
    encoded = []
    for bit in bitstream:
        if bit == '1':
            encoded.extend([1, -1])
        else:
            encoded.extend([-1, 1])
    return encoded

# نمودار Manchester encoding
def plot_signal(signal, title):
    plt.figure(figsize=(10,2))
    t = range(len(signal))
    plt.step(t, signal, where='post')
    plt.ylim(-1.5, 1.5)
    plt.title(title)
    plt.grid(True)
    plt.show()

# انکودینگ و نمایش نمودار
manchester_encoded_signal = manchester_encode(bitstream)
plot_signal(manchester_encoded_signal, "Manchester Encoding")


