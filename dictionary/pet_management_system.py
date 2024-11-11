# a dictionary to hold all records
records = {}
#patient_number = 123

def menu_selection():    
    menus = [
        "Add a new pet",
        "Remove a pet",
        "List all pets",
        "List a specific pet based on patient number",
        "List all data (patient #, type, name, age) for all pets",
        "Exit"
    ]

    while True:
        print("Menu\n==========")
        for i in range(len(menus)):
            print(f"{i+1}. {menus[i]}")
        
        choice = input("Enter a selection:")
        if not choice.isdigit():
            print("Your choice must be a digit")
            continue

        choice = int(choice)
        menu_length = len(menus)
        if choice < 1 or choice > menu_length:
            print(f"Your choice must be in the range 1-{menu_length}")
            continue

        return choice

def add_new_pets():
    while True:
        #prompt the user for the pet type
        pet_type = input("Enter the type of pet:")
        #prompt the user for the pet name
        name = input("Enter the pet's name:")
        #ensure that the pet name is not empty
        if len(name) == 0:
            print("Pet name cannot be empty")
            continue
        #prompt for the age
        age = input("Pet age:")
        #ensure that age is digit and not negative
        if not age.isdigit() or int(age) < 0:
            print("Age must be a positive digit")
            continue
        #convert from string to int
        age = int(age)

        #prompt for patient number
        patient_number = int(input("Patient number:"))

        #create the patient record
        patient = {
            "name":name,
            "type":pet_type,
            "age":age,
            "patient_number":patient_number
        }

        #store the record using the patient id as key
        records[str(patient_number)] = patient
        #notify the user that the patient was added
        print(f"The record for the patient {patient} was successfully created")
        break # quit adding pets
    
def remove_a_pet():
    #prompt for patient number
    patient_number = input("Enter the patient number:")
    #ensure that the patient number exist in the key
    if patient_number in records:
        del records[patient_number] #delete record if the key was found
        print(f"The record for {patient_number} was successfully deleted")
    else:
        #inform the user if the key was not found
        print(f"No patient number:{patient_number} was found")

def list_all_pets():
    #if there are no data then we show no data
    if len(records) == 0:
        print("No pet data to show")
    else:
        #show all pets naemes
        for patient_number in records:
            patient = records[patient_number] #this retrives a patient dictonary
            print(patient["name"])

def list_all_pets_data():
    if len(records) == 0:
        print("No pet data to show")
    else:
        #show all pet records dictionary
        for patient_number in records:
            patient = records[patient_number]
            print(patient)
            print()

def list_pet_based_on_patient_number():
    if len(records) == 0:
            print("No pet data to show")
    patient_number = input("Enter the patient number:")
    if patient_number in records:
        patient = records[patient_number]
        print(patient)
    else:
        print(f"No patient number:{patient_number} was found")
    
        
        


def main():
    while True:
        choice = menu_selection()
        if choice == 1:
            add_new_pets()
        elif choice == 2:
            remove_a_pet()
        elif choice == 3:
            list_all_pets()
        elif choice == 4:
            list_pet_based_on_patient_number()
        elif choice == 5:
            list_all_pets_data()
        else:
            print("Thank you for using Rochester Pet Vet System... bye")
            exit(0)
        



main()
    
