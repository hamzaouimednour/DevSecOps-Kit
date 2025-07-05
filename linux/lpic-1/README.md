# LPIC-1


## 101


### Topic 101: System Architecture

#### 101.1: Hardware configuration

```ini

## BIOS (Basic Input/Output System)
■ firmware init hardware and loads OS 
- support MBR partitioning (smaller drives ≤ 2TB)
- provides configuration options:
    - boot sequence: set correct boot device
    - enabled / disabled devices
    - virtualization feature support

## UEFI (Unified Extensible Firmware Interface)
■ firmware replaces BIOS with a modern GUI
- support GPT and MBR partitioning (drives > 2TB)
- support Secure Boot
- provides faster startup

## Troubleshooting
- access boot? : `F2`, `F12`, `Del`, `Esc`, etc.
- undetected hardware? : defective device or port / a problem within OS

## Terms
[ PCI (Peripheral Component Interconnect) ]
    - standard interface used to connect hardware to motherboard (network, sound cards, GPUs, ...)
[ LKM (Loadable Kernel Module: *.ko) ]
    - drivers / code loaded dynamically for kernel features (support hardware, system)
[ kmod ] : set of tools to manage Linux Kernel modules (insert, remove, list, ...)

# Tips
- use `sudo` for more detailed output.

## Devices Inspection - CLI
| Command        | Description                             | Flags
|----------------|-----------------------------------------|-----------------------------------------------------|
| `lspci`        | List PCI devices                        |-v: verbose, -k: kernel driver, -s: slot, -d: device |
| `lsusb`        | List USB devices                        |-v: verbose, -d: device, -s: bus, -t: tree           |
| `lshw`         | Detailed hardware info (use `sudo`)     |
| `lsblk`        | List block devices                      |
| `fdisk -l`     | List partitions                         |
| `dmidecode`    | BIOS and hardware info                  |
| `dmesg`        | Kernel/hardware boot messages           |
| `hwinfo`       | Comprehensive hardware summary          |

## Kernel Modules - CLI
| Command        | Description                             |
|----------------|-----------------------------------------|
| `lsmod`        | List loaded modules                     |
| `modprobe`     | Load a module                           |
| `rmmod`        | Remove a module                         |
| `modinfo`      | Info about a module                     |
| `depmod`       | Generate dependency info                |

```
    
    - specialized commands or to read specific files inside special filesystems.

        
 

    ## ⚙️ System Resources
    - Understand and manage:
    - IRQs (Interrupt Requests)
    - DMA (Direct Memory Access)
    - I/O Addresses
    - Conflicts can cause hardware issues

    ## 📁 Device Files
    - Located in `/dev`
    - Example: `/dev/sda`, `/dev/ttyUSB0`
    - Managed by `udev` (dynamic device management)

    ## 🧪 Troubleshooting Tips
    - Use `dmesg | grep <device>` to trace device issues
    - Check module dependencies with `lsmod` and `modinfo`
    - Re-seat or test hardware if not detected


#### 101.2: Boot the system

#### 101.3: Change runlevels / boot targets and shutdown or reboot system


### Topic 102: Linux Installation and Package Management


### Topic 103: GNU and Unix Commands


### Topic 104: Devices, Linux Filesystems, Filesystem Hierarchy Standard


## 102
### Topic 105: Shells and Shell Scripting
### Topic 106: User Interfaces and Desktops
### Topic 107: Administrative Tasks
### Topic 108: Essential System Services
### Topic 109: Networking Fundamentals
### Topic 110: Security


## Ref
```
- https://wiki.lpi.org/wiki/LPIC-1_Summary_Version_4.0_To_5.0
- https://www.lpi.org/our-certifications/exam-101-102-objectives/
- https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
- https://tldp.org/guides.html
- 
```