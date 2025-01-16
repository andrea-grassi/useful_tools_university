"""
    Andrea Grassi January 2025
    This code simulates and visualizes the output response of an operational amplifier.
    It calculates the theoretical output Vout as a function of the input Vin, considering a gain A 
    and a reference voltage Vr. Saturation is then applied to limit the output within the supply 
    voltage limits Vcc+ and Vcc-. The plot shows both the theoretical and saturated responses.
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
R_ref = 10e3         # R reference
R_in = 2e3           # R input
A = -R_ref/R_in      # Gain
Vr = 0               # Reference voltage
Vcc_plus = 5         # Upper limit
Vcc_minus = 0        # Lower limit
V_in_sig_plus = 1    # Upper limit input signal
V_in_sig_minus = - 1 # Lower limit inpur signal

# Input range
Vin = np.linspace(V_in_sig_minus, V_in_sig_plus, 500)

# Vout = Vr - A * (Vin - Vr)
Vout_corrected = Vr + A * (Vin - Vr)

# Apply saturation limits
Vout_corrected_saturated = np.clip(Vout_corrected, Vcc_minus, Vcc_plus)

# Plot
plt.figure(num="Operational Amplifier Output range", figsize=(8, 5))
plt.plot(Vin, Vout_corrected, label="Theoretical Output ", linestyle="--", color="blue")
plt.plot(Vin, Vout_corrected_saturated, label="Saturated Output", color="red")
plt.axhline(Vcc_plus, color="gray", linestyle=":", label=f"Vcc+ = {Vcc_plus}V")
plt.axhline(Vcc_minus, color="gray", linestyle=":", label=f"Vcc- = {Vcc_minus}V")
plt.axvline(0, color="black", linestyle=":")
plt.axhline(0, color="black", linestyle=":")

# Dashed lines at saturation values 
plt.axhline(np.max(Vout_corrected_saturated), color="green", linestyle="--", label="Saturation upper bound")
plt.axhline(np.min(Vout_corrected_saturated), color="orange", linestyle="--", label="Saturation lower bound")

# Add custom labels for the gain and saturation levels in the legend
plt.legend(
    loc='upper left', 
    bbox_to_anchor=(0.5, -0.2),  # Place the legend below the plot at the left
    labels=[
        "Theoretical Output", 
        "Saturated Output", 
        f"Vcc+ = {Vcc_plus}V", 
        f"Vcc- = {Vcc_minus}V", 
        f"Saturation upper bound = {np.max(Vout_corrected_saturated):.2f}V", 
        f"Saturation lower bound = {np.min(Vout_corrected_saturated):.2f}V", 
        f"Gain A = {A:.2f}"
    ]
)

plt.title("Output range of an Operational Amplifier")
plt.xlabel("Input Voltage (Vin) [V]")
plt.ylabel("Output Voltage (Vout) [V]")
plt.grid()

plt.tight_layout(pad=1)

# Show the plot
plt.show()