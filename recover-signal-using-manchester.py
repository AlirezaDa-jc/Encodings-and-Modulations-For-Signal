import matplotlib.pyplot as plt
import numpy as np

bitstream = "01001000 01100001 01110000 01110000 01111001 00100000 01011001 01100001 01101100 01100100 01100001 00100000 01101110 01101001 01100111 01101000 01110100" # برای تست


# مرحله فرضی برای تولید سیگنال Manchester
def simple_manchester_encode(bitstream):
    encoded = []
    for bit in bitstream:
        encoded.append(-1 if bit == '0' else 1)
    return encoded
    
tx_signal = simple_manchester_encode(bitstream)  # فرستنده سیگنال

# مرحله فرضی کلاک ریکاوری (PLL)
def fake_pll(tx_signal):
    # در اینجا فقط برای نمایش از سیگنال فرستنده استفاده می‌کنیم
    rx_signal = np.array(tx_signal) * np.exp(1j * np.pi/2)  # اعمال یک انحراف فاز فرضی
    return np.angle(rx_signal)  # بازگشت فاز سیگنال

# سیگنال دریافتی (با انحراف فاز)
rx_signal = fake_pll(tx_signal)

# نمودار سازی
plt.figure(figsize=(15, 5))

# نمودار سیگنال فرستنده
plt.subplot(2, 1, 1)
plt.step(range(len(tx_signal)), tx_signal, where='mid', linewidth=2)
plt.title('Manchester Encoded Signal (TX - Transmitter)')
plt.ylim(-1.5, 1.5)
plt.ylabel('Amplitude')
plt.grid(True)

# نمودار سیگنال دریافتی (بعد از PLL)
plt.subplot(2, 1, 2)
plt.plot(rx_signal, linestyle='-', marker='o', color='red')
plt.title('Recovered Signal Phase after PLL (RX - Receiver)')
plt.ylabel('Phase (Radians)')
plt.xlabel('Bit intervals')
plt.grid(True)

plt.tight_layout()
plt.show()



