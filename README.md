# Pi Pico Motherboard Controller

This project turns a Raspberry Pi Pico into a custom PC power management controller, designed to interface a modern case with a proprietary motherboard and a 12VO power supply.

This controller solves several hardware compatibility issues:

- It generates the missing `PWR_OK` ("Power Good") signal required by the motherboard to boot safely.
- It intelligently controls the case fans via a 5V relay, adding a five-minute cooldown period after the PC shuts down.
- It reads the case's power and reset buttons and uses a second relay to operate the motherboard's power switch.
- It knows if the PC is on or off by directly sensing the 5V power from a motherboard USB port.

---

## 🔌 Final Pinout Guide

This pinout matches your selected project version.

### ⚡ Power & Ground

- **`VBUS` (Pin 40):** Power Input
  - **Connects to:** The `+5V` wire from your external power supply.
- **`GND` (e.g., Pin 38):** Common Ground
  - **Connects to:** The `Ground` from your external PSU, shared with all other components.

### 📥 Inputs (Sensing)

- **`GP14` (Pin 19):** Case Power Button
  - **Connects to:** The case's physical power button.
- **`GP15` (Pin 20):** Case Reset Button
  - **Connects to:** The case's physical reset button.
- **`GP22` (Pin 29):** PC Power State Sensor
  - **Connects to:** The `+5V` wire from a motherboard USB port.

### 📤 Outputs (Control)

- **`GP12` (Pin 16):** Motherboard Power Control
  - **Connects to:** The Low-Voltage (LV) input on your logic level converter for the power button relay.
- **`GP16` (Pin 21):** Case LED Control
  - **Connects to:** The positive `(+)` lead of the case's front panel LED.
- **`GP17` (Pin 22):** Power OK Signal
  - **Connects to:** The Low-Voltage (LV) input on your logic level converter for the `PWR_OK` signal.
- **`GP18` (Pin 24):** Fan Relay Control
  - **Connects to:** The Low-Voltage (LV) input on your logic level converter for the fan relay.

###  Other

- **Fan Relay:** 
  - **Connects to:** NC (Normally Closed) terminal on your fan relay.

- **MOBO PWR Relay:** 
  - **Connects to:** NO (Normally Open) terminal on your power button relay.