#!/bin/bash

date

echo

lscpu | grep -i "model name"
lscpu | grep -i "cpu max mhz"
lscpu | grep -i "core(s)"
lscpu | grep -i "thread(s)"

echo

lspci | grep -i vga

echo

ip a | sed 's/^[[:space:]]*//' | grep inet | grep -v :

