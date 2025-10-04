# pi-pico-mobo-ctrl
This project uses a Raspberry Pi Pico as a smart power controller for a custom PC. It generates the missing PWR_OK signal for a 12VO PSU, controls power-on/off via a relay, and manages a 5-minute fan cooldown after shutdown. The Pico senses the PC's on/off state by monitoring a motherboard USB port.
