# Learning Objective:
# This tutorial teaches how to design a simple, extensible command-line unit converter
# using a modular plugin system in Python. You will learn to define an interface
# with Abstract Base Classes (ABCs), create different "plugin" implementations that
# adhere to this interface, and dynamically load/use these plugins at runtime.
# This demonstrates principles of modularity, polymorphism, and how to easily add
# new conversion types without modifying the core application logic.

import sys
import abc # 'abc' module provides tools for Abstract Base Classes

# --- 1. Define the Plugin Interface (Abstract Base Class) ---
# This `ConverterPlugin` is an Abstract Base Class (ABC). It defines the blueprint
# or "contract" that all specific converter plugins must follow.
# By inheriting from `abc.ABC` and using `@abc.abstractmethod`/@abc.abstractproperty,
# we ensure that any class pretending to be a ConverterPlugin MUST implement these.
class ConverterPlugin(abc.ABC):
    @abc.abstractproperty
    def supported_units(self) -> set[str]:
        """
        Returns a set of all units (strings, e.g., "m", "C") that this specific
        converter plugin is capable of handling.
        This is an abstract property, meaning subclasses MUST provide an implementation.
        """
        pass

    @abc.abstractmethod
    def can_convert(self, from_unit: str, to_unit: str) -> bool:
        """
        Checks if this plugin can perform a conversion between the given units.
        This method allows the main application to query each plugin before attempting
        a conversion, ensuring only relevant plugins are used.
        """
        pass

    @abc.abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Performs the actual unit conversion.
        This is the core logic that each plugin provides for its specific domain.
        Subclasses MUST implement this method.
        """
        pass

# --- 2. Implement Specific Converter Plugins ---
# Each of these classes is a concrete "plugin" that adheres to the ConverterPlugin interface.
# They encapsulate the logic for a specific type of conversion.

class LengthConverter(ConverterPlugin):
    # _conversion_factors maps each unit to its equivalent value in our chosen base unit (meters).
    # This makes conversions easy: A -> Meters -> B.
    _conversion_factors = {
        "m": 1.0,           # meter (our base unit for length)
        "km": 1000.0,       # kilometer
        "cm": 0.01,         # centimeter
        "mm": 0.001,        # millimeter
        "in": 0.0254,       # inch
        "ft": 0.3048,       # foot
        "yd": 0.9144,       # yard
        "mi": 1609.34       # mile
    }

    # Implement the `supported_units` abstract property.
    @property
    def supported_units(self) -> set[str]:
        return set(self._conversion_factors.keys())

    # Implement the `can_convert` abstract method.
    def can_convert(self, from_unit: str, to_unit: str) -> bool:
        # This plugin can convert if both the 'from' and 'to' units are in its dictionary.
        return from_unit in self.supported_units and to_unit in self.supported_units

    # Implement the `convert` abstract method for length conversions.
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not self.can_convert(from_unit, to_unit):
            # This check acts as a safeguard; `can_convert` should ideally be called first.
            raise ValueError(f"Length conversion not supported: {from_unit} to {to_unit}")

        # Step 1: Convert the initial value to the base unit (meters).
        value_in_meters = value * self._conversion_factors[from_unit]
        # Step 2: Convert from the base unit (meters) to the target unit.
        converted_value = value_in_meters / self._conversion_factors[to_unit]
        return converted_value

class TemperatureConverter(ConverterPlugin):
    # This plugin handles temperature units. The conversion logic is different
    # (non-linear formulas) compared to length, but it still fits the same interface!
    _supported_temp_units = {"C", "F", "K"} # Celsius, Fahrenheit, Kelvin

    @property
    def supported_units(self) -> set[str]:
        return self._supported_temp_units

    def can_convert(self, from_unit: str, to_unit: str) -> bool:
        # Check if both units are recognized by this specific temperature converter.
        return from_unit in self.supported_units and to_unit in self.supported_units

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not self.can_convert(from_unit, to_unit):
            raise ValueError(f"Temperature conversion not supported: {from_unit} to {to_unit}")

        # First, convert the 'from' value to a common base (Celsius).
        # This simplifies the conversion logic by breaking it into two steps:
        # 1. Any_Unit -> Celsius, 2. Celsius -> Target_Unit.
        if from_unit == "C":
            val_celsius = value
        elif from_unit == "F":
            val_celsius = (value - 32) * 5/9
        elif from_unit == "K":
            val_celsius = value - 273.15
        else:
            # This case should ideally not be reached if `can_convert` logic is sound.
            raise ValueError(f"Unsupported temperature unit: {from_unit}")

        # Then, convert from the Celsius base to the 'to' unit.
        if to_unit == "C":
            return val_celsius
        elif to_unit == "F":
            return (val_celsius * 9/5) + 32
        elif to_unit == "K":
            return val_celsius + 273.15
        else:
            # Again, this should not be reached.
            raise ValueError(f"Unsupported temperature unit: {to_unit}")

# --- 3. Register and Load Plugins ---

# This list serves as our simple "plugin registry".
# To add a new conversion type (e.g., Area, Volume, Time), you would simply:
# 1. Create a new class (e.g., `AreaConverter`) that inherits from `ConverterPlugin`.
# 2. Implement all abstract methods (`supported_units`, `can_convert`, `convert`).
# 3. Add an instance of your new class to this `UNIT_PLUGINS` list.
# The main application logic (`main` function) does not need to change! This is the essence of extensibility.
UNIT_PLUGINS: list[ConverterPlugin] = [
    LengthConverter(),      # Instantiate our LengthConverter plugin
    TemperatureConverter(), # Instantiate our TemperatureConverter plugin
    # Add more plugin instances here to extend the converter's capabilities.
]

# --- 4. Main Application Logic ---

def main():
    # Check if the correct number of command-line arguments are provided.
    # We expect: script_name <value> <from_unit> <to_unit> (total 4 elements including script_name)
    if len(sys.argv) != 4:
        print("Usage: python converter.py <value> <from_unit> <to_unit>")
        print("Example: python converter.py 10 km mi")
        print("Example: python converter.py 32 F C")
        sys.exit(1) # Exit with a non-zero code to indicate an error.

    try:
        # Parse the command-line arguments.
        value = float(sys.argv[1])
        # Standardize units to lowercase for case-insensitive matching (e.g., "KM" vs "km").
        from_unit = sys.argv[2].lower()
        to_unit = sys.argv[3].lower()

        converted_value = None
        # Iterate through all registered plugins to find one that can handle the request.
        for plugin in UNIT_PLUGINS:
            if plugin.can_convert(from_unit, to_unit):
                # If a plugin reports it can handle the conversion, use it.
                converted_value = plugin.convert(value, from_unit, to_unit)
                break # We found a converter, so we can stop checking other plugins.

        if converted_value is not None:
            # Print the result using an f-string for clear formatting.
            print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
        else:
            # If no plugin could handle the conversion, inform the user.
            print(f"Error: No converter found for {from_unit} to {to_unit}.")
            # Provide hints for supported units from existing plugins.
            print("Supported units for Length: " + ", ".join(sorted(LengthConverter().supported_units)))
            print("Supported units for Temperature: " + ", ".join(sorted(TemperatureConverter().supported_units)))

    except ValueError as e:
        # Catch errors related to invalid input (e.g., non-numeric value) or conversion issues.
        print(f"Error: Invalid input or conversion problem. {e}")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# This standard Python construct ensures that `main()` is called only when the script
# is executed directly (e.g., `python converter.py`), not when imported as a module.
if __name__ == "__main__":
    main()

# --- Example Usage (How to run this code from your terminal) ---
# 1. Save the code above into a file named `converter.py`.

# 2. Open your terminal or command prompt and navigate to the directory
#    where you saved `converter.py`.

# 3. Try these commands:

#    a. Convert 10 kilometers to miles:
#       python converter.py 10 km mi
#       Expected Output: 10.0 km is equal to 6.21 mi

#    b. Convert 32 Fahrenheit to Celsius:
#       python converter.py 32 F C
#       Expected Output: 32.0 F is equal to 0.00 C

#    c. Convert 100 meters to feet:
#       python converter.py 100 m ft
#       Expected Output: 100.0 m is equal to 328.08 ft

#    d. Convert 25 Celsius to Kelvin:
#       python converter.py 25 C K
#       Expected Output: 25.0 C is equal to 298.15 K

#    e. Try an unsupported conversion (e.g., liters to miles):
#       python converter.py 5 L mi
#       Expected Output: Error: No converter found for l to mi.
#                        Supported units for Length: cm, ft, in, km, m, mi, mm, yd
#                        Supported units for Temperature: C, F, K

#    f. Try invalid input (e.g., non-numeric value):
#       python converter.py abc km mi
#       Expected Output: Error: Invalid input or conversion problem. could not convert string to float: 'abc'