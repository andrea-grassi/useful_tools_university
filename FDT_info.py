import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# FDT G(s)
num = [10, 10, 10]  # num
den = [1, 0, -1]    # den
system = signal.TransferFunction(num, den)

# Bode
def plot_bode(system):
    w, mag, phase = signal.bode(system)

    plt.figure("Bode", figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag, label="Module")
    plt.title("Bode")
    plt.ylabel("Module [dB]")
    plt.grid(which='both', linestyle='--', linewidth=0.5)

    # Phase
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase, label="Phase", color='orange')
    plt.ylabel("Phase [°]")
    plt.xlabel("Frequency [rad/s]")
    plt.grid(which='both', linestyle='--', linewidth=0.5)

    plt.tight_layout()

# Nyquist
def plot_nyquist(system):
    w, h = signal.freqresp(system)

    plt.figure("Nyquist", figsize=(6, 6))
    plt.plot(h.real, h.imag, label="Nyquist", color="purple")
    plt.plot(h.real, -h.imag, linestyle='--', color="purple", alpha=0.5)  # Parte speculare
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title("Nyquist")
    plt.xlabel("Re(G(jω))")
    plt.ylabel("Im(G(jω))")
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.axis("equal")

# Rlocus
def plot_root_locus(system):
    poles = np.roots(den)
    zeros = np.roots(num)

    plt.figure("Roots", figsize=(6, 6))
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label="Poli")
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label="Zeri")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title("Roots")
    plt.xlabel("Re(s)")
    plt.ylabel("Im(s)")
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.axis("equal")

# Functions call
plot_bode(system)
plot_nyquist(system)
plot_root_locus(system)

# Show figures
plt.show()
