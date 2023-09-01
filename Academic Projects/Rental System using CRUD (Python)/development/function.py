import datetime
def WelcomeNotice(): #message displayed to welcome user 
    print("**********************************************")
    print("\tWelcome to our Application")
    print("**********************************************")
    print("\n")

def OptionSelectNotice(): #message displayed to select option 
    print("Select a desirable option")
    print("(1) || Press 1 for renting a costume")
    print("(2) || Press 2 for returning a costume")
    print("(3) || Press 3 to exit.\n")

def ThankyouNotice(): # message displayed when exitted from program  
    print("\nThank You for using our application.\n")

def InvalidNotice(): # message displayed in case of invalid input 
    print("\nPlease enter a valid input")
    print("\nThe value shall be selected as per the provided options\n")

def RentC(): #message displayed containing options available to rent 
    print("\nOptions available for Rent\n")

def AvailableCostume(): #message displayed when costume is available
    print("\n-----------------------------------")
    print("Costume is in Stock.")
    print("------------------------------------\n")

def UnavailableCostume(): #message displayed when costume is unavailable
    print("\n-----------------------------------")
    print("Insufficient stock for the selected Costume.")
    print("------------------------------------\n")


def InvalidExceptionNotice(): #message displayed when invalid input is given
    print("**********************************")
    print("Please provide a valid option")
    print("**********************************")


def RentDisplay(): # Displaying rent table
    file = open("Costume.txt","r")
    print("--------------------------------------------------------------")
    print("\tID \tCustomer Name   Costume Brand  Price   Quantity")
    print("--------------------------------------------------------------")
    IDcounter = 0
    for line in file:
        IDcounter = IDcounter + 1
        print("\t", IDcounter, "\t" + line.replace(",","\t"))
        print("--------------------------------------------")
    file.close()


def dictionaryRent(): #creating dictionary 
    file = open("Costume.txt", "r") #opening text file 
    IDcounter = 0
    dictionary_Costume = {}
    for line in file: 
        IDcounter = IDcounter + 1
        line = line.replace("\n","")
        line = line.split(',')

        dictionary_Costume[IDcounter] =  line

    return dictionary_Costume
    file.close() #closing text file


def ReturnC(): #message displayed during return
    print("Return")

def valid_costumeIDr(): #valid costume ID during return
    IsException = False #exception handling
    while IsException == False:
        try:
            validCostumeIDr = int(input("Please, Enter the ID of costume you desire to return: "))
            IsException = True
        except:
            InvalidExceptionNotice()
    
    while validCostumeIDr <= 0 or validCostumeIDr > len(dictionaryRent()):
        print("\nPlease provide a valid costume ID !\n")
        RentDisplay()
        validCostumeIDr = int(input("\nPlease, Enter the ID of costume you desire to return: "))
    return validCostumeIDr


def valid_costumeID(): #valid costume ID during rent
    IsException = False
    while IsException == False:
        try:
            validCostumeID = int(input("Please, Enter the ID of costume you desire to rent: "))
            IsException = True
        except:
            InvalidExceptionNotice()
    
    while validCostumeID <= 0 or validCostumeID > len(dictionaryRent()):
        print("\nPlease provide a valid costume ID !\n")
        RentDisplay()
        validCostumeID = int(input("\nPlease, Enter the ID of costume you desire to rent: "))
    return validCostumeID

def RentQuantity(stockquantity): # checking the quantity of costume during rent
    IsException = False
    while IsException == False:
        try:
            quantityCostume = int(input("\nEnter the quantity: "))
            IsException = True
        except:
            InvalidExceptionNotice()

    while quantityCostume <=0 or quantityCostume > stockquantity:
        if quantityCostume <= 0:
            print("\n-----------------------------------------")
            print("Please provide a valid quantity.") #message if invalid input
            print("-----------------------------------------\n")
        else:
            print("\n-----------------------------------------")
            print("Provided quantity is greater than the stock quantity.") #message if input is greater than stock
            print("-----------------------------------------\n")

        IsException = False
        while IsException == False:
            try:
                quantityCostume = int(input("\nEnter the quantity: "))
                IsException = True
            except:
                InvalidExceptionNotice()
    return quantityCostume

def ReturnQuantity(c): # checking the quantity of costume during rent
    IsException = False
    while IsException == False:
        try:
            quantityCostume = int(input("\nEnter the quantity: "))
            IsException = True
        except:
            InvalidExceptionNotice()

    while quantityCostume <=0:
        if quantityCostume <= 0:
            print("\n-----------------------------------------")
            print("Please provide valid quantity.")#message if invalid input
            print("-----------------------------------------\n")
        IsException = False
        while IsException == False:
            try:
                quantityCostume = int(input("\nEnter the quantity: "))
                IsException = True
            except:
                InvalidExceptionNotice()
    return quantityCostume

def StockCostume(dictionary): 
    file = open("Costume.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()

def CalculatePrice(dictionary, quantitydetails, costumeID): #display price
    Price = float(dictionary[costumeID][2].replace("$",""))
    print("The Price would be:", Price)
    pricePItem = Price * quantitydetails
    return pricePItem

def BillofRent(name, todaysdate, totalprice, rentCostumename, rentCostumebrand, Price): #display bill details
    print("\n--------------------------------------------")
    print("\t Bill Details") 
    print("--------------------------------------------\n")
    print("Name: ", name)
    print("Date and Time of Rent: ", todaysdate)
    print("Total price: " + "$", totalprice)
    print("Rented Costumes are: ")
    for x in range(len(rentCostumename)):
        print(str(x+1) + ". " + rentCostumename[x] + ":- " + rentCostumebrand[x] + "\t$"+ str(Price[x]))
    print("**********************************************")

def Create_DetailofRent(cname, date, total, costumename, costumebrand, Price):
    fileName = "Rent_" + cname + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"
#creating detail of rent bill in text file
    file = open(fileName, "w")
    file.write("Name: " + cname + "\n")
    file.write("Date of rent: " + str(date) + "\n")
    file.write("Total price of: " + str(total) + "\n")
    file.write("Rented Costumes are: " + "\n")
    for i in range(len(costumename)):
        file.write(str(i+1) + ". " + costumename[i] + ":- " + costumebrand[i] + "\t$"+ str(Price[i]) + "\n")
    file.close()

def BillofReturn(name, todaysdate, days, fine, costumename, costumebrand, listA): #creating bill during return
    print("\n--------------------------------------------")
    print("\t Bill Details")
    print("--------------------------------------------\n")
    print("Name: ", name)
    print("Time of return: ", todaysdate)
    print("Total no of days: ", days)
    print("Applicable Fine: " + "$", fine)
    print("Rented Costumes are: ")
    for i in range(len(costumename)):
        print(str(i+1) + ". " + costumename[i] + ":- " + costumebrand[i] + "\t$" + str(listA[i]))
    print("**********************************************")

def Create_DetailofReturn(cname, date, days, fine, costumeName, costumeBrand, listA):
    fileName = "Return_" + cname + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"
#creating detail of return bill in text file
    file = open(fileName, "w")
    file.write("Name: " + cname + "\n")
    file.write("Date of return: " + str(date) + "\n")
    file.write("Total no of days:" + str(days))
    file.write("Applicable Fine: " + str(fine) + "\n")
    file.write("Rented Costumes are: " + "\n")
    for x in range(len(costumeName)):
        file.write(str(x+1) + ". " + costumeName[x] + ":- " + costumeBrand[x] + "$" + str(listA[x]) +"\n")
    file.close()
