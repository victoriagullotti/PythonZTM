import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
print('Current directory: ', script_dir)

# Get PYTHONPATH
python_path = sys.path
print('PYTHONPATH before changes: ', python_path)

# Check if the script directory is already in PYTHONPATH
if script_dir not in python_path:
    # Append the script directory to PYTHONPATH
    sys.path.append(script_dir)

# Get new PYTHONPATH
print('PYTHONPATH after changes: ', sys.path)
