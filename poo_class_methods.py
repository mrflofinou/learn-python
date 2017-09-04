####################################################################
# Define an instance method called "know_beard_color"
# It should return the beard color of another instance.
#
# Define a class method to print out the name of each Florian.
####################################################################

class Florian:
    HEIGHT = 1.75
    INSTANCES = []
    NAMES = []

    def __init__(self, beard_color, glasses, name):
        self.beard_color = beard_color
        self.glasses = glasses
        self.name = name
        self.ID = len(self.INSTANCES)
        self.INSTANCES.append([self.beard_color, self.glasses, self.name])
        self.NAMES.append(name)

    def know_beard_color(self, instance):
        for i, florian in enumerate(self.INSTANCES):
            if self.INSTANCES[instance.ID] == self.INSTANCES[i]:
                beard_color = self.INSTANCES[i][0]
        return beard_color

    @classmethod
    def name_each_florian(cls):
        return cls.NAMES


flo = Florian(glasses="noires", beard_color="brun", name="MrFlofinou")
fiflo = Florian(glasses="rouges", beard_color="blanche", name="Robert")
fofli = Florian(glasses="bleues", beard_color="roux", name="Jean-Paul")
print(fiflo.know_beard_color(fiflo))
print(Florian.name_each_florian())
