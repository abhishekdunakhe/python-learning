import os

# Static directory path
directory = "/Resqroom-admin"

# Check if directory exists
if os.path.exists(directory):
    print(f"Contents of directory: {directory}")
    for item in os.listdir(directory):
        print(item)
else:
    print("Directory does not exist.")
