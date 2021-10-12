# Brian D. Christman
# Purpose: to evaluate the object oriented program bike.py and ensure that
# everything is working properly.

# Import the bike class
from bike import Bike

# Begin the try and except block for error handling
try:
    # Create the first user's bike inputs and print the current gear
    test = Bike(15, 10, 2, "hand brakes")
    print(f"The current gear is {test.getCurGear()}.")

    # Increase the current gear until it attempts to exceed 15
    # This could be done with a while loop as well
    test.increaseGear(test.getCurGear())
    test.increaseGear(test.getCurGear())
    test.increaseGear(test.getCurGear())
    test.increaseGear(test.getCurGear())
    test.increaseGear(test.getCurGear())
    test.increaseGear(test.getCurGear())

    # Reset the current gear to 1 and attempt to go below 1
    # Use the resetGear and decreaseGear functions to do this
    test.resetGear(test.getCurGear())
    test.decreaseGear(test.getCurGear())

    # Change/set the brake type to electric
    # Change the entry below or comment the line out to continue
    test.setBrakes("electric")

# End the general error block and print out any errors.
except Exception as e:
    print(f"Got an error: {e}")

# Clear the console's browser history each time the program is run.
# This prevents anything from being inappropriately stored and reused.
