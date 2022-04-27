"""Python serial number generator."""


from time import sleep


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a generator that let user input a start point"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Show terminal represintation"""
        return f"<Generator start = {self.start} next = {self.next}>"

    def generator(self):
        """Returns the next number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Rests the generator to the start point"""
        self.next = self.start
