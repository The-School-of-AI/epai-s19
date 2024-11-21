# Smart Device Controller 🎮

A Python implementation of a smart device controller created as part of the EPAI (Extensive Python AI) course. This project demonstrates advanced Python concepts including class attributes, callable classes, and function attributes.

## 🌟 Features

- Class-based smart device implementation
- Device status management and tracking
- Built-in device counter
- Callable class functionality
- Function attributes for device information
- Comprehensive test coverage

## 🧩 Class Structure

### SmartDevice Class
The main class that implements smart device functionality:

```python
device = SmartDevice(device_name="Living Room Light", model_number="LRL001", is_online=False)
```

#### Key Components:

1. **Class Attributes**
   - `device_count`: Tracks total number of devices created

2. **Instance Attributes**
   - `device_name`: Name of the device
   - `model_number`: Device model number
   - `is_online`: Device online status
   - `status`: Dictionary storing device status attributes

3. **Methods**
   - `update_status(attribute, value)`: Update device status
   - `get_status(attribute)`: Retrieve status attributes
   - `toggle_online()`: Toggle device online state
   - `reset()`: Reset device to default state

4. **Special Features**
   - Callable class implementation
   - `device_info` function attribute

## 🚀 Usage Examples

```python
# Create a new device
device = SmartDevice("Kitchen Light", "KL100")

# Update device status
device.update_status("battery", 85)
device.update_status("temperature", 24.5)

# Get specific status
battery_level = device.get_status("battery")  # Returns 85

# Toggle device online status
device.toggle_online()

# Use callable instance
print(device())  # Prints formatted device name and model

# Get device info using function attribute
info = device.device_info()
```

## 🧪 Testing

The project includes comprehensive tests in `test_smart_device.py`. Run tests using:

```bash
pytest test_smart_device.py
```

## 🎓 Educational Context

This project is part of the EPAI course curriculum, demonstrating:
- Object-Oriented Programming in Python
- Class and Instance Attributes
- Special Methods (`__init__`, `__call__`)
- Function Attributes
- Property Decorators
- Test-Driven Development

## 📝 Requirements

- Python 3.6+
- pytest (for running tests)

