class Singleton:
    """
    A singleton is a class that can only be instantiated once.
    Any subsequent instantiation returns the same instance.
    """
    
    # Holds the single instance
    _instance = None
    

    def __new__(cls, *args, **kwargs):
        """Override the __new__ method to control instance creation."""
        # If singleton doesn't exist, create new instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    

    def __init__(self, value=None):
        """Initialize the Singleton only once."""

        # Make sure singleton is only initialized once, even if __init__ is called more than once
        if not self._initialized:
            self._initialized = True
            self.value = value if value is not None else "Default Value"
    

    def get_value(self):

        return self.value
    

    def set_value(self, value):

        self.value = value



# Usage example
if __name__ == "__main__":

    value1 = "String_1"
    value2 = "String_2"

    print(f"Creating first instance 's1' with value: '{value1}'...")
    s1 = Singleton(value1)
    print(f"First instance value: {s1.get_value()}\n")
    
    print(f"Attempting to create second instance 's2' with value '{value2}'...")
    s2 = Singleton(value2)    # Does not actually create new instance
    print(f"Second instance value: {s2.get_value()}\n")    # s2 is not a unique instance, but instead a reference to s1
    
    print(f"Checking if first and second instance are the same...\n{s1 == s2}\n")
    
    print("Setting value of 's1' through reference 's2'...")
    s2.set_value(value2)
    print(f"After updating 's2', value of 's1' is: {s1.get_value()}\n\n")
