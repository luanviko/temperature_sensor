import matplotlib.pyplot as plt 
import numpy as np, sys

def moving_average(data, n_samples):
    # Apply average on latest n_samples.
    # input:  data, n_samples
    # output: array with averaged samples
    average = []
    for i in range(0, len(data)):
        A = i-n_samples 
        B = i+n_samples
        if A < 0: A = 0
        if B > len(data): B = n_samples
        average.append(np.average(data[A:B]))
    return average

# Load data
file_path = int(sys.argv[1])
room, probe = np.loadtxt(file_path, usecols=(1,2), delimiter=",", skiprows=1, unpack=True)
    
# Plot original data
x = np.arange(0, len(room))
plt.plot(x, room, label="Room", color="orange", alpha=0.5)
plt.plot(x, probe, label="MPPC Board", color="blue", alpha=0.5)
plt.xlabel("Sample")
plt.ylabel("Temperature (C)")
plt.legend()

# Plot averaged data
average_probe = moving_average(probe, 60)
average_room  = moving_average(room, 60)
plt.plot(np.arange(0, len(average_probe)), average_probe, color="blue", label="Average MPPC Board")
plt.plot(np.arange(0, len(average_room)), average_room, color="orange", label="Average MPPC Board")

# Save and show plot
plt.savefig(file_path.replace(".csv", ".pdf"))
plt.show()

