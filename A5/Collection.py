from validation import Validator
from A5.VaccineRequest import VaccineRequest
from A5.Vaccine import Vaccine
from A5.Observer import Observer, Event
from A5.Logger import Logger
import datetime

class Collection:
    def __init__(self, collection = []):
        self.collection = collection
        self.observer = Observer()

    def print(self):
        if self.collection == []:
            print("Collection is empty")
        for i in range(len(self.collection)):
            print(self.collection[i])
            print("--------------------")
    
    def clear(self, out_file = "out"):
        print("Clearing Complete")
        self.collection = []
        event = Event("clear", [f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] Cleared collection\n", out_file])
        event.trigger(self.observer)

    def add_element_console(self, out_file = "out"):
        temp = VaccineRequest.console_input()
        for element in self.collection:
            if element.ID == temp.ID:
                print(f"ID{element.ID} already exists")
                return
        self.collection.append(temp)
        event = Event("add", f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] Added element with ID{temp.ID}\n")
        event.trigger(self.observer)
        
    def add_element(self, string, out_file = "out"):
        temp = string.split(" ")
        if not Validator.is_integer(temp[0]):
            print("ID must be a number")
            return
        else: 
            temp_id = temp[0]
        for element in self.collection:
            if element.ID == temp_id:
                print(f"ID{element.ID} already exists")
                return
        temp_request = VaccineRequest()
        temp_request.set_id(temp[0])
        temp_request.set_patient_name(temp[1])
        temp_request.set_patient_phone(temp[2])
        temp_request.set_vaccine(temp[3])
        temp_request.set_date(temp[4])
        temp_request.set_start_time(temp[5])
        temp_request.set_end_time(temp[6])
        if temp_request.ID is None\
            or temp_request.patient_name is None\
            or temp_request.patient_phone is None\
            or temp_request.vaccine is None\
            or temp_request.date is None\
            or temp_request.start_time is None\
            or temp_request.end_time is None:
            print("Not all fields are correct")
        else:
            self.collection.append(temp_request)
            event = Event("add", [f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] Added element with ID{temp_request.ID}\n", out_file])
            event.trigger(self.observer)

    def read_from_file(self, file_name,  out_file = "out", position = None):
        if out_file is None:
            out_file = "out"
        file = open(file_name, 'r')
        if position is None:
            temp = file.read().split("\n")
            for n in temp:
                self.add_element(n, out_file)
        else:
            content = file.readlines()
            try:
                self.add_element(content[position-1].strip(), out_file)
            except IndexError:
                print("Wrong position")

    def find_elements(self, value):
        arr = []
        for element in self.collection:
            if element.contains(value):
                arr.append(element)
        
        return arr
    
    def sort_data(self, type):
        if type == "ID":
            self.collection.sort(key=lambda x: x.ID)
        elif type == "patient_name":
            self.collection.sort(key=lambda x: x.patient_name)
        elif type == "patient_phone":
            self.collection.sort(key=lambda x: x.patient_phone)
        elif type == "vaccine":
            self.collection.sort(key=lambda x: x.vaccine)
        elif type == "date":
            self.collection.sort(key=lambda x: x.date)
        elif type == "start_time":
            self.collection.sort(key=lambda x: x.start_time)
        elif type == "end_time":
            self.collection.sort(key=lambda x: x.end_time)
        else:
            print("Sort type isn't valid")
            return self.sort_data(input("Enter Sort Type: id/patient_name/patient_phone/vaccine/date/start_time/end_time"))
        
    def delete_by_id(self, ID, out_file = "out"):

        if not Validator.is_integer(ID) or int(ID) < 0:
            print("Enter valid number")
        else:
            for i in range(len(self.collection)):
                if self.collection[i].ID == int(ID):
                    del self.collection[i]
                    event = Event("delete", [f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] Deleted element with ID{self.collection[i].ID} \n", out_file])
                    event.trigger(self.observer)
                    return
            print("Element not found")

    def edit_by_id(self, ID, type, value, out_file = "out"):
        if not Validator.is_integer(ID) or int(ID) < 0:
            print("Enter valid number")
        else:
            for i in range(len(self.collection)):
                if self.collection[i].ID == int(ID):
                    file = open(out_file, 'a')
                    file.write(f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}] Edited element with ID{self.collection[i].ID} \n")
                    self.collection[i].edit(type, value)
                    return
            print("Element not found")
                
    def print_log(log):
        file = open(log, 'r')
        print(file.read())

    def delete_by_index(self, pos, out_file = "out"):
        if not Validator.is_integer(pos):
            print("Enter valid number")
        else:
            del self.collection[int(pos)-1]

    def delete_in_bounds(self, start_pos, end_pos, out_file = "out"):
        Validator.validate_range(start_pos, end_pos)
        for i in range(start_pos, end_pos + 1):
            self.delete_by_index(start_pos, out_file)