from appointment import *

class ClinicManagement:
    appoint = Appointment()
    while True:
        print('-----------------------Clinic Management--------------------------')
        print('\n1.Add doctor to clinic \n2.Check availibility of perticular doctor \n3.Chech available doctors in clinique \n4.Quit')
        try:
            user_input = int(input('Enter choice : '))
        except ValueError:
            print('Enter right choice and try again')
            continue
        if user_input == 1:
            appoint.addDoctor()
            try:
                save = int(input('Enter 1 to save'))
            except ValueError:
                print('Enter right choice and try again')
                continue
            if save == 1:
                appoint.saveDoctor()
        if user_input == 2:
            doctor_id = input('Enter doctor id : ')
            print('Enter right choice and try again')
            appointment_date = input('Enter appointment date : ')
            availibility = appoint.searchAvailibility(doctor_id,appointment_date)
            if availibility:
                print('Available')
                try:
                    choice = int(input('To take appointment press 1'))
                except ValueError:
                    print('Enter right choice and try again')
                    continue
                if choice == 1:
                    appoint.addPatient()
                    save = int(input('Enter 1 to save'))
                    if save == 1:
                        appoint.savePatient()
            else:
                print('Not available')
                print('You can take appointment on next day')
        if user_input == 3:
            appoint.displayDoctor()
        if user_input == 4:
            break
        print('--------------------END----------------------')