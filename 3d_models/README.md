# 3D Enclosure Design - Multi-Layer Network Appliance

## Overview

This directory contains 3D models and design files for a custom enclosure that integrates:
- **Netgear 24-Port Smart Ethernet Switch** (base layer)
- **Radxa X4 N100 SBC** (upper layer, inverted)
- **Linksys AX1800 WiFi Router** (upper layer, inverted)
- **Advanced cooling system** with multiple fans and air channels

## Design Specifications

### Dimensions
- **Overall Enclosure**: 460 × 250 × 180 mm
- **Wall Thickness**: 4 mm (optimized for 3D printing)
- **Material**: ABS or PETG plastic (recommended for durability)

### Component Layers

#### Layer 1 (Base): Netgear 24-Port Smart Switch
- **Position**: Bottom
- **PCB Dimensions**: 440 × 210 × 45 mm
- **Ports**: Ethernet ports on front, power/console on rear
- **Mounting**: Direct on enclosure floor with standoffs

#### Layer 2 (Middle): Cooling System
- **Air Gap**: 40 mm between switch PCB and middle section
- **Vertical Air Channels**: Guides air from side intakes to top exhaust
- **120mm Central Exhaust Fan**: 
  - Mounted at top center
  - Pulls hot air upward from between Radxa and Router
  - Exhaust capacity: ~130-150 CFM

#### Layer 3 (Upper): Radxa X4 & WiFi Router (Inverted Mount)
- **Radxa X4 N100**: 160 × 110 mm PCB (inverted)
- **Linksys AX1800**: 200 × 150 mm PCB (inverted)
- **Vertical Separation**: 30 mm air gap between them
- **Mounting**: Standoffs with custom brackets

### Cooling System Architecture

**Intake (Left & Right)**
- 80mm fans (one on each side)
- Total intake: ~60-80 CFM per fan
- Air flow: Side → Vertical channels → Top exhaust

**Exhaust (Top Center)**
- 120mm fan (central)
- Exhaust capacity: ~130-150 CFM
- Hot air from Radxa and Router PCBs exits upward

**Air Channel Design**
- Side vents on left and right with 80mm fan mounts
- Internal vertical channels force air upward
- Baffle plates create turbulence for better cooling
- Air distribution holes around Radxa/Router to improve SMD cooling

### Ventilation Features

#### Fan Mounts
1. **Left Side 80mm Intake Fan**
   - Position: X=15mm from left edge, centered vertically
   - Hole diameter: 80mm
   - Intake direction: Right (into enclosure)

2. **Right Side 80mm Intake Fan**
   - Position: X=445mm from left (15mm from right edge), centered vertically
   - Hole diameter: 80mm
   - Intake direction: Left (into enclosure)

3. **Top Center 120mm Exhaust Fan**
   - Position: Center top (X=230mm, Y=125mm)
   - Hole diameter: 120mm
   - Exhaust direction: Upward

#### Router Antenna Holes
- **Location**: Right side (router side)
- **Quantity**: 2 holes
- **Diameter**: 16mm each
- **Positions**: 
  - Antenna 1: Y=62.5mm (1/4 depth)
  - Antenna 2: Y=187.5mm (3/4 depth)
- **Purpose**: Allow WiFi router antennas to extend outside enclosure

### Internal Components

#### Mounting Hardware
- **Radxa X4**: 4× M3 standoffs, 20mm height
- **Netgear Switch**: 4× M3 standoffs, 15mm height
- **Router**: 4× M3 standoffs, 20mm height
- **Fans**: Standard 80mm and 120mm fan brackets

#### Cable Management
- **Front**: Ethernet ports (24× RJ45)
- **Rear**: Power inlet, console/serial port
- **Internal**: SBC interconnects (USB, serial)

### Thermal Performance Goals

**Design Targets**
- Keep Radxa SBC < 75°C under load
- Keep WiFi router PCB < 70°C under load
- Keep switch PCB < 65°C under load
- Air circulation: Complete chamber air change every 30-45 seconds

**Cooling Path**
1. Hot air rises from switch PCB
2. Air drawn into side intake fans
3. Forced upward through vertical channels
4. Passes over Radxa and Router PCBs
5. Exits through 120mm top fan

## Files in This Directory

### `generate_enclosure.py`
Python script that generates the base STL model with:
- Main enclosure box (hollow)
- Fan mounting holes (80mm × 2, 120mm × 1)
- Antenna holes (16mm × 2)
- Proper hole depths for fan mounting

**Usage:**
```bash
python generate_enclosure.py
```

**Output:** `multi_layer_enclosure.stl`

### `multi_layer_enclosure.stl`
Binary STL file containing:
- Enclosure geometry
- All fan mount holes
- Antenna holes
- Ready for 3D printing or CAD refinement

## Assembly Instructions

### 1. 3D Printing
- **Print Time**: ~40-60 hours (depending on printer)
- **Material**: ABS or PETG (1.75mm filament)
- **Settings**:
  - Layer Height: 0.2mm
  - Infill: 20% (grid pattern)
  - Support: Yes (for internal channels)
  - Print Speed: 60 mm/s (for quality)

### 2. Post-Processing
- Remove support material carefully
- Sand interior surfaces (120-220 grit) for better airflow
- Clean all dust from interior before assembly

### 3. Assembly Steps

**Step 1: Base Assembly**
1. Install M3 standoffs (15mm) on enclosure floor
2. Place Netgear switch PCB on standoffs
3. Secure with M3 screws

**Step 2: Install Middle Support**
1. Install M3 standoffs (40mm total: 15mm existing + 25mm new) on corners
2. This creates the air gap for cooling

**Step 3: Install Radxa & Router**
1. Mount Radxa X4 inverted on standoffs (20mm)
2. Mount WiFi router PCB inverted above Radxa
3. Leave 30mm air gap between them for 120mm fan

**Step 4: Install Fans**
1. Install 80mm intake fans:
   - Left side: Intake direction → RIGHT
   - Right side: Intake direction → LEFT
2. Install 120mm exhaust fan:
   - Top center: Exhaust direction → UP
3. Use standard fan mounting brackets

**Step 5: Antenna Installation**
1. Insert WiFi router antennas through antenna holes
2. Route antenna cables through dedicated channels
3. Secure antennas with provided clips

**Step 6: Cable Management**
1. Run Ethernet cables to front
2. Route power/console to rear
3. Connect SBC interconnects
4. Cable ties for organization

**Step 7: Seal & Test**
1. Install any cable port covers
2. Power on and test fans
3. Verify airflow with thermal imaging if possible
4. Monitor temperatures during first 24 hours operation

## Refinements in CAD Software

The generated STL is a functional base. For production, refine in CAD:

### Fusion 360 (Recommended)
1. Import multi_layer_enclosure.stl
2. Add internal air channel geometry using Sketch + Loft
3. Create component mounting brackets
4. Add cable guides and clips
5. Generate technical drawings
6. Export refined STL for final print

### FreeCAD (Free Alternative)
1. Open STL file
2. Use Part Design workbench
3. Create air channel pads
4. Add mounting bracket sketches
5. Boolean operations for integration
6. Export as STEP for manufacturing

### Blender (Mesh Editing)
1. Import STL
2. Remesh internal surfaces
3. Add detail geometry
4. UV unwrap for manufacturing documentation
5. Export refined mesh

## Specifications Reference

### Netgear 24-Port Smart Switch
- Model: GS724T or similar
- PCB Size: 440 × 210 × 45 mm
- Power: Rear-mounted connector
- Ports: 24× Gigabit (front), 2× SFP (rear)
- Heat Dissipation: ~20W typical

### Radxa X4 N100
- Form Factor: Single board computer
- Dimensions: 160 × 110 mm
- Power: USB-C PD (20W)
- Processor: Intel Processor N100
- Heat Dissipation: ~15W typical (passive cooling sufficient with active airflow)

### Linksys AX1800 Router
- PCB Size: ~200 × 150 mm
- Power: AC adapter
- WiFi: 802.11ax, 2.4GHz + 5GHz
- Heat Dissipation: ~10W typical

## Thermal Monitoring

### Recommended Sensors
- DS18B20 temperature sensors on each PCB
- Placement:
  - Near CPU/main IC of each board
  - In air path between intake and exhaust

### Monitoring Software
- GPIO-based temperature logging
- Fan speed control based on temperature
- Alert thresholds: Warn at 75°C, shutdown at 85°C

## Future Enhancements

1. **Display Integration**: Add small LCD status display
2. **Fan Speed Control**: PWM-based fan speed adjustment
3. **Power Distribution**: Integrated PDU with outlet control
4. **UPS Integration**: Battery backup section
5. **Rack Mounting**: Add mounting ears for 19" rack
6. **Remote Management**: IPMI-style out-of-band management

## License

This 3D model design is provided as part of the PiTrezor project.
You are free to modify, print, and distribute for personal or educational use.

## Support & Feedback

For modifications, improvements, or questions:
- Create an issue on GitHub
- Share your build photos
- Contribute improved designs

---

**Created**: November 28, 2025  
**Version**: 1.0  
**Status**: Ready for printing and refinement
