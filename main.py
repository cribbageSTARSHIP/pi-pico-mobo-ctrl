import machine
import time

# --- Pin Definitions ---
# Inputs
power_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
reset_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
pc_state_sensor = machine.Pin(22, machine.Pin.IN) # Direct 5V sensing

# Outputs
case_led = machine.Pin(16, machine.Pin.OUT)
motherboard_power_control = machine.Pin(12, machine.Pin.OUT)
power_ok_signal = machine.Pin(17, machine.Pin.OUT)
fan_relay_control = machine.Pin(18, machine.Pin.OUT)

# --- Constants ---
POWER_OK_DELAY_MS = 300
FAN_COOLDOWN_MINUTES = 5
FAN_COOLDOWN_MS = FAN_COOLDOWN_MINUTES * 60 * 1000

# --- Initial State ---
motherboard_power_control.high() # Set HIGH to keep active-low relay OFF
power_ok_signal.low()
case_led.low()
fan_relay_control.high() # Set HIGH to keep active-low fan relay OFF
print("Pico controller initialized. Waiting for commands.")

# --- Helper Function ---
def pulse_motherboard_power():
    """Simulates a short, momentary power button press via the relay."""
    print("Pulsing motherboard power control relay...")
    motherboard_power_control.low()
    time.sleep_ms(500)
    motherboard_power_control.high()

# --- Main Loop ---
pc_is_on_flag = pc_state_sensor.value() == 1
shutdown_fan_timer_start = 0

while True:
    current_pc_state = pc_state_sensor.value() == 1
    
    # --- State Change Detection (Handles PWR_OK and Fans) ---
    if current_pc_state and not pc_is_on_flag: # PC just turned ON
        print("PC turned ON.")
        fan_relay_control.low() # Turn fans ON
        shutdown_fan_timer_start = 0
        print(f"Waiting {POWER_OK_DELAY_MS}ms to send PWR_OK...")
        time.sleep_ms(POWER_OK_DELAY_MS)
        power_ok_signal.high()
        print("PWR_OK signal sent.")
        
    elif not current_pc_state and pc_is_on_flag: # PC just turned OFF
        print("PC turned OFF.")
        power_ok_signal.low()
        print(f"Starting {FAN_COOLDOWN_MINUTES}-minute fan cooldown.")
        shutdown_fan_timer_start = time.ticks_ms()
        
    pc_is_on_flag = current_pc_state
    
    # --- Cooldown Timer Logic ---
    if shutdown_fan_timer_start != 0:
        if time.ticks_diff(time.ticks_ms(), shutdown_fan_timer_start) >= FAN_COOLDOWN_MS:
            print("Cooldown complete. Turning fans OFF.")
            fan_relay_control.high()
            shutdown_fan_timer_start = 0
            
    case_led.value(pc_is_on_flag)

    # --- Simple Button Logic ---
    # Power button turns PC on (if off) or requests clean shutdown (if on)
    if power_button.value() == 0:
        print("Power button pressed.")
        pulse_motherboard_power()
        time.sleep(1) # Debounce to prevent multiple presses

    # Reset button requests a clean shutdown/reboot if the PC is on
    if reset_button.value() == 0 and pc_is_on_flag:
        print("Reset button pressed. Requesting OS shutdown/reboot.")
        pulse_motherboard_power()
        time.sleep(1) # Debounce
    
    time.sleep_ms(50)