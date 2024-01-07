# Import functionalities from the main file
from main import *

# Display Menu
def displayMenu():
    print('\nWelcome to Car Park🙂!')
    print('\t1. Enter the car park')  
    print('\t2. Exit the car park')
    print('\t3. View available parking spaces')
    print('\t4. Query parking record by ticket number')
    print('\t5. Quit')


# Show details of the record
def displayRecord(record):
    print('These are the details of your ticket')
    print(f"\t\tTicket Number' : '{record['TicketNumber']}'")
    print(f"\t\tVehicle Number' : '{record['VehicleNumber']}'")
    print(f"\t\tTime Entry' : '{record['TimeEntry']}'")
    print(f"\t\tTime Exit : '{record['TimeExit']}'")
    print(f"\t\tParking Space' : '{record['ParkingIdentifier']}'")
    print(f"\t\tCost' : '{'£' if record['Cost'] != 'None' else ''}{record['Cost']}'")

    
# Enter Car Park
def enteringCarPark():
    print('\nYou are entering the car park!')
    print(CAR_NUMBER_INSTRUCTIONS)
    car_number = input('\tEnter your car number: ')
    
    # Add car to the car park
    newRecord = addCar(car_number)
    # Check if the car addition was successful.
    if newRecord: 
        print('\nThe car has successfully entered the car park!')
        displayRecord(newRecord)
        print(f'\t\tAvailable Parking Spaces: {len(getAvailableParkingSpace())}')
        
    #Error Message
    else:
        print('The car number is not valid / Parking space is full / Car is already present\n')
    
    
# Exit Car Park
def exitingCarPark():
    print('\nYou are exiting the car park!')
    print(CAR_NUMBER_INSTRUCTIONS)
    car_number = input('\tEnter your car number: ')
    
    # Remove car to the car park
    newRecord = removeCar(car_number)
    
    # Check if the car removal was successful.
    if newRecord: 
        print('\nThe car has successfully exited the car park!')
        displayRecord(newRecord)
        print(f'\t\tAvailable Parking Spaces: {len(getAvailableParkingSpace())}')
        
    #Error Message
    else:
        print('The car number is not valid / Car is not present\n')
        
        
# Show available parking spaces
def showAvailParkingSpaces():
    availPKSpace = getAvailableParkingSpace()
    print('\nThese are the available parking spaces!!!\n')
    print('Available Spaces: '+ ', '.join(availPKSpace))
    print(f'\nNumber of Available Parking Spaces: {len(availPKSpace)}')


# Query ticket number
def queryTicketNumber():
    ticket_number = input('\tEnter your ticket number: ').upper().strip()
    
    # Remove car to the car park
    newRecord = getTicket(ticket_number)
    print()
    
    # Check if the car removal was successful.
    if newRecord: 
        displayRecord(newRecord)
        
    #Error Message
    else:
        print('The ticket number is not valid\n')
    


# Read file - parking_records.csv when the program starts
if readFile():
    # File Success message
    print(f'Record reading from {CSV_FILE} is successful!') 
    
    option = None
    while option != '5':
        # Display menu and ask user for option
        displayMenu()
        option = input('Please select an option between 1-5: ')
        
        # When user chooses 1 
        if option == '1':
            enteringCarPark()
        
        # When user chooses 2 
        elif option == '2':
            exitingCarPark()
        
        # When user chooses 3 
        elif option == '3':
            showAvailParkingSpaces()
        
        # When user chooses 4 
        elif option == '4':
            queryTicketNumber()
            
        # When user chooses 5
        elif option == '5':
            # Save the records in the file 
            writeFile() 
            print('/nThank you very much for using my car park. Goodbye!')
        
        # When a user option is invalid
        else:
            print('Invalid Option! Please try again')
            

# Error message for problems in reading file
else:
    print(f'There was an error in reading file - {CSV_FILE}')
    print(f'Please make sure the file - {CSV_FILE} is present in the same directory! \nGoodbye!')
        

        
        
