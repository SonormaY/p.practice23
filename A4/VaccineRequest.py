from validation import Validator
from A4.Vaccine import Vaccine
import datetime

class VaccineRequest:
    def __init__(self, ID = None, patient_name = None, patient_phone = None, vaccine = None, date = None, start_time = None, end_time = None):
        self.ID = ID
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    @Validator.validate_date
    def set_date(self, date):
        self.date = date

    @Validator.validate_time
    def set_start_time(self, time):
        self.start_time = time

    @Validator.validate_time
    def set_end_time(self, time):
        self.end_time = time

    @Validator.validate_ID
    def set_id(self, id):
        self.ID = id

    @Validator.validate_name
    def set_patient_name(self, name):
        self.patient_name = name

    @Validator.validate_patient_phone
    def set_patient_phone(self, phone):
        self.patient_phone = phone

    @Validator.validate_vaccine
    def set_vaccine(self, vaccine):
        self.vaccine = vaccine
            

    def __str__(self):
        return f"ID: {self.ID}\n" \
               f"Patient name: {self.patient_name}\n" \
               f"Phone number: +38{self.patient_phone}\n" \
               f"Vaccine: {self.vaccine.value}\n" \
               f"Date: {datetime.datetime.strftime(self.date, '%d-%m-%Y')}\n" \
               f"Start time: {datetime.datetime.strftime(self.start_time, '%H:%M')}\n" \
               f"End time: {datetime.datetime.strftime(self.end_time, '%H:%M')}\n"
        
    def __eq__(self, other):
        return (self.id == other.id and
                self.patient_name == other.patient_name and
                self.patient_phone == other.patient_phone and
                self.vaccine == other.vaccine and
                self.date == other.date and
                self.start_time == other.start_time and
                self.end_time == other.end_time)
    
    def console_input():
        temp = VaccineRequest()
        
        while temp.ID is None:
            temp.set_id(input("Enter ID: "))
        while temp.patient_name is None:
            temp.set_patient_name(input("Enter Patient Name: "))
        while temp.patient_phone is None:
            temp.set_patient_phone(input("Enter Patient Phone: "))
        while temp.vaccine is None:
            temp.set_vaccine(input("Enter Vaccine type: "))
        while temp.date is None:
            temp.set_date(input('Enter a date in DD-MM-YYYY format: '))
        while temp.start_time is None:
            temp.set_start_time(input("Enter start time in HH:MM format: "))
        check = False
        while temp.end_time is None or check:
            temp.set_end_time(input("Enter end time in HH:MM format: "))
            if temp.end_time <= temp.start_time:
                check = True
                print("End time cannot be less or equal than start time")
            else:
                check = False

        return temp

    def contains(self, value):
        value = str(value)
        if value in str(self.ID) \
                or value in self.patient_name \
                or value in self.patient_phone \
                or value in self.vaccine.value \
                or value in datetime.datetime.strftime(self.date, "%d-%m-%Y") \
                or value in datetime.datetime.strftime(self.start_time, "%H:%M") \
                or value in datetime.datetime.strftime(self.end_time, "%H:%M") :
            return True
        else: return False

    @Validator.validate_type
    def edit(self, type, value):
        if type == "ID" and Validator.is_integer(value):
            self.set_id(value)
        elif type == "patient_name":
            self.set_patient_name(value)
        elif type == "patient_phone":
            self.set_patient_phone(value)
        elif type == "vaccine":
            self.set_vaccine(value)
        elif type == "date":
            self.set_date(value)
        elif type == "start_time":
            if value >= self.end_time:
                print("Start time cannot be greater or equal than end time")
                return
            else:
                self.set_start_time(value)
        elif type == "end_time":
            if value <= self.start_time:
                print("End time cannot be less or equal than start time")
                return
            else:
                self.set_end_time(value)

    