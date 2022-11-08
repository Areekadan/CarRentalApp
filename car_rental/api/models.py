from tkinter import CASCADE
from unittest.mock import DEFAULT
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=5, blank=True)

    def __str__(self):
         return self.street_number + " " + self.street_name + " " + self.city 


class BranchPhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)
    branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)


class CarType(models.Model):
    car_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    daily_cost = models.FloatField(max_length=10)
    weekly_cost = models.FloatField(max_length=10)
    monthly_cost = models.FloatField(max_length=10)
    late_fee = models.FloatField(max_length=10)
    change_branch_fee = models.FloatField(max_length=10)

    def __str__(self):
        return self.description


class Car(models.Model):
    # choices for status
    STATUS_CHOICES = (('Available', 'Available'),('Not Available', 'Not Available'))

    car_id = models.AutoField(primary_key=True)
    car_type = models.ForeignKey(CarType, related_name='car_type', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, related_name='car_branch', default='', on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=15)
    colour = models.CharField(max_length=15)
    license_plate = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    mileage = models.FloatField(max_length=25)

    def __str__(self):
        return self.license_plate


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # Password and number will now temporarily be chars. Might need to hash them later
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    salary = models.IntegerField()
    rank = models.CharField(max_length=30)
    DOB = models.DateField()
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=5, blank=True)
    works_at = models.ForeignKey(Branch, models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name

    


class EmployeePhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    drivers_license = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    DOB = models.DateField()
    gold_member = models.BooleanField()
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name


class CustomerPhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15)


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    date_from = models.DateField()
    date_to = models.DateField()
    date_returned = models.DateField()
    total_cost = models.FloatField(max_length=10)
    car = models.ForeignKey(Car, models.SET_NULL, null=True, default="")
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True, default="")
    employee_given_by = models.ForeignKey(Employee, models.SET_NULL, null=True, default="")
    branch_came_from = models.ForeignKey(Branch, related_name='%(class)s_came_from', on_delete=models.SET_NULL, null=True, default="")
    branch_goes_to = models.ForeignKey(Branch, related_name='%(class)s_goes_to', on_delete=models.SET_NULL, null=True, default="")
    requested_car_type = models.ForeignKey(CarType, models.SET_NULL, null=True, default="")
