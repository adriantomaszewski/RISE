import scipy
from scipy.io.wavfile import read
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
from pylab import*

# You will need to change the file path as appropriate
file_path = "/Users/adrian/Downloads/cricket_leg.wav" # Mac Desktop
#file_path = "C:/Users/janedoe/Desktop/cricket.wav" # Windows Desktop

# Read audio file
input_data = read(file_path) 
sample_rate = input_data[0]
audio = input_data[1] # mono file
if ndim(audio)>1:
    audio = audio[:,0]
samples = len(audio)
seconds = samples / sample_rate

# Normalize amplitude (from -1 to +1)
denom = np.max(np.abs(audio))
data = audio/denom

# Display audio file information
print("Number of samples: " + str(samples))
print("Sample rate (samples per second): " + str(sample_rate))
print("Number of seconds: " + str(seconds))

# Plot audio
plt.plot(data)
plt.ylabel("Amplitude (normalized)")
plt.xlabel("Time (samples)")
plt.show()

# Find spikes
# You may need to tweak the minimum height (amplitude) required for a spike.
# If you are picking up too many spikes, decrease the min_height (has to be more than 0).
# If you are not picking up enough spikes, increase the min_height (can't be greater than 1).
# Make sure you use the same min_height for each trial comparison so you are comparing apples-to-apples!
min_height = .67 # a spike has to have an amplitude >= 0.67

# You may need to tweak the minimum distance (in samples) between spikes.
# If you are picking up too many spikes, increase the min_distance.
# If you are not picking up enough spikes, decrease the min_distance (has to be at least 1).
# Make sure you use the same min_distance for each trial comparison so you are comparing apples-to-apples!
min_distance = 100 # spikes need to be at least 100 samples apart

# You may need to tweak the minimum width (in samples) of a spike.
# If you are picking up too many spikes, increase the min_width.
# If you are not picking up enough spikes, decrease the min_width (has to be at least 1)
# Make sure you use the same min_width for each trial comparison so you are comparing apples-to-apples!
min_width = 1 # spikes need to be at least 1 sample wide.

# Plot spikes
peaks, other = find_peaks(data, height=min_height, threshold=0, distance=min_distance, width=min_width)
plt.plot(data)
plt.plot(peaks, data[peaks], "x")
plt.show()

# Root mean square
rms = sqrt(mean(np.square(data)))
print("Root mean square: " + str(rms))

# number of spikes
spike_count = len(peaks)
print("Number of spikes: " + str(spike_count))

# number of spikes per second
spike_rate = len(peaks) / (len(data) / sample_rate)
print("Spike rate per second: " + str(spike_rate))
