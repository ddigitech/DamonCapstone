# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator
# import datetime

# Create your models here.


# Car Make model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name




class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    dealer_id = models.IntegerField(null=True)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    SPORT = "Sport"
    COUPE = "Coupe"
    MINIVAN = "Mini"
    VAN = "Van"
    PICKUP = "Pickup"
    TRUCK = "Truck"
    BIKE = "Bike"
    SCOOTER = "Scooter"
    OTHER = "Other"
    CAR_CHOICES = [(SEDAN, "Sedan"), (SUV, "SUV"), (WAGON, "Station wagon"), (SPORT, "Sports Car"),
                   (COUPE, "Coupe"), (MINIVAN, "Mini van"), (VAN,
                                                             "Van"), (PICKUP, "Pick-up truck"),
                   (TRUCK, "Truck"), (BIKE, "Motor bike"), (SCOOTER, "Scooter"), (OTHER, 'Other')]
    model_type = models.CharField(
        null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)

    YEAR_CHOICES = []
    for r in range(1969, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.model_type



# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
