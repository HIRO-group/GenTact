# SparkFun Pro Micro ESP32-C3 Capacitive Sensor Project

This project demonstrates how to use capacitive sensing with the SparkFun Pro Micro ESP32-C3 and the CapacitiveSensorR4 library.

## Hardware Requirements

- **SparkFun Pro Micro ESP32-C3** board
- **1MΩ resistor** (1 megohm, critical for proper operation)
- **Jumper wires** for connections
- **Capacitive sensor material** (aluminum foil, copper tape, or wire)
- **Optional**: External LED with 220Ω resistor

## Pin Connections

### SparkFun Pro Micro ESP32-C3 Pinout Reference

The ESP32-C3 has the following key pins available:

| Pin | GPIO | Function | Notes |
|-----|------|----------|-------|
| D0  | GPIO0 | Boot/Flash button | Use for input only |
| D1  | GPIO1 | TX/Debug | Available for I/O |
| D2  | GPIO2 | Built-in LED | Can be used as LED output |
| D3  | GPIO3 | RX/Debug | Available for I/O |
| D4  | GPIO4 | **SEND PIN** | Used in our example |
| D5  | GPIO5 | **RECEIVE PIN** | Used in our example |
| D6  | GPIO6 | General I/O | Available |
| D7  | GPIO7 | General I/O | Available |
| D8  | GPIO8 | General I/O | Available |
| D9  | GPIO9 | General I/O | Available |
| D10 | GPIO10 | **LED PIN** | Used in our example |

### Wiring Diagram

```
ESP32-C3 Pro Micro      1MΩ Resistor      Capacitive Sensor
┌──────────────────┐         │                    │
│                  │         │                    │
│  GPIO4 (Send)    ├─────────┼────────────────────┤
│                  │         │                    │
│  GPIO5 (Receive) ├─────────┘                    │
│                  │                              │
│  GPIO10 (LED)    ├──[220Ω]──┤LED├──┐           │
│                  │                   │           │
│  GND             ├───────────────────┘           │
│                  │                               │
│                  │    Capacitive Sensor         │
│                  │    (foil, copper tape,       │
│                  │     or bare wire)            │
└──────────────────┘                              │
                                                  │
┌─────────────────────────────────────────────────┘
│ Touch surface - when touched, capacitance changes
│ and the sensor detects the touch
└─────────────────────────────────────────────────
```

### Detailed Connection Instructions

1. **Send Pin Connection:**
   - Connect GPIO4 to one terminal of the 1MΩ resistor

2. **Receive Pin Connection:**
   - Connect GPIO5 to the other terminal of the 1MΩ resistor
   - Also connect GPIO5 to your capacitive sensor material

3. **LED Connection (Optional):**
   - Connect GPIO10 through a 220Ω resistor to the positive leg of an LED
   - Connect the negative leg of the LED to GND
   - Alternatively, use the built-in LED on GPIO2

4. **Capacitive Sensor Material:**
   - Use aluminum foil, copper tape, or even a piece of wire
   - Size affects sensitivity: larger = more sensitive
   - Keep away from other conductors to avoid interference

## Software Setup

### 1. Install Arduino IDE
- Download from [arduino.cc](https://www.arduino.cc/en/software)
- Install version 2.0 or later

### 2. Install ESP32 Board Package
1. Open Arduino IDE
2. Go to **File > Preferences**
3. Add this URL to "Additional Board Manager URLs":
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
4. Go to **Tools > Board > Boards Manager**
5. Search for "ESP32" and install "esp32 by Espressif Systems"

### 3. Install CapacitiveSensorR4 Library
1. Go to **Tools > Manage Libraries**
2. Search for "CapacitiveSensorR4"
3. Install "CapacitiveSensorR4" by Paul Badger
4. If not found, you can install it manually:
   - Download from: https://github.com/PaulStoffregen/CapacitiveSensor
   - Extract to your Arduino libraries folder

### 4. Board Selection
1. Go to **Tools > Board**
2. Select **ESP32 Arduino > ESP32C3 Dev Module**
3. Or if available: **ESP32 Arduino > SparkFun ESP32-C3 Thing Plus**

### 5. Upload Settings
- **CPU Frequency**: 160 MHz
- **Flash Frequency**: 80 MHz
- **Flash Mode**: DIO
- **Flash Size**: 4MB
- **Partition Scheme**: Default 4MB with spiffs
- **Port**: Select the correct COM port

## How It Works

### Capacitive Sensing Principle
- The library measures the time it takes to charge a capacitor through the resistor
- When you touch the sensor, you add your body's capacitance to the circuit
- This changes the charge time, which the library detects as a touch

### Code Features
1. **Automatic Calibration**: Establishes baseline when not touched
2. **Touch Detection**: Compares current reading to baseline + threshold
3. **Debouncing**: Prevents false triggers from electrical noise
4. **LED Feedback**: Visual indication of touch status
5. **Serial Output**: Real-time data for monitoring and debugging

## Troubleshooting

### Common Issues and Solutions

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| No readings | Wrong resistor value | Use exactly 1MΩ resistor |
| Erratic readings | Electrical interference | Move away from power supplies, WiFi |
| Too sensitive | Threshold too low | Increase touch threshold in code |
| Not sensitive enough | Threshold too high | Decrease threshold or use larger sensor |
| Library not found | Not installed | Install CapacitiveSensorR4 via Library Manager |

### Sensitivity Adjustment
- **More Sensitive**: Use larger sensor area, decrease threshold
- **Less Sensitive**: Use smaller sensor area, increase threshold
- **Code Adjustment**: Modify the `touchThreshold` variable or call `adjustSensitivity()`

### Optimal Resistor Values
- **1MΩ (recommended)**: Good balance of sensitivity and stability
- **Higher values (2-10MΩ)**: More sensitive but more prone to noise
- **Lower values (100kΩ-500kΩ)**: Less sensitive but more stable

## Example Output

When running correctly, you should see output like this:

```
SparkFun Pro Micro ESP32-C3 Capacitive Sensor Example
=====================================================
Calibrating sensor baseline...
..........
Calibration complete. Baseline: 85
Touch threshold set to: 93
Sensor ready!
Raw: 87, Filtered: 86, Baseline: 85, Difference: 1, Touch: NO
Raw: 89, Filtered: 87, Baseline: 85, Difference: 2, Touch: NO
*** TOUCH DETECTED ***
Raw: 156, Filtered: 143, Baseline: 85, Difference: 58, Touch: YES
Raw: 158, Filtered: 145, Baseline: 85, Difference: 60, Touch: YES
*** TOUCH RELEASED ***
Raw: 91, Filtered: 134, Baseline: 85, Difference: 49, Touch: NO
```

## Advanced Configuration

### Multiple Sensors
To add more sensors, create additional CapacitiveSensor objects:

```cpp
CapacitiveSensorR4 sensor1 = CapacitiveSensorR4(4, 5);   // GPIO4 -> GPIO5
CapacitiveSensorR4 sensor2 = CapacitiveSensorR4(6, 7);   // GPIO6 -> GPIO7
CapacitiveSensorR4 sensor3 = CapacitiveSensorR4(8, 9);   // GPIO8 -> GPIO9
```

### Sensitivity Tuning
```cpp
// In your setup() function
adjustSensitivity(0.05);  // Very sensitive (5% above baseline)
adjustSensitivity(0.15);  // Less sensitive (15% above baseline)
```

## Safety Notes
- Use appropriate resistor values to prevent damage
- Avoid short circuits between pins
- Don't exceed 3.3V on any GPIO pin
- Be mindful of current limits (max 12mA per pin)

## Further Reading
- [CapacitiveSensor Library Documentation](https://github.com/PaulStoffregen/CapacitiveSensor)
- [ESP32-C3 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)
- [SparkFun Pro Micro ESP32-C3 Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro-rp2040-hookup-guide)

## License
This example code is provided under the MIT License. Feel free to modify and use in your projects. 