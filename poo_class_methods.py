####################################################################
# Define an instance method called "know_beard_color"
# It should return the beard color of another instance.
#
# Define a class method to print out the name of each Florian.
####################################################################

class Florian:
    HEIGHT = 1.80

    def __init__(self, beard_color, glasses):
        self.beard_color = beard_color
        self.glasses = glasses

    def know_beard_color(self, instance):
        print(instance.beard_color)


flo = Florian(glasses="noires", beard_color="brun")
fiflo = Florian(glasses="rouges", beard_color="blanche")
fiflo.know_beard_color(flo)
