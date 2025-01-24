#!/bin/bash

while ! ping -c 1 google.com &> /dev/null; do
    sleep 1
done

sudo ntpdate pool.ntp.org
