####################################################################
# Define an instance method called "know_beard_color"
# It should return the beard color of another instance.
#
# Define a class method to print out the name of each Florian.
####################################################################

class Florian:
    HEIGHT = 1.75
    NAMES = []

    def __init__(self, beard_color, glasses, name):
        self.beard_color = beard_color
        self.glasses = glasses
        self.name = name
        self.NAMES.append(name)

    def know_beard_color(self, instance):
        return instance.beard_color

    @classmethod
    def name_each_florian(cls):
        print(cls.NAMES)


flo = Florian(glasses="noires", beard_color="brun", name="MrFlofinou")
fiflo = Florian(glasses="rouges", beard_color="blanche", name="Robert")
fofli = Florian(glasses="bleu", beard_color="roux", name="Jean-Paul")
print(fiflo.know_beard_color(flo))
Florian.name_each_floria()
