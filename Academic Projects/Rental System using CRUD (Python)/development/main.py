import function #importing function.py
import datetime
function.WelcomeNotice() #calling Welcome message
contLoop = True 
while contLoop == True:

    function.OptionSelectNotice() #calling Option selection message

    IsException = False
    while IsException == False:
        try:
            n = int(input("Choose a desirable option: ")) #Taking input from the user
            IsException = True
        except:
            function.InvalidExceptionNotice()
            function.OptionSelectNotice()


    if n == 1: # option to rent
        function.RentC() #call options available message
        function.RentDisplay() # call rent table
        function.dictionaryRent() #call dictionary

        dictionary_Costume = function.dictionaryRent() #checking

        rentCostumeID = function.valid_costumeID() #checking

        rentCostumeA = [] #list creation
        rentCostumeC = [] #list creation
        Price = [] #list creation

        if int(dictionary_Costume[rentCostumeID][3]) > 0:
            function.AvailableCostume()

            quantityCostume = function.RentQuantity(int(dictionary_Costume[rentCostumeID][3]))
            dictionary_Costume[rentCostumeID][3] = int(dictionary_Costume[rentCostumeID][3]) - quantityCostume

            name = input("Please enter your name: ") #taking user input
            todaysdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            rentCostumeA.append(dictionary_Costume[rentCostumeID][0]) #adding to list
            rentCostumeC.append(dictionary_Costume[rentCostumeID][1])   #adding to list

            function.StockCostume(dictionary_Costume)

            totalPrice = function.CalculatePrice(dictionary_Costume,quantityCostume,rentCostumeID)
            Price.append(totalPrice) #adding to list
            
            print("################################################")
            print("Do you desire to rent another costume as well?") #prompt
            contrent = input("Please enter 'y' if you want to rent another costume else provide any other input: ").lower()

            loop = True
            while loop == True:
                if contrent == "y":
                    function.RentC()
                    function.RentDisplay()
                    dictionary_Costume = function.dictionaryRent()
                    rentCostumeID = function.valid_costumeID()

                    if int(dictionary_Costume[rentCostumeID][3]) > 0:
                        function.AvailableCostume()

                        
                        

                        if dictionary_Costume[rentCostumeID][0] in rentCostumeA:
                            quantityCostume = function.RentQuantity(int(dictionary_Costume[rentCostumeID][3])) + quantityCostume
                        
                        else:
                            rentCostumeA.append(dictionary_Costume[rentCostumeID][0])
                            rentCostumeC.append(dictionary_Costume[rentCostumeID][1])
                            quantityCostume = function.RentQuantity(int(dictionary_Costume[rentCostumeID][3])) + quantityCostume

                        dictionary_Costume[rentCostumeID][3] = int(dictionary_Costume[rentCostumeID][3]) - quantityCostume
                        function.StockCostume(dictionary_Costume)

                        totalprice = function.CalculatePrice(dictionary_Costume,quantityCostume,rentCostumeID) + totalPrice
                        Price.append(totalprice)
                        totalPrice = totalprice + totalPrice
                        print("**********************************************")
                        print("Do you desire to rent another costume as well?")
                        contrent = input("Please enter 'y' if you want to rent another costume else provide any other input: ").lower()
                    else:
                        function.UnavailableCostume()
                        function.BillofRent(name, todaysdate, totalPrice, rentCostumeA, rentCostumeC, Price) #calling rent bill
                        function.Create_DetailofRent(name, todaysdate, totalPrice, rentCostumeA, rentCostumeC, Price) #calling detail of rent bill
                        loop = False

                else:
                    function.BillofRent(name, todaysdate, totalPrice, rentCostumeA, rentCostumeC, Price)
                    function.Create_DetailofRent(name, todaysdate, totalPrice, rentCostumeA, rentCostumeC, Price)
                    loop = False
                    
        else:
            function.UnavailableCostume() #calling unavailablecostume notice
            
        
    elif n == 2: #option to return
        function.ReturnC() #calling functions
        function.RentDisplay()
        dictionary_Costume = function.dictionaryRent()
        returnCostumeID = function.valid_costumeIDr()

        returnCostumeA = [] #creating lists
        returnCostumeC = []
        listA = []

        quantityCostume = function.ReturnQuantity(int(dictionary_Costume[returnCostumeID][3]))
        dictionary_Costume[returnCostumeID][3] = int(dictionary_Costume[returnCostumeID][3]) + quantityCostume

        name = input("Please, enter your name: ") #taking input
        todaysdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        returnCostumeA.append(dictionary_Costume[returnCostumeID][0]) #adding to lists
        returnCostumeC.append(dictionary_Costume[returnCostumeID][1])

        function.StockCostume(dictionary_Costume)
        IsException = False
        while IsException == False:
            try:
                days = int(input("How many days was the costume rented for? ")) #Taking input from the user
                IsException = True
            except:
                function.InvalidExceptionNotice()
        

        fine = 0
        lateday = 0
        finep = 10
        if days > 5: #condition
            lateday = days - 5
            fine = lateday * finep * quantityCostume
            print("You have been fined:", fine, "for returning ", lateday, " days late.")
            listA.append(fine) #adding to listA
        print("**********************************************")
        print("Have you rented another costume as well?")
        contrent = input("Please enter 'y' if you've rented another costume else provide any other input: ").lower()

        loop = True
        while loop == True:
            if contrent == "y":
                function.ReturnC()
                function.RentDisplay()
                dictionary_Costume = function.dictionaryRent()
                returnCostumeID = function.valid_costumeIDr()
                

                if dictionary_Costume[returnCostumeID][0] in returnCostumeA:
                    quantityCostume = function.ReturnQuantity(int(dictionary_Costume[returnCostumeID][3])) + quantityCostume
                    dictionary_Costume[returnCostumeID][3] = int(dictionary_Costume[returnCostumeID][3]) + quantityCostume
                        
                else:
                    returnCostumeA.append(dictionary_Costume[returnCostumeID][0])
                    returnCostumeC.append(dictionary_Costume[returnCostumeID][1])
                    quantityCostume = function.ReturnQuantity(int(dictionary_Costume[returnCostumeID][3])) + quantityCostume
                    dictionary_Costume[returnCostumeID][3] = int(dictionary_Costume[returnCostumeID][3]) + quantityCostume

                function.StockCostume(dictionary_Costume)

                Fine = (lateday * finep * quantityCostume)
                fine = Fine + fine
                listA.append(Fine)
                print("You have been fined:", fine, "for returning ", lateday, " days late.")

                print("**********************************************")
                print("Have you rented another costume as well?")
                contrent = input("Please enter 'y' if you've rented another costume else provide any other input: ").lower()

            else:
                function.BillofReturn(name, todaysdate, days, fine, returnCostumeA, returnCostumeC, listA) #calling rentbill
                function.Create_DetailofReturn(name, todaysdate, days, fine, returnCostumeA, returnCostumeC, listA) #calling detail of rent bill
                loop = False
    

    elif n == 3: #option to exit
        function.ThankyouNotice() #calling thank you message
        contLoop = False

    else:
        function.InvalidNotice() #invalid option selection
