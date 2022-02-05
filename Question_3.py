# Here I made a dictionary containing the cars Mr. Omondi started with and their specifications.

Cars = {"Sienna": {"Model": "SE245", "Year_Released": 2012, "Year_Bought": 2015, "Money_made": 20000,
                   "Plate_Number": "ABC-1234", "No._of _times_rented": 40},
        "ford": {"Model": "SE255", "Year_Released": 2019, "Year_Bought": 2020, "Money_made": 120000,
                 "Plate_Number": "ABC-1224", "No._of _times_rented": 26},
        "Toyota": {"Model": "SE245", "Year_Released": 2011, "Year_Bought": 2015, "Money_made": 10000,
                   "Plate_Number": "ABC-1114", "No._of _times_rented": 30},
        "Lamborghini": {"Model": "SE245", "Year_Released": 2014, "Year_Bought": 2015, "Money_made": 200000,
                        "Plate_Number": "ABC-9934", "No._of _times_rented": 10},
        "Porsche": {"Model": "SE532", "Year_Released": 2009, "Year_Bought": 2010, "Money_made": 100000,
                    "Plate_Number": "ABC-5678", "No._of _times_rented": 52}}

# This code gives the Mr. Omondi the ability to pick what operation he wants to go through with which will then\n
# simultaneously call the function attached to the option as you can see in line 65-74.


Option = int(input('Kindly pick the Operation You want \n'
                   "Press 1 if you want to rent car\n"
                   "Press 2 if you want to add car\n"
                   "press 3 if you want to delete a car\n"
                   "press 4 if you want to know the number of times the car has been rented\n"
                   "press 5 if you want to know the money made"
                   ))

# The functions below show what operations would be carried out as soon as Mr. Omondi picks either one of the options.


def rent(cars):
    Name_of_car = input("Kindly input the name of the car you want to rent")
    amount = int(input("How much do you want to rent it out?"))
    cars[Name_of_car]["Money_made"] += amount
    cars[Name_of_car]["No._of _times_rented"] += int(1)
    print(cars[Name_of_car])


def add(cars):
    New_car = input("Kindly input the name of your car")
    cars[New_car] = {}
    Cars[New_car]["Model"] = input("Kindly input the Model of the car")
    cars[New_car]["Year_Released"] = input("Kindly input the year of release of the car")
    cars[New_car]["Year_Bought"] = input("Kindly input the year the car was bought")
    cars[New_car]["Money_made"] = input("Kindly input the amount of money the car has made")
    cars[New_car]["Plate_Number"] = input("Kindly input the plate number of the car")
    cars[New_car]["No._of_times_rented"] = input("Kindly input the number of times the car has been rented")
    print(Cars)


def remove(cars):
    Name_of_car = input("Kindly input the name of cars you want to delete")
    del cars[Name_of_car]
    print(cars)


def number_of_times_rented(cars):
    Name_of_car = input("Kindly input the name of the car")
    print(cars[Name_of_car]["No._of _times_rented"])


def money_made(cars):
    Name_of_car = input("Kindly put in the name of the car")
    print(cars[Name_of_car]["Money_made"])


if Option == 1:
    rent(Cars)
elif Option == 2:
    add(Cars)
elif Option == 3:
    remove(Cars)
elif Option == 4:
    money_made(Cars)
else:
    number_of_times_rented(Cars)
