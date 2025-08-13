import sys
import soundfile as sf
import pyloudnorm as pyln
import numpy as np

# Check for command line argument
if len(sys.argv) < 2:
    print("Usage: python measure_lkfs.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

# Read audio data
try:
    data, rate = sf.read(file_path)
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# ensure data is float
if data.dtype != np.float32 and data.dtype != np.float64:
    data = data.astype(np.float32) / np.iinfo(data.dtype).max


# Create a meter
meter = pyln.Meter(rate) # create BS.1770 meter

# Measure loudness
loudness = meter.integrated_loudness(data) # measure loudness

print(f"Loudness: {loudness:.2f} LKFS")
