from doctor import *
from patient import *
import json


class Appointment:
    def __init__(self):
        self.doctor_detail = {"doctor" : []}
        self.patient_detail = {"patient" : []}
        self.patient_path = 'clinicManagement/patient.json'
        self.doctor_path = 'clinicManagement/doctor.json'
        self.new_doctor = 'new_doctor'
        self.new_patient = 'new_patient'
    
    '''
        - addDoctor(self) takes no argument, collect information from doctor and add him on duty
    '''
    def addDoctor(self):
        id = input('Enter id : ')
        name = input('Enter name: ')
        specialization = input('Enter specialization : ')
        availability = input('Enter availability : ')
        self.new_doctor = Doctor(id,name,specialization,availability)

    '''
        -saveDoctor(self) will ask you whether you want to save detail or not
    '''
    def saveDoctor(self):
        try:
            with open(self.doctor_path,'r') as doctor_file:
                self.doctor_detail = json.load(doctor_file)
        except json.decoder.JSONDecodeError:
            print('Addig 1st doctor !!!')
        finally:
            self.doctor_detail['doctor'].append(self.new_doctor.__dict__)
            with open(self.doctor_path,'w') as doctor_file:
                json.dump(self.doctor_detail, doctor_file, indent=2)
    
    '''
        - addPatient(self) takes no argument, collect information from patient
    '''
    def addPatient(self):
        flag = True
        id = input('Enter id : ')
        name = input('Enter Name : ')
        mobile_no = input('Enter mobile no. : ')
        age = input('Enter age : ')
        appointment_date = input('Appointment date : ')
        while flag:
            appointed_to = input('Enter id number of doctor : ')
            with open(self.doctor_path,'r') as doctor_file:
                self.doctor_detail = json.load(doctor_file)
            for doctor in self.doctor_detail["doctor"]:
                if doctor["id"] == appointed_to:
                    self.new_patient = Patient(id,name,mobile_no,age,appointed_to,appointment_date)
                    flag = False
                    break
                else:
                    flag = True
                    continue
    
    '''
        -savePatient(self) will ask you whether you want to save detail or not
    '''
    def savePatient(self):
        try:
            with open(self.patient_path,'r') as patient_file:
                self.patient_detail = json.load(patient_file)
        except json.decoder.JSONDecodeError:
            print('This is 1st patient !!!')
        finally:
            self.patient_detail["patient"].append(self.new_patient.__dict__)
            with open(self.patient_path,'w') as patient_file:
                json.dump(self.patient_detail,patient_file,indent=2)

    '''
        -searchAvailibility(self,doctor_id,appointment_date) takes doctor id and appointment date as input 
            and return True if doctor is available on that perticular date, else will return false
    '''
    def searchAvailibility(self,doctor_id,appointment_date):
        count = 0
        try:
            with open(self.patient_path,'r') as patient_file:
                self.patient_detail = json.load(patient_file)
                for patient in self.patient_detail['patient']:
                    if patient['appointed_to'] == doctor_id and patient['appointment_date'] == appointment_date:
                        count += 1
        except:
            print('There is no patients, all doctor are available')
        if count < 5:
            return True
        return False

    '''
        -displayDoctor(self) this method will display available doctors in clinic with all details
    '''
    def displayDoctor(self):
        try:
            with open(self.doctor_path,'r') as doctor_file:
                self.doctor_detail = json.load(doctor_file)
            for doctor in self.doctor_detail['doctor']:
                print('----',doctor['name'],'----')
                for key,detail in doctor.items():
                    print(key,':',detail)
        except json.decoder.JSONDecodeError:
            print('No doctor available in clinic')
        

