import re

# Predefined variables
games_records = [] #this will keep a list of all game sales

# COMMENT OUT BEFORE SUBMIT - THIS MAKE TESTING EASY INSTEAD OF DOING A EMPTY RECORD EACH TIME THE PROGRAM RUN
# games_records = [
#     {
#         "name":"Punk",
#         "platform":"PC", 
#         "date":"10-10-2024",
#         "cost":10
#     },
#     {
#         "name":"FIFA",
#         "platform":"PC", 
#         "date":"10-10-2024",
#         "cost":10
#     } ,
#     {
#         "name":"TF2",
#         "platform":"XBOX", 
#         "date":"10-10-2024",
#         "cost":10
#     } 
# ]

# Predefined function
def display_menu():
    print("Menu Options:")
    print("1. Create a new sale")
    print("2. Remove a record")
    print("3. Show all sales")
    print("4. Filter sale by platform")
    print("5. Exit")
    
# Predefined function
def menu_selection():
    display_menu()
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            
            return choice
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# functions to be completed by the student goes here
#This function will use regex to ensure that the date is in the format MM-DD-YYYY. 
def is_valid_date(date):
    #the pattern is MM-DD-YYYY
    date_format_pattern = r'\d{2}-\d{2}-\d{4}'
    result = re.match(date_format_pattern,date)
    #there is no match we will get a none
    if result == None:
        return False
    #otherwise we return true
    return True

def create_sale():
    #prompt the user for informations
    #name of the game, game platform
    name_of_game = input("Enter the name of the game:")
    game_platform = input("Enter the game platform:")
    #you must validate that the date is in an acceptable format. If it is not, re-prompt the user for the date information. 
    while True:
        date_of_sale = input("Enter the date of the sale(MM-DD-YYYY):")
        if is_valid_date(date_of_sale) == True:
            break

        #if we get here then the date is not valid
        print("Invalid date format. Date must be MM-DD-YYYY")
    
    cost_of_the_game = float(input("Enter the cost of the game:")) 

    #create the record of the game sale
    sales_record = {
        "name":name_of_game,
        "platform":game_platform, 
        "date":date_of_sale,
        "cost":cost_of_the_game
    } 

    #add the record to the list of game records
    games_records.append(sales_record)

    #let the user know the record was successfully created
    print(f"{sales_record} was successfully created")

def remove_record():
    #prompt the user for the name and platform of the game sale record to remove from the list 
    name_of_game = input("Enter the name of the game:")
    game_platform = input("Enter the game platform:")

    #we setup match to false before we start searching
    match_found = False

    #remember record is a dictionary with {name:<name>, platform:<platform>, date:<date>, cost:<cost>} 
    for record in games_records:
        #make sure it match the name and platform
        if record["name"] == name_of_game and record["platform"] == game_platform:
            #if we get a match then we can remove it
            games_records.remove(record)
            #update match found to true
            match_found = True
            #let the user know that the record was deleted
            print(f"{record} was successfully deleted")
            break # exit the loop as we already find our match, no need to check everything else
    
    #show for no match
    if match_found == False:
        print(f"No match was found for game name:{name_of_game} with platform:{game_platform}")
    
def show_sales():
    #we can use the len to let us know if something is empty
    if len(games_records) == 0:
        print("The list is currently empty.")
    else:
        #print(games_records)
        #OR clean it up a little
        for record in games_records:
            print(record)

def filter_by_platform_rec(record_list, target, filtered_list):
    #if we get a empty record_list then we want all matching filtered_list
    if len(record_list) == 0:
        return filtered_list
    
    #We will always look at the first record
    record = record_list[0]
    #check if the platform match the target
    if record["platform"] == target:
        #if it match, we add it to the filtered_list
        filtered_list.append(record)
    
    #we will now shorten the list by starting at 1: to the end so that we dont do the 0 index
    record_list = record_list[1:]
    
    #recursively perform the search and append in filter list as need
    return filter_by_platform_rec(record_list, target, filtered_list)

def filter_by_platform():
    target_platform = input("Enter the platform to filter by:")
    #The initial filtered_list should be an empty list.
    filtered_list = []
    #Call the filter_by_platform_rec(record_list, target, filtered_list) to recursively search the game_records.
    filter_by_platform_rec(games_records, target_platform, filtered_list)

    #no match if the filter list is 0
    if len(filtered_list) == 0:
        print(f"No match found for {target_platform}")
    else:
        #print(filtered_list)
        # OR clean up
        for record in filtered_list:
            print(record)

def main():
    while True:
        try:
            selection = menu_selection()
            if selection == 1:
                create_sale()
            elif selection == 2:
                remove_record()
            elif selection == 3:
                show_sales()
            elif selection == 4:
                filter_by_platform()
            else:
                print("Thank you for using this platform")
                print("Goodbye.....")
                break
        except:
            print("Invalid action!")
    

if __name__ == "__main__":
    main()

#dummy tests
# print(is_valid_date("01-01-2024"))
# print(is_valid_date("01-01-202"))

# create_sale()
#remove_record()
# show_sales()

# matches = []
# filter_by_platform_rec(games_records, "XBOX", matches)

# print(matches)

# filter_by_platform()