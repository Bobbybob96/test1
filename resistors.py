""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1

resistors.py

Thomas Heine
100777741

this program simulates static resistors and variable resistors

"""
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


class VariableResistor(Resistor):
    """Model a variable resistor that adjusts resistance as a percentage of the fixed value."""
    def __init__(self, res):
        """Constructor sets the fixed resistance and initializes actual resistance to 100%."""
        super().__init__(res)
        self.actual_resistance = res  # start at 100%

    def set_resistance(self, percent):
        """Set the actual resistance as a percentage (0 to 100) of the fixed resistance."""
        if percent < 0 or percent > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.actual_resistance = (percent / 100.0) * self.resistance

    def current(self, voltage):
        """Override to use actual resistance in Ohm's law."""
        return voltage / self.actual_resistance

    def __str__(self):
        """Return a string representation of the variable resistor."""
        return f"R={self.resistance} (actual={self.actual_resistance})"


if __name__ == "__main__":
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    # UNCOMMENT THIS BLOCK TO TEST VariableResistor
    r2 = VariableResistor(1000.0)
    print("R2:", r2)
    print("R2 100%: voltage=12.0, current=", r2.current(12.0))
    r2.set_resistance(50.0)
    print("R2 50%: voltage=12.0, current=", r2.current(12.0))
