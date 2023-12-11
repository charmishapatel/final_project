# Assignment: Project: Classes - CPRG-216-Q
#  
# A hair salon appointment management system is made using this python code, 
# which makes use of the Appointment class. Functions like appointment scheduling, cancellation, location, 
# and printing are available through the system. Initializing a weekly schedule with available time 
# slots is done via the create_weekly_calendar function. By reading appointment data from a file, the
# load_scheduled_appointments function counts the numeber of appointments already scheduled. The primary function of the program controls
# its main interface, which is a menu that allows user-inputted actions. Encapsulating attributes such 
# as client name, phone number, day of the week, start time hour, and appointment type, instances of the 
# Appointment class represent appointments. 
#
# Inputs:
#     load_choice
#     file_name
#     option
#     day
#     start_hour_str
#     client_name
#     client_phone
#     appt_type_str
#     start_hour
#     saving_data
# Output:
#     printing the default start statement
#     aks the user to input selected load_choice
#     asks the user to print file_name
#     if wrong then re-enter file_name
#     load_scheduled_appointments(file_name, calendar) function prints no of previously scheduled appointments
#     print_menu() function loads the menu options and ask the user to enter one of the menu option
#     if option selected is [1] then it asks the user about the day, start hour, name, phone number and type of appointment
#     and appointment booked statement is printed  
#     if option selected is [3] then it ask the user to input day of the week and prints the available appointments on that day
#     it also prints the start and end time and type of appointment available
#     if option selected is [2] then it asks user's name and prints the booked appointments for that name 
#     with the name of the client, phone number, day, start and end time and type of appointment 
#     if option selected is [4] it asks user to enter the day and start hour of the appointment to be cancelled
#     if option selected is [9] it exits the system and the loop stops running 
#     at the end it asks user if he/she wants to save the a above schedueld appointments in a file  
#     if user enter yes then ask the name of the file in which it is to be saved
#     if the filename already exists the asks teh user to overwrite if yes the it overwrites 
#     if no then ask user to enter new filename
#     atlast prints the goodbye statement
#    
# Processing: Calculations:
#     create_weekly_calendar
#     load_scheduled_appointments
#     checking_booked_slot
#     print_menu
#     find_appointment_by_time
#     show_appointments_by_name
#     show_appointments_by_day
#     save_scheduled_appointments
#     main


# Author Charmisha Patel, Harshdeep Kaur, Prabhjot Kaur
# Version 2023-12-10




import appointment as ap

def create_weekly_calendar():
    calendar = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for day in days_of_week:
        for hour in range(9, 17):
            appointment = ap.Appointment(day, hour)
            calendar.append(appointment)

    return calendar

def load_scheduled_appointments(filename, calendar):
        count = 0
        opening_file = open(filename, 'r')
        lines = opening_file.readlines()
        for line in lines:
            values = line.strip().split(',')
            day_of_week = values[3]
            start_time_hour = int(values[4])
            appointment = find_appointment_by_time(calendar, day_of_week, start_time_hour)
            if appointment:
                appointment.schedule(values[0], values[1], int(values[2]))
                count +=1
        print(f'{count} previously scheduled appointments have been loaded')


def checking_booked_slot(calendar, day, start_hour):
    for appointment in calendar:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour and appointment.get_client_name() != "":
            return True
    return False

def print_menu():
    print("\n")
    print("Jojo's Hair Salon Appointment Manager")
    print("=" * 37)
    print("1) Schedule an appointment")
    print("2) Find appointment by name")
    print("3) Print calendar for a specific day")
    print("4) Cancel an appointment")
    print("9) Exit the system")
    

    return input("Enter your selection: ")

def find_appointment_by_time(calendar, day, start_hour):
    for appointment in calendar:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment
    return None

def show_appointments_by_name(calendar, name):
    for appointment in calendar:
        if name.lower() in appointment.get_client_name().lower():
            print(appointment)
    
def show_appointments_by_day(calendar, day):

    print(f"Appointments for {day.capitalize()}\n")
    
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
   
    print("-" * 80)

    for appointment in calendar:
        if appointment.get_day_of_week().lower() == day.lower():
            client_name = appointment.get_client_name() if appointment.get_client_name() else " "
            client_phone = appointment.get_client_phone() if appointment.get_client_phone() else " "
            start_time = f"{appointment.get_start_time_hour():02d}:00"
            end_time = f"{appointment.get_start_time_hour() + 1:02d}:00"  
            appt_type = appointment.get_appt_type_desc() if appointment.get_client_name() else "Available"
            print(f'{client_name:16} {client_phone:>15} {day.capitalize():>8} - {start_time:>8} {end_time:>9} {appt_type:>20}')

def save_scheduled_appointments(calendar, file_name):
    count = 0
 
    if file_name == "appointments1.csv":
        yes_no = input('File already exist. Do you want to overwrite it (Y/N): ').upper()
        if yes_no == 'N':
            file_name = input('Enter file name: ')
            opening_new_file = open(file_name, 'w')
            for appointment_obj in calendar:
              if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
            print(f'{count} scheduled appointments have been saved')

        else:
             opening_new_file = open(file_name, 'w')
             for appointment_obj in calendar:
               if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
             print(f'{count} scheduled appointments have been saved')

    else:
        opening_new_file = open(file_name, 'w')
        for appointment_obj in calendar:
            if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
        print(f'{count} scheduled appointments have been saved')



def main():
    calendar = create_weekly_calendar()
    
 
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_choice = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
    if load_choice == 'y':
         file_name = input("Enter appointment filename: ")
         if file_name == 'appointments1.csv':
           load_scheduled_appointments(file_name, calendar)
         else:
          file_name = input("File not found. Re-enter appointment filename: ")
          load_scheduled_appointments(file_name, calendar)
    option = print_menu()

    while option != '9':
        match option:
            case '1':
                print("\n** Schedule an appointment **")
                day = input("What day: ").capitalize()
                start_hour_str = input("Enter start hour (24 hour clock): ")
                if start_hour_str.isdigit() and 0 <= int(start_hour_str) <= 23:
                   start_hour = int(start_hour_str)
                   appointment = find_appointment_by_time(calendar, day, start_hour)
                
                   if checking_booked_slot(calendar, day, start_hour):
                      print("Sorry that time slot is booked already!")
                      option = print_menu()
                   elif appointment:
                      client_name = input("Client Name: ").capitalize()
                      client_phone = input("Client Phone: ")
                      print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")

                      appt_type_str = input("Type of Appointment: ")
                      if appt_type_str in ['1', '2', '3', '4']:
                        appt_type = int(appt_type_str)
                        appointment.schedule(client_name, client_phone, appt_type)
                        print(f"OK, {client_name}'s appointment is scheduled!")
                        option = print_menu()
                      else:
                        print("Sorry that is not a valid appointment type!")
                        option = print_menu()
                   else:
                    print("Sorry that time slot is not in the weekly calendar!")
                    option = print_menu()
            
            case '2':
                print("\n** Find appointment by name **")
                client_name = input("Enter Client Name: ").capitalize()
                found_appointments = False
                print("Appointment for "+ client_name)  
                print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name","Phone", "Day", "Start", "End", "Type"))
                # print(f"\n{'Client Name'.ljust(20)} {'Phone'.ljust(15)} {'Day'.ljust(10)} {'Start'.ljust(10)} {'End'.ljust(10)} {'Type'}")
                print("-" * 80)
                for appointment in calendar:
                  
                  if client_name in appointment.get_client_name().capitalize():
                  
                    print(appointment)
                    
                    found_appointments = True
                
                if not found_appointments:
                    
                    print("No appointments found.")
                 
                option = print_menu()
            case '3':
                print("\n** Print calendar for a specific day **")
                day = input("Enter day of week: ")
                show_appointments_by_day(calendar, day)
                option = print_menu()
            case '4':
                    print("\n** Cancel an appointment **")
                    day = input("What day: ").capitalize()
                    start_hour = int(input("Enter start hour (24 hour clock): "))
                    appointment = find_appointment_by_time(calendar, day, start_hour)

                    if appointment and appointment.get_client_name():  
                       client_name = appointment.get_client_name()  
                       appointment.cancel()
                       print(f"Appointment: {day} {start_hour:02d}:00 - {start_hour + 1:02d}:00 for {client_name} has been cancelled!")
                       option = print_menu()
                    elif appointment:  
                       print(f"That time slot isn't booked and doesn't need to be cancelled")
                       option = print_menu()
                    else:  
                       print("Sorry, that time slot is not in the weekly calendar!")
                       option = print_menu()

    print('\n** Exit the system **')
    saving_data = input('Would you like to save all scheduled appointments to a file (Y/N)?').upper()
    file_name = input('Enter appointment filename: ')
    if saving_data != 'N':
        save_scheduled_appointments(calendar, file_name)
        print('Good Bye')
    else:
        print('Good Bye!')

if __name__ == "__main__":
    main()
