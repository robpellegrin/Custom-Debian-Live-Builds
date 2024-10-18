# Custom Debian Live Environment for OpenMPI

This repository contains the configuration files and scripts needed to build a minimal Debian live environment tailored for use with OpenMPI. The goal is to create a portable image that can be booted from a USB flash drive, allowing for quick addition of computers to your computing cluster.

## Features

- Lightweight Debian-based live environment. Only the essentials are included.
- Easy to build using `live-build`
- Pre-configured with OpenMPI for distributed computing
- Easily bootable from USB flash drives
- Simple setup for adding nodes to your cluster
- No changes or modifications to the existing OS alrady on the host computer.

## Requirements

- A machine running Debian or a Debian-based system to build the live image
- `live-build` package installed (`sudo apt install live-build`)
- USB flash drive (at least 2GB recommended)

## Included Packages

The following packages are included in the live environment:
- libopenmpi-dev
- nfs-common
- build-essential
- openssh-server
- iperf
- lm-sensors
- parallel ([GNU Parallel](https://www.gnu.org/software/parallel/))
- sshpass
- htop
- Standard system utilities (e.g., `ls`, `cp`, etc.)

Note that there is no desktop environment!

## Getting Started

### Building the Live Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/robpellegrin/live-builds/tree/main/COSC420-live-build
   cd COSC420-live-build

2. **Install the dependencies:**

   ```bash
   sudo apt install live-build
   ```

3. **Build the image:**

   ```bash
   lb config && sudo lb build
   ```
   After several minutes, if all goes well, this command will create a bootable ISO file in the current directory.

### Writing the image to a USB drive

1. **Find the name of your flash drive:**

   ```bash
   lsblk
   ```

2. **Write the image to the USB drive:**

   ```bash
   sudo dd if=/path/to/iso/ of=/dev/sdX bs=1M status=progress
   ```
   Replace `sdX` with the name of your flash drive, as shown in the previous step.

### Booting from a USB Flash Drive

1. Insert the USB drive into the target computer.
2. Boot the computer and enter the BIOS/UEFI settings.
3. Select the USB drive as the boot device.
4. The system will boot into the custom Debian live environment with OpenMPI pre-installed.

### Customization
This image is highly customizable, and can be modified to suit your needs. For more information,
check out the [live-build](https://live-team.pages.debian.net/live-manual/html/live-manual/index.en.html) manual.


## Acknowledgments

- [live-build](https://live-team.pages.debian.net/live-manual/) manual
- [Debian Live Environment](https://wiki.debian.org/LiveCD) documentation
- [OpenMPI](https://www.open-mpi.org) documentation
- [COSC420](https://github.com/robpellegrin/COSC420) course materials