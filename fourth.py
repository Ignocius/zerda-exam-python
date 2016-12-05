# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

# The following code should work with the class:

class Rocket:
    def __init__(self, rocket_type, starting_fuel=0, launches_num=0):
        self.rocket_type = rocket_type
        self.starting_fuel = starting_fuel
        self.launches_num = launches_num

    def launch(self):
        if self.starting_fuel > 0:
            self.launches_num += 1
            if self.rocket_type == 'falcon1':
                self.starting_fuel -= 1
            else:
                self.starting_fuel -= 9

    def refill(self):
        used_Fuel = 0
        if self.rocket_type == 'falcon1':
            while self.starting_fuel < 5:
                self.starting_fuel += 1
                used_Fuel += 1
        else:
            while self.starting_fuel < 20:
                self.starting_fuel += 1
                used_Fuel += 1
        return used_Fuel

    def getStats(self):
        return("name: {0}, fuel: {1}, launches: {2}".format(self.rocket_type, str(self.starting_fuel), str(self.launches_num)))

falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
