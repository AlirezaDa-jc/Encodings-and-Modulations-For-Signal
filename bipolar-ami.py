import matplotlib.pyplot as plt
import numpy as np

bitstream = '01001000011000010111000001110000011110010010000001011001011000010110110001100100011000010010000001001110011010010110011101101000'



def bipolar_ami_encode(bitstream):
    encoded_signal = []
    last_nonzero = -1
    for bit in bitstream:
        if bit == '0':
            encoded_signal.append(0)
        else:
            last_nonzero *= -1
            encoded_signal.append(last_nonzero)
    return encoded_signal

# انکودینگ و نمایش نمودار
ami_encoded_signal = bipolar_ami_encode(bitstream)
plot_signal(ami_encoded_signal, "Bipolar-AMI Encoding")




