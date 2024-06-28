import os

counter_file = './Counters/counter.txt'

# Read the current counter value
if os.path.exists(counter_file):
    with open(counter_file, 'r') as file:
        counter = int(file.read().strip())
else:
    counter = 0

# Increment the counter
counter += 1

# Write the new counter value back to the file
with open(counter_file, 'w') as file:
    file.write(str(counter))

print(f"::set-output name=counter::{counter}")