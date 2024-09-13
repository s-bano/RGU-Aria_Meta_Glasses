import os

# Path to the shared flag file
flag_file_path = "noise_flag.txt"

# Create the noise flag file
with open(flag_file_path, 'w') as f:
    f.write("apply_noise")

print("Noise will be applied to the video stream.")

# Keep the script running so that the flag persists
try:
    while True:
        pass
except KeyboardInterrupt:
    if os.path.exists(flag_file_path):
        os.remove(flag_file_path)
    print("Noise flag removed.")
