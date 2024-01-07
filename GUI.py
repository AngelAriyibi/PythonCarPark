from main import *
from tkinter import *
import re


# Display Tickets
def displayTicket(record):
    ticketY = 160
    canvas.create_text(350, ticketY - 5, text=f"Details of your ticket", font=('Verdana',16, 'bold'), justify="center", tags="ticket", width = 650)

    # Add number of available space to record
    record['AvailableSpace'] = len(getAvailableParkingSpace())

    # Display the ticket title and ticket value
    i = 1
    for k,v in record.items():
        title = ''.join([' ' + char if char.isupper() and i > 0 else char for i, char in enumerate(k)])
        canvas.create_text(350, ticketY + i * 24 , text=f"{title}: {v}", font=('Verdana',14), justify="center", tags="ticket", width = 650)
        i += 1
    
    
# Display error message for car or ticket pages
def displayErrorMessage(number, car = True):
    errorText = f'Cannot find the ticket details of the car with {"registration" if car else "ticket"} number "{number}"'
    canvas.create_text(350, 200, text=errorText, font=('Verdana',15 ), justify="center", tags="ticket", fill='red', width = 550)


# Enter Car Park for GUI
def mainCanvasGUI(enter = True, ticketQuery = False):
    
    # Define action:
    action = None

    # If the user clicks on query ticket, then perform the getTicket function
    if ticketQuery:
        action = getTicket
        instructionText = 'Enter your Ticket Number'

    # Otherwise perform addCar or RemoveCar function if the user is entering or exiting
    else:
        action = addCar if enter else removeCar
        instructionText = CAR_NUMBER_INSTRUCTIONS + ' Enter your car registration number.'

    # When user clicks on submit button
    def onSubmit():
        # Clear ticket section
        canvas.delete('ticket')
        
        # Get number (car or ticket) and perform the right action
        number = carNumberEntry.get()
        record = action(number)
        
        # If the record is available display otherwise display error message
        if record:
            displayTicket(record)
        else:
            displayErrorMessage(number, not ticketQuery)

    # Create Instruction Message
    canvas.create_text(350, 50, text=instructionText, font=('Verdana',13), justify="center", tags="text", width = 650)
    
    # Entry Button
    carNumberEntry = Entry()
    canvas.create_window(330, 105, window=carNumberEntry, tags="carNumberEntry")
    
    # Submit Button
    submitBtn = Button(app, text='SUBMIT', command=onSubmit)
    canvas.create_window(470, 105, window=submitBtn, tags="submitButton")
        

# Show GUI for the available parking spaces
def showParkingSpaces():
    parkingSpacesAvail = getAvailableParkingSpace()
    tmpText = f'Number of available parking spaces is {len(parkingSpacesAvail)}'
    canvas.create_text(350, 70, text=tmpText, font=('Verdana',14,'bold'), justify="center", width = 650)

    # Go through all parking spaces and display in an organized form
    for i,pkSpace in enumerate(parkingSpacesAvail):
        row = (i // 10 ) * 40
        col = (i % 10) * 70
        canvas.create_text(40 + col, 130 + row, text=pkSpace, font=('Verdana',14))


# Functionality for when the menu buttons are clicked
def menuClicked(idx):
    # Change Side Label text and clear the canvas
    sideLabel.config(text=menus[idx])
    canvas.delete('all')
    
    # Save to file and End program if user quits
    if idx == 4:
        writeFile() 
        app.destroy()
        return
    
    # Enter the car park
    elif idx == 0:
        mainCanvasGUI(enter = True )
    
    # Exit the car park
    elif idx == 1:
        mainCanvasGUI(enter = False)
    
    # Enter the car park
    elif idx == 2:
        showParkingSpaces()
    
    # Enter the car park
    elif idx == 3:
        mainCanvasGUI(ticketQuery = True)


# Create menu buttons
def createMenuButtons():
    def menuButton(text, X, command):
        button = Button(app, text=text, font=("Verdana", 12, 'bold'), anchor='center', justify ='center', width=17, height= 4, command=command )
        button.place(x=X, y=10)
        return button
    
    # Go through the menu
    global menus
    menus = ["Enter the Car Park \n(Hourly Rate: £2.00)", "Exit Car Park", "View available\n parking spaces", "Query parking record\n by ticket number", "Quit"]
    for i,menu in enumerate(menus):
        menuButton(menu, (i * 200) + 10, lambda i=i: menuClicked(i))
        


def createGUI():
    # Create the main application window
    global app
    app = Tk()
    app.title("ANGEL CAR PARK")
    app.geometry('1000x500')

    # Side Label
    global sideLabel
    sideLabel = Label(app, text='Welcome!!!', font=("Verdana", 13, 'bold'), anchor='center')
    sideLabel.place(x=30 ,y= 250)
    
    # Main Canvas
    global canvas
    canvas = Canvas(app, bg='white', width=700, height=350)
    canvas.place(x = 250, y = 120)
    
    # Create menu Section
    createMenuButtons()

    # Start the GUI event loop if file is read, otherwise close file
    if readFile():
        app.mainloop()
    else:
        print('There is a problem with the file. Please try again later')
        exit()



createGUI()

