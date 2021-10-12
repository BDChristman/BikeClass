# Brian D. Christman
# Purpose: to use object oriented programming to evaluate different bike class settings,
# and ensure that entry errors are caught and corrected for.

# Properties
#  Gears: getGears(), setGears()
#  CurrentGear: getCurGear(), setCurGear()
#  Wheels: getWheels(), setWheels()
#  Brakes: getBrakes(), setBrakes()

# Methods
#  resetGear(curGear)
#  increaseGear(curGear)
#  decreaseGear(curGear)

# Import the package used in this program
import sys


# define Python user-defined exceptions
class Error(Exception):
    # Base error class used for other exceptions
    pass


class InvalidEntryError(Error):
    # Raised when an entry does not meet the functions specifications
    pass


class IncreaseError(Error):
    # Raised when the function attempts to increase above the top boundary
    pass


class DecreaseError(Error):
    # Raised when the function attempts to decrease below the bottom boundary
    pass


# Define the Python class used for the program and its default properties
class Bike:
    # Private properties
    __gears: int = 1
    __curGear: int = 1
    __wheels: int = 1
    __brakes = "hand brakes"

    # Instantiate a copy of this class
    def __init__(self,
                 gears=1,
                 curGear=1,
                 wheels=1,
                 brakes="hand brakes"):

        # Set all the properties
        self.setGears(gears)
        self.setCurGear(curGear)
        self.setWheels(wheels)
        self.setBrakes(brakes)

    # Getter and setter for the number of gears property
    # Holds and tests conditions for running and calls errors if necessary
    def getGears(self) -> int:
        return self.__gears

    def setGears(self, gears: int) -> None:
        try:
            if 1 <= gears <= 15:
                gears = int(gears)
            else:
                raise InvalidEntryError

        except InvalidEntryError:
            print("Error: the number of gears you entered is invalid. Enter an integer between 1 and 15.")
            sys.exit(1)

        try:
            if gears:
                self.__gears = gears

        except Exception as e:
            raise e

    # Getter and setter for the current gear property
    # Holds and tests conditions for running and calls errors if necessary
    def getCurGear(self) -> int:
        return self.__curGear

    def setCurGear(self, curGear: int) -> None:
        try:
            if int(curGear) >= 1 and int(curGear) <= self.__gears:
                curGear = int(curGear)
            else:
                raise InvalidEntryError

        except InvalidEntryError:
            print(
                f"Error: the current gear value you entered is invalid. Enter an integer between 1 and {self.__gears}.")
            sys.exit(1)

        try:
            if curGear:
                self.__curGear = curGear

        except Exception as e:
            raise e

    # Getter and setter for the number of wheels property
    # Holds and tests conditions for running and calls errors if necessary
    def getWheels(self) -> int:
        return self.__wheels

    def setWheels(self, wheels: int) -> None:
        try:
            if int(wheels) >= 1 and int(wheels) <= 4:
                wheels = int(wheels)
            else:
                raise InvalidEntryError

        except InvalidEntryError:
            print("Error: the number of wheels you entered is invalid. Enter an integer between 1 and 4.")
            sys.exit(1)

        try:
            if wheels:
                self.__wheels = wheels

        except Exception as e:
            raise e

    # Getter and setter for the brake type property
    # Holds and tests conditions for running and calls errors if necessary
    def getBrakes(self) -> str:
        return self.__brakes

    def setBrakes(self, brakes: str) -> None:
        try:
            if brakes in ["hand brakes", "foot brakes"]:
                self.__brakes = brakes
            else:
                raise InvalidEntryError

        except InvalidEntryError:
            print(f"Error: invalid brake option. Enter either 'hand brakes' or 'foot brakes'.")
            sys.exit(1)

    # Method for resetting the current gear back to 1
    # Holds and tests conditions for running and calls errors if necessary
    def resetGear(self, curGear: int) -> None:
        try:
            curGear = 1
            print(f"The current gear has been reset to {curGear}.")

        except Exception as e:
            raise e

        try:
            if curGear:
                self.__curGear = curGear

        except Exception as e:
            raise e

    # Method for increasing the current gear by 1
    # Holds and tests conditions for running and calls errors if necessary
    def increaseGear(self, curGear: int) -> None:
        try:
            if int(curGear) >= 1 and int(curGear) < self.__gears:
                curGear = int(curGear) + 1
                print(f"The current gear has increased to {curGear}.")
            else:
                raise IncreaseError

        except IncreaseError:
            print(f"Cannot increase the current gear any further. The current gear is {curGear}.")
            print()

        try:
            if curGear:
                self.__curGear = curGear

        except Exception as e:
            raise e

    # Method for decreasing the current gear by 1
    # Holds and tests conditions for running and calls errors if necessary
    def decreaseGear(self, curGear: int) -> None:
        try:
            if int(curGear) >= 2:
                curGear = int(curGear) - 1
                print(f"The current gear has decreased to {curGear}")
            else:
                raise DecreaseError

        except DecreaseError:
            print(f"Cannot decrease the current gear any further. The current gear is {curGear}.")
            print()
        try:
            if curGear:
                self.__curGear = curGear

        except Exception as e:
            raise e

# Clear the console's browser history each time the program is run.
# This prevents anything from being inappropriately stored and reused.
