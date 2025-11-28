# PiTrezor ILI9341 Display Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Trezor Compatible](https://img.shields.io/badge/Trezor-Compatible-blue.svg)](https://trezor.io/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Zero%20W-red.svg)](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)

A complete solution for integrating ILI9341 color SPI displays with PiTrezor hardware wallets. This project combines modern PiTrezor firmware with proven display drivers using an innovative "Reverse Firmware Transplant" approach.

## 🎯 What This Project Solves

- **Display Compatibility**: Enables ILI9341, ILI9486, and similar SPI displays with PiTrezor
- **Firmware Compatibility**: Works with modern PiTrezor firmware versions
- **Hardware Integration**: Proper GPIO configuration for buttons and display control
- **Automated Setup**: Everything builds automatically with minimal user intervention

## 📦 What's Included

### Pre-built Components
- **Ready-to-Flash Image**: `pitrezor-raspberrypi0-wifi-universal.img` - Complete working system
- **Installation Files**: Detailed guides and configuration files
- **Source Code**: Build scripts and diagnostic tools
- **Documentation**: Complete setup instructions and troubleshooting guides

### Key Features
✅ Modern PiTrezor firmware (universal cryptocurrency support)  
✅ Working ILI9341 color display with proper drivers  
✅ WiFi connectivity for Trezor Suite integration  
✅ Automated first-boot configuration  
✅ Comprehensive diagnostic tools  
✅ Detailed installation and user manuals  

## 🚀 Quick Start

### Option 1: Flash Pre-built Image (Recommended)
```bash
# Using Balena Etcher or Raspberry Pi Imager:
1. Download Raspberry Pi Imager
2. Select: pitrezor-raspberrypi0-wifi-universal.img
3. Flash to microSD card
4. Connect ILI9341 display using GPIO pins (see wiring guide)
5. Insert SD card and power on
6. Display should work after 2-5 minute first boot setup
```

### Option 2: Manual Installation
See `docs/INSTALLATION_GUIDE.html` for detailed step-by-step instructions.

## 🔧 Hardware Requirements

### Raspberry Pi Zero W
- Processor: BCM2835 ARM11 (1GHz single-core)
- RAM: 512 MB
- WiFi: 802.11 b/g/n (required for Trezor Suite)
- GPIO: Standard 40-pin layout

### ILI9341 Display
- Controller: ILI9341 (ILI9486 also supported)
- Resolution: 240×320 pixels
- Interface: SPI (Serial Peripheral Interface)
- Supply: 3.3V power and logic

### GPIO Connections
| Display Pin | Pi Zero GPIO | Function |
|-------------|-------------|----------|
| VCC | 3.3V | Power (CRITICAL: 3.3V only) |
| GND | GND | Ground |
| CS | GPIO 8 | Chip Select |
| RESET | GPIO 25 | Display Reset |
| DC | GPIO 24 | Data/Command Select |
| MOSI | GPIO 10 | SPI Data Input |
| SCK | GPIO 11 | SPI Clock |
| LED | GPIO 18 | Backlight Control |
| YES | GPIO 20 | Confirm Button |
| NO | GPIO 13 | Cancel Button |

See `docs/WIRING_GUIDE.md` for detailed diagrams.

## 📋 Documentation

- **[User Manual](docs/User%20Operation-Instruction%20Manual.html)** - Operating guide and common tasks
- **[Build & Flash Guide](docs/Build%20and%20Flash%20Instrcution%20Manual.html)** - Installation instructions
- **[Feature Overview](docs/Feature%20Overview.md)** - Technical project details
- **[Project README](docs/PROJECT_README.md)** - Complete technical documentation

## 🛠️ Installation Methods

### Method 1: Pre-built Image (Easiest - 15 minutes)
Recommended for most users. Image includes everything pre-configured.

### Method 2: Manual Installation (Advanced - 1-2 hours)
For customization or if you want to build everything yourself.

## 🐛 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| Black Screen | Enable SPI in `/boot/config.txt` - add `dtparam=spi=on` |
| Garbled Display | Lower SPI speed in config: `FBCP_SPI_SPEED_DIVISOR=40` |
| Buttons Not Responding | Verify GPIO wiring, check pin assignments |
| WiFi Won't Connect | Ensure 2.4GHz network, verify password, move closer to router |

For detailed troubleshooting, see the User Manual or run:
```bash
/opt/pitrezor/scripts/comprehensive-display-debug.sh
```

## 📊 Performance Characteristics

- **First Boot**: 2-5 minutes (builds optimized display driver)
- **Subsequent Boots**: ~30 seconds (uses cached driver)
- **Display Response**: Real-time framebuffer copying
- **Button Latency**: <100ms response time
- **Power Usage**: ~2A at 5V (includes display backlight)

## 🔐 Security Features

- Hardware-based encryption on Trezor firmware
- PIN protection for device access
- Seed phrase recovery capability
- Air-gapped operation (private keys never leave device)
- On-device transaction approval (protects against malware)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Components
- **PiTrezor**: [SatoshiLabs/Trezor](https://github.com/trezor) (LGPL 3.0)
- **fbcp-ili9341**: [juj/fbcp-ili9341](https://github.com/juj/fbcp-ili9341) (MIT)
- **Raspberry Pi**: [Raspberry Pi Foundation](https://www.raspberrypi.com/) (Various)

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest improvements
- Share working configurations
- Improve documentation

## 📚 Resources

- [Trezor Official Documentation](https://docs.trezor.io/)
- [fbcp-ili9341 GitHub](https://github.com/juj/fbcp-ili9341)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [Trezor Suite](https://suite.trezor.io/)

## ❓ Support

For issues, questions, or feature requests:
1. Check the [Troubleshooting Guide](docs/User%20Operation-Instruction%20Manual.html#troubleshooting)
2. Review the [Installation Guide](docs/Build%20and%20Flash%20Instrcution%20Manual.html)
3. Run diagnostic tools included in the package
4. Open an issue on GitHub with detailed information

## 📝 Project Status

**Status**: ✅ Complete & Working  
**Last Updated**: November 28, 2025  
**Version**: 1.13.1.0  

### Tested Configurations
- ✅ Raspberry Pi Zero W + ILI9341 Display
- ✅ Modern PiTrezor firmware (universal mode)
- ✅ Trezor Suite remote connection
- ✅ WiFi connectivity and operation
- ✅ All cryptocurrency types

---

**Created with ❤️ for the cryptocurrency hardware wallet community**

For more information, see the complete documentation in the `/docs` folder.
