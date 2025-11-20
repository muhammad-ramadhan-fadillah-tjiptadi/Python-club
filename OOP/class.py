class NamaClass:
    def __init__(self, atribut1=None, atribut2=None):
        # Initialize instance attributes
        self.atribut1 = atribut1
        self.atribut2 = atribut2

    def method1(self, parameter1, parameter2):
        """
        Example method that returns the sum of two parameters
        
        Args:
            parameter1: First number
            parameter2: Second number
            
        Returns:
            Sum of parameter1 and parameter2
        """
        return parameter1 + parameter2

    def method2(self, parameter3):
        """
        Example method that processes parameter3 with instance attributes
        
        Args:
            parameter3: Value to be processed
            
        Returns:
            Dictionary containing processed data
        """
        return {
            'original': parameter3,
            'with_attr1': parameter3 + str(self.atribut1) if self.atribut1 is not None else None,
            'with_attr2': parameter3 * 2 if isinstance(parameter3, (int, float)) else parameter3 * 2
        }