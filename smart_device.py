class SmartDevice:
    """
    A class representing a smart device.
    """

    device_count = 0
    
    def __init__(self, device_name:str, model_number:str, is_online:bool=False):
        """
        Initializes a new SmartDevice instance.

        Args:
            device_name (str): The name of the device.
            model_number (str): The model number of the device.
            is_online (bool, optional): Whether the device is online. Defaults to False.
            status (dict, optional): The status of the device like battery level, temperature, etc. Defaults to an empty dictionary.
        """
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        SmartDevice.device_count += 1
        
    def update_status(self, attribute, value):
        """
        Updates the status of the device.
        """
        self.status[attribute] = value
    
    def get_status(self, attribute):
        """
        Gets the status of the device.
        """
        return self.status.get(attribute, "Attribute not found")
    
    def toggle_online(self):
        """
        Toggles the online status of the device.
        """
        self.is_online = not self.is_online

    def reset(self):
        """
        Resets the status of the device.
        """
        self.status = {}

    def __call__(self):
        """
        Returns a string representation of the device.
        """
        return f"{self.device_name} (Model: {self.model_number})"
    

    def device_info(self):
        """
        Returns the status of the device.
        """
        return self.status
    
