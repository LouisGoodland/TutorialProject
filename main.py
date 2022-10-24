"""
This is the main file that will be ran in the code.
This file contains 4 classes for the problem described. As well as
some testing code for the classes.
The only import used is Enum, which allows for Enumerations in Python.
"""
# Import used for Enumeration
from enum import Enum


class FuelType(Enum):
    """
    This is an Enum for the 3 valid fuel types for a vehicle.
    It can be either Petrol, Diesel or Electric
    """

    PETROL = 1
    DIESEL = 2
    ELECTRIC = 3


class Vehicle:
    """
    This is the parent class of car, motorbike and van: vehicle.
    It models the general functionality a vehicle can do.
    It contains 3 attributes:
        engine_size: (int) The size of the vehicles' engine.

        num_of_seats: (int) The number of seats the vehicle has.

        fuel_type: (FuelType) The type of fuel the vehicle uses.

    It contains 2 methods:
        __init__(engine_size, num_of_seats, fuel_type): Initiates the class

        drive(): Performs the driving function*
    """

    def __init__(self, engine_size, num_of_seats, fuel_type):
        """
        Initialise method that sets the input parameters to the class attributes after validation
            :param engine_size: (int) representing the engine size in cc

            :param num_of_seats: (int) representing the number of seats

            :param fuel_type: (FuelType) A representation the vehicles fuel type
        """

        # Throws an error if a vehicle is created (not van / car e.t.c)
        if type(self) is Vehicle:
            raise Exception('Base is an abstract class and cannot be instantiated directly')

        try:

            # Checks that each of the parameters are of the correct type
            if not isinstance(engine_size, int):
                raise Exception("engine_size is not an integer")
            if not isinstance(num_of_seats, int):
                raise Exception("num_of_seats is not an integer")
            if not isinstance(fuel_type, FuelType):
                raise Exception("fuel_type is not a FuelType")

            # Checks that the engine size and number of seats are valid
            if not 0 < engine_size < 10000:
                raise Exception("Invalid engine size")
            if not 0 < num_of_seats < 21:
                raise Exception("Invalid amount of seats")

            # Sets the class variables to the input variables
            self.engine_size = engine_size
            self.num_of_seats = num_of_seats
            self.fuel_type = fuel_type

        # Prints any errors if they occur
        except Exception as e:
            print(str(e))

            # Creates a default Vehicle if the inputs are invalid
            print("creating default vehicle")
            self.engine_size = 1000
            self.num_of_seats = 4
            self.fuel_type = FuelType.PETROL

    def drive(self):
        """
        A method that performs the driving functionality of a vehicle
            :return: There is no return
        """

        print("Driving...")
        print(self.fuel_type)


class Car(Vehicle):
    """
    A specific subclass of vehicle that represents a car. No unique attributes / methods.
    """
    pass


class Lorry(Vehicle):
    """
    A specific subclass of vehicle that represents a lorry. It additionally contains
    attributes:
        has_a_trailer: (boolean) If the lorry has a trailer or not

        length: (int) The length of the lorry
    methods:
        __init__(engine_size, num_of_seats, fuel_type, has_a_trailer, length):
        sets the has_a_trailer boolean and length then calls the parent constructor

        wheelie(): A method that docks or undocks the trailer

    """

    def __init__(self, engine_size, num_of_seats, fuel_type, has_a_trailer, length):
        """
                Initialise method that sets the can_wheelie boolean if its valid and calls the parent constructor
                    :param engine_size: (int) representing the engine size in cc

                    :param num_of_seats: (int) representing the number of seats

                    :param fuel_type: (FuelType) A representation the vehicles fuel type

                    :param has_a_trailer: (boolean) If the lorry has a trailer

                    :param length: (int) The length of the lorry

                """

        try:

            # Checks that has_a_trailer is a boolean and the length is an integer
            if not isinstance(has_a_trailer, bool):
                raise Exception("can_wheelie is not a boolean")
            if not isinstance(length, int):
                raise Exception("length is not an int")

            # Checks the length is valid
            if not 3999 < engine_size < 18751:
                raise Exception("Invalid length")

            # Sets the class variables and calls the parent constructor
            self.has_a_trailer = has_a_trailer
            self.length = length
            super().__init__(engine_size, num_of_seats, fuel_type)

        # Prints any errors if they occur
        except Exception as e:
            print(str(e))

            # Creates a default Vehicle if the inputs are invalid
            print("creating default lorry")
            self.has_a_trailer = False
            self.length = 6000
            super().__init__(1000, 4, FuelType.PETROL)

    def dock(self):
        """
        A method that performs the docking functionality
            :return: There is no return
        """
        if self.has_a_trailer:
            self.has_a_trailer = False
        else:
            self.has_a_trailer = True


class Motorbike(Vehicle):
    """
    A specific subclass of vehicle that represents a motorbike. It additionally contains
    attributes:
        can_wheelie: (boolean) If the motorbike can wheelie or not
    methods:
        __init__(engine_size, num_of_seats, fuel_type, can_wheelie):
        sets the can_wheelie boolean and calls the parent constructor

        wheelie(): A method that performs a wheelie

    """

    def __init__(self, engine_size, num_of_seats, fuel_type, can_wheelie):
        """
        Initialise method that sets the can_wheelie boolean if its valid and calls the parent constructor
            :param engine_size: (int) representing the engine size in cc

            :param num_of_seats: (int) representing the number of seats

            :param fuel_type: (FuelType) A representation the vehicles fuel type

            :param can_wheelie: (boolean) If the motorbike can wheelie or not

        """

        try:

            # Checks that can_wheelie is a boolean
            if not isinstance(can_wheelie, bool):
                raise Exception("can_wheelie is not a boolean")

            # Sets the class variables and calls the parent constructor
            self.can_wheelie = can_wheelie
            super().__init__(engine_size, num_of_seats, fuel_type)

        # Prints any errors if they occur
        except Exception as e:
            print(str(e))

            # Creates a default Vehicle if the inputs are invalid
            print("creating default bike")
            self.can_wheelie = False
            super().__init__(1000, 4, FuelType.PETROL)

    def wheelie(self):
        """
        A method that performs a bike wheelie
            :return: There is no return

        """

        # If the bike can wheelie, do a wheelie
        if self.can_wheelie:
            print("doing a wheelie")


class Van(Vehicle):
    """
    A specific subclass of vehicle that represents a van. It additionally contains
    attributes:
        payload: (int) The amount of weight the van can carry

    """

    def __init__(self, engine_size, num_of_seats, fuel_type, payload):
        """
        Initialisation method that sets the payload if its valid and calls the parent constructor
        :param engine_size: (int) representing the engine size in cc

        :param num_of_seats: (int) representing the number of seats

        :param fuel_type: (FuelType) A representation the vehicles fuel type

        :param payload: (int) The amount in kg of payload the van can carry

        """

        try:

            # Validates that the payload is an int between 0 and 2000
            if not isinstance(payload, int):
                raise Exception("payload is not an integer")
            if not 0 < payload < 2000:
                raise Exception("payload is not between 0 and 2000")

            # Sets the payload and calls the parent constructor
            self.payload = payload
            super().__init__(engine_size, num_of_seats, fuel_type)

        # Prints any errors if they occur
        except Exception as e:
            print(str(e))

            # Creates a default Vehicle if the inputs are invalid
            print("creating default van")
            self.payload = 1000
            super().__init__(1000, 4, FuelType.PETROL)


"""
Here you should write all of the tests you want to run for your code
Think about testing invalid inputs as well as boundary testing
"""


# Change if you want to see the existing tests be run
running_existing_tests = True
if running_existing_tests:
    # Testing invalid vehicle inputs
    test = Motorbike("invalid_engine_size", 4, FuelType.DIESEL, True)
    test2 = Motorbike(1000, "invalid_num_of_seats", FuelType.DIESEL, True)
    test3 = Motorbike(1000, 4, "invalid_fuel_type", True)

    # Testing invalid motorbike inputs
    test4 = Motorbike(1000, 4, FuelType.DIESEL, "invalid_can_wheelie")

    # Testing invalid van inputs
    test5 = Van(1000, 4, FuelType.DIESEL, "invalid_payload")

    # Boundary testing engine size
    test6 = Motorbike(999999, 4, FuelType.DIESEL, True)
    test7 = Motorbike(0, 4, FuelType.DIESEL, True)
    test9 = Motorbike(9999, 4, FuelType.DIESEL, True)
    test10 = Motorbike(10000, 4, FuelType.DIESEL, True)
    test11 = Motorbike(-999999, 4, FuelType.DIESEL, True)

    # Boundary testing seat amount
    test12 = Motorbike(1000, -100, FuelType.DIESEL, True)
    test13 = Motorbike(1000, 0, FuelType.DIESEL, True)
    test14 = Motorbike(1000, 20, FuelType.DIESEL, True)
    test15 = Motorbike(1000, 21, FuelType.DIESEL, True)
    test16 = Motorbike(1000, 100, FuelType.DIESEL, True)

    # Boundary testing fuel type
    test17 = Motorbike(1000, 100, FuelType.PETROL, True)
    test18 = Motorbike(1000, 100, FuelType.ELECTRIC, True)
    # Other fuel types not accepted (will be highlighted)

    # Boundary Testing can wheelie
    test19 = Motorbike(1000, 100, FuelType.DIESEL, False)

    # Boundary Testing payload
    test20 = Van(1000, 4, FuelType.DIESEL, -1000)
    test21 = Van(1000, 4, FuelType.DIESEL, 0)
    test22 = Van(1000, 4, FuelType.DIESEL, 1)
    test23 = Van(1000, 4, FuelType.DIESEL, 1999)
    test24 = Van(1000, 4, FuelType.DIESEL, 100000)

    # Testing that vehicle is abstract
    try:
        test25 = Vehicle(1000, 4, FuelType.DIESEL)
    except Exception as e:
        print(str(e))
