#!/bin/bash

id="Portable"

# Perdue Hall 101
if ip a | grep -i "brd 131.118.40.255" &> /dev/null; then
  id="PH101"

# Second floor on TETC and TETC110B
elif ip a | grep -i "brd 131.118.37.255" &> /dev/null; then
  id="TETC110B"

# TETC110A
elif ip a | grep -i "brd 10.249.14.255" &> /dev/null; then
  id="TETC110A"

# TETC213G
elif ip a | grep -i "brd 131.118.200.255" &> /dev/null; then
  id="TETC213G"

fi

# Update config file with new ID only if a value for id was set.
if [ ! -z "$id" ]; then
  sed "s/Portable/$id/" ~/xmrig/config.json
fi

echo "ID set to: $id"
