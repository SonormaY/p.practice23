import re
import datetime
from A5.Vaccine import Vaccine

class Validator:
    def is_integer(input_string):
        try:
            int(input_string)
            return True
        except ValueError:
            return False     
    def validate_ID(func):
        def wrapper(self, value):
            if not Validator.is_integer(value) or int(value) < 0:
                print("ID is not integer or not positive")
                return
            else:
                return func(self, value)
        return wrapper 
    def validate_name(func):
        def wrapper(self, value):
            if not re.match(r"^[A-Za-z]+$", value):
                print("Name must contain only letters")
            else:
                return func(self, value)
        return wrapper
    def validate_date(func):
        def wrapper(self, value):
            try:
                date = datetime.datetime.strptime(value, "%d-%m-%Y")
            except ValueError as e:
                print(e)
            else:
                return func(self, date)
        return wrapper
    def validate_time(func):
        def wrapper(self, value):
            try:
                time = datetime.datetime.strptime(value, "%H:%M")
            except ValueError as e:
                print(e)
            else:
                return func(self, time)
        return wrapper
    def validate_patient_phone(func):
        def wrapper(self, value):
            if not re.match(r"^[0-9]{10}$", value):
                print("Phone Number must contain only numbers and can only be 10 digits long")
            else:
                return func(self, value)
        return wrapper
    def validate_vaccine(func):
        def wrapper(self, value):
            try:
                vaccine = Vaccine(value)
            except ValueError as e:
                print(e)
            else:
                return func(self, vaccine)
        return wrapper
    def validate_type(func):
        def wrapper(self, type, value):
            if value in ["id", "patient_name", "patient_phone", "vaccine", "date", "start_time", "end_time"]:
                return func(self, type, value)
            else:
                print("Type isn't valid")
                return
        return wrapper
            
    def input_integer(message):
        while True:
            user_input = input(message)
            if Validator.is_integer(user_input):
                return int(user_input)
            else: print("Enter a number")
            
    def validate_range(min_value, max_value):
        if min_value > max_value:
            raise ValueError("Wrong bounds")