# Solar Power Monitoring System
# EEE Student GitHub Project

import random
import time
from datetime import datetime

# Solar panel specifications
PANEL_RATED_POWER = 1000  # Watts
SOLAR_IRRADIANCE = 1000   # W/m²

# Energy accumulated in kWh
total_energy = 0.0


def read_solar_data():
    """Generate simulated solar panel sensor readings."""

    voltage = random.uniform(30, 42)       # Volts
    current = random.uniform(5, 24)        # Amps
    irradiance = random.uniform(500, 1000) # W/m²

    return voltage, current, irradiance


def calculate_power(voltage, current):
    """Calculate solar power in watts."""
    return voltage * current


def calculate_efficiency(power, irradiance):
    """Calculate approximate panel efficiency."""
    if irradiance == 0:
        return 0

    efficiency = (power / PANEL_RATED_POWER) * 100
    return min(efficiency, 100)


def display_data(voltage, current, irradiance, power, efficiency):
    """Display monitoring information."""

    print("\n" + "=" * 50)
    print("        SOLAR POWER MONITORING SYSTEM")
    print("=" * 50)

    print("Time              :", datetime.now().strftime("%H:%M:%S"))
    print(f"Solar Voltage     : {voltage:.2f} V")
    print(f"Solar Current     : {current:.2f} A")
    print(f"Solar Irradiance  : {irradiance:.2f} W/m²")
    print(f"Output Power      : {power:.2f} W")
    print(f"Panel Efficiency  : {efficiency:.2f} %")

    if power < 200:
        status = "LOW POWER"
    elif power < 600:
        status = "NORMAL"
    else:
        status = "HIGH POWER"

    print("System Status     :", status)
    print("=" * 50)


def main():
    global total_energy

    # Monitoring interval in seconds
    interval = 2

    print("Starting Solar Power Monitoring System...")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:

            # Read sensor values
            voltage, current, irradiance = read_solar_data()

            # Calculate power
            power = calculate_power(voltage, current)

            # Calculate efficiency
            efficiency = calculate_efficiency(power, irradiance)

            # Energy = Power × Time
            energy = (power * interval) / 3600000
            total_energy += energy

            # Display results
            display_data(
                voltage,
                current,
                irradiance,
                power,
                efficiency
            )

            print(f"Energy Generated : {total_energy:.6f} kWh")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n\nSolar monitoring stopped.")
        print(f"Total Energy Generated: {total_energy:.6f} kWh")


if __name__ == "__main__":
    main()
