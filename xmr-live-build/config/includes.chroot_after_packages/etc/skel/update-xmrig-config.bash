#!/bin/bash

# Get the number of threads (CPU cores)
threads=$(lscpu | grep "^CPU(s):" | awk '{print $2}')

# Generate the array of thread counts (counting from 0)
rx_array=$(seq -s', ' 0 $((threads - 1)))

# Create the updated rx array in JSON format, without extra leading spaces
updated_rx="\"rx\": [${rx_array}]"

# Update the configuration file
config_file="config.json"

# Use sed to update the "rx" array under the "cpu" section, making a backup 
# file before editing.
sed -i.bak "s/\"rx\": \[.*\]/$updated_rx/" ~/xmrig/"$config_file"

# Display the array before exiting.
echo "Updated rx array to: [$rx_array]"

