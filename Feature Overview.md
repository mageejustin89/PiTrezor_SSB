# PiTrezor ILI9341 Display Integration Project

**Complete solution for adding ILI9341 SPI displays to PiTrezor hardware wallets**

## 📦 Project Overview

This project provides everything needed to integrate ILI9341 color SPI displays with PiTrezor firmware, including automated build scripts, configuration files, diagnostic tools, and pre-built images.

### 🎯 What This Solves
- **Display Compatibility**: Enables ILI9341, ILI9486, and similar SPI displays with PiTrezor
- **Firmware Compatibility**: Works with both old and new PiTrezor firmware versions  
- **Hardware Integration**: Proper GPIO configuration for buttons and display control
- **Automatic Setup**: No manual compilation required, everything builds automatically

## 📁 Package Contents

### 1. Source Code Package (`source-code.zip`)
- **Build Scripts**: Automated fbcp-ili9341 compilation with Pi Zero optimizations
- **Service Scripts**: Display mirror service and PiTrezor startup scripts  
- **Diagnostic Tools**: Comprehensive troubleshooting and hardware test scripts
- **Documentation**: Technical details and customization guides

### 2. Source Files Package (`source-files.zip`)  
- **Configuration Files**: Ready-to-use pitrezor.config with display settings
- **Installation Instructions**: Step-by-step manual setup guide
- **Hardware Wiring**: GPIO pin assignments and connection diagrams
- **Boot Configuration**: SPI enablement and system settings

### 3. Ready-to-Flash Images (in `Modified IMG` folder)
- **`pitrezor-REVERSE-TRANSPLANT-universal.img`**: Final working image with modern firmware + working display
- **Previous iteration images**: For reference and testing

## 🚀 Quick Start

### Option 1: Flash Ready Image (Easiest)
1. Flash `pitrezor-REVERSE-TRANSPLANT-universal.img` to SD card
2. Connect ILI9341 display using standard GPIO pins
3. Insert SD card and power on
4. Display should work automatically after 2-5 minute first boot setup

### Option 2: Manual Installation
1. Extract `source-files.zip`
2. Follow installation guide in `source-files/README.md`  
3. Extract `source-code.zip` for build scripts
4. Configure and test using provided tools

## 🔧 Technical Approach

### The "Reverse Transplant" Method
Instead of trying to fix display drivers on new firmware images, we:

1. **Started with working base**: Used old PiTrezor image with proven display drivers
2. **Transplanted modern firmware**: Extracted new PiTrezor binaries and replaced old ones
3. **Preserved display ecosystem**: Kept all working display drivers and configurations
4. **Updated startup logic**: Modified scripts for universal firmware compatibility

This approach is more reliable than trying to fix complex display driver issues on new images.

### Key Innovations
- **Configuration-driven builds**: All settings read from pitrezor.config
- **Intelligent service timing**: Display driver starts after PiTrezor application  
- **Graceful fallbacks**: Multiple backup options if components fail
- **Universal firmware**: Full cryptocurrency support, not just Bitcoin
- **Comprehensive diagnostics**: Complete troubleshooting toolkit

## 📋 Hardware Requirements

### Raspberry Pi Zero W
- **Required**: Pi Zero W (WiFi needed for Trezor Suite connection)
- **GPIO Pins**: Standard layout, no HAT conflicts
- **Power**: Stable 5V supply (display increases power consumption)

### ILI9341 Display  
- **Supported**: ILI9341, ILI9486, Adafruit PiTFT, WaveShare 35B
- **Interface**: SPI (requires 7 GPIO pins)
- **Resolution**: 240x320 or 320x480 depending on model
- **Backlight**: GPIO-controlled LED backlight

### GPIO Connections
```
Display Pin  →  Pi Zero GPIO  →  Description
VCC          →  3.3V          →  Power (critical - must be 3.3V)
GND          →  Ground        →  Ground connection
CS           →  CE0 (GPIO 8)  →  SPI chip select  
RESET        →  GPIO 25       →  Display reset
DC           →  GPIO 24       →  Data/Command select
SDI/MOSI     →  GPIO 10       →  SPI data input
SCK          →  GPIO 11       →  SPI clock
LED          →  GPIO 18       →  Backlight control

YES Button   →  GPIO 20       →  Confirm/OK button
NO Button    →  GPIO 13       →  Cancel/Back button
```

## 🛠️ Configuration Options

### Display Types
- **ILI9341**: 240x320, most common, good performance
- **ILI9486**: 320x480, larger, requires slower SPI speed  
- **ADAFRUIT_PITFT**: Adafruit-specific optimizations
- **WAVESHARE35B**: WaveShare 3.5" display support

### Performance Tuning
- **SPI Speed**: `FBCP_SPI_SPEED_DIVISOR` (20-60, higher = more stable)
- **Scale Factor**: `TREZOR_OLED_SCALE` (1-16, display zoom level)
- **Statistics**: `FBCP_ENABLE_STATS` (performance overlay)

### Firmware Mode
- **Universal**: All cryptocurrencies supported (recommended)
- **Bitcoin-only**: Smaller firmware, Bitcoin transactions only

## 🐛 Troubleshooting

### Common Issues
1. **Black Screen**: Usually SPI not enabled (`dtparam=spi=on` in `/boot/config.txt`)
2. **No Display**: Check 3.3V power connection and wiring
3. **Garbled Display**: Wrong display type or SPI speed too high
4. **No Response**: GPIO button wiring or configuration issue

### Diagnostic Tools
- **`comprehensive-display-debug.sh`**: Complete system analysis
- **`hardware-test.sh`**: Basic GPIO and backlight testing
- **Built-in logs**: Check console output during boot

### Support Resources
- **Detailed README files**: Step-by-step troubleshooting  
- **Hardware diagrams**: GPIO wiring verification
- **Configuration examples**: Working settings for common setups

## 📈 Project Timeline

- **Initial Development**: fbcp-ili9341 integration attempts
- **Display Driver Troubleshooting**: SPI configuration and timing issues
- **Reverse Transplant Innovation**: Switch from display fixing to firmware transplant
- **Final Solution**: Working universal firmware with proven display drivers
- **Documentation**: Comprehensive source code and installation packages

## 🎯 Results

### Successful Integration
- ✅ **Modern PiTrezor firmware** compatible with Trezor Suite
- ✅ **Working ILI9341 display** with proper color and responsiveness  
- ✅ **Universal cryptocurrency support** (not limited to Bitcoin)
- ✅ **Stable operation** with proper timing and fallbacks
- ✅ **Automated setup** requiring minimal user intervention

### Performance Characteristics  
- **First boot**: 2-5 minutes (builds optimized display driver)
- **Subsequent boots**: 30 seconds (uses cached driver)
- **Display response**: Real-time framebuffer copying
- **Button response**: Immediate GPIO input handling
- **Power consumption**: Slightly increased due to display backlight

## 📜 License & Credits

### Original Software
- **PiTrezor**: SatoshiLabs (Trezor) project
- **fbcp-ili9341**: Jukka Jylänki (juj) GitHub project
- **Raspberry Pi**: Raspberry Pi Foundation

### This Project  
- **Integration scripts**: Custom development for PiTrezor compatibility
- **Configuration files**: Optimized for Pi Zero W hardware
- **Documentation**: Complete setup and troubleshooting guides
- **Diagnostic tools**: Custom troubleshooting and testing utilities

---

**Created: November 12, 2025**  
**Project: PiTrezor ILI9341 Display Integration**  
**Method: Reverse Firmware Transplant**  
**Status: Complete Working Solution** ✅