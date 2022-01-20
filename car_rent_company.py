class CarRentCompany:
    def __init__(self, cars):
        self.cars = cars

    # Method of object CarRentCompany, displaying all available cars
    def displayCar(self):
        print("Available cars are: ")
        for car in self.cars:
            print(" " + car)

    # Method of object CarRentCompany, check if given text in parameter carName is in self.cars, if it is remove it, if it's not display message. 
    def borrowCar(self, carName):
        if carName in self.cars:
            print(f"\nGood choice! Here You go, take the keys, oh and return it after 1 week")
            self.cars.remove(carName)
        else: print("Sorry we don't have that car")

    # Method of object CarRentCompany, appends value of parameter carName to self.cars     
    def returnCar(self, carName):
        self.carname = carName
        self.cars.append(carName)
        print("Thanks for returning the car!")

class Client:
    # requestCars and returnCars methods of object Client, assigning value to self.cars from input for further use 
    def requestCars(self):
        self.cars = input("What car would You like? : ")
        return self.cars
        
    def returnCars(self):
        self.cars = input("What car are You returning? : ")
    
if __name__ == "__main__":
    # CarRentCompany initialization object and assigning it to carCompany variable
    carComapny = CarRentCompany(["Porshe V15", "Mercedes X2", "Tesla 3", "Skoda", "Fiat Multipla", "Toyota Paris", "Fiat Seicento"])

    # Client initialization object and assigning it to client1 variable
    client1 = Client()

    # Welcome text and options message text
    print("Hello there to our Car Rent Company")
    optionMsg ='''
        Please choose an option:
        1. Display list of all available car
        2. Borrow car
        3. Return car
        4. Exit Car Rent Company \n
        '''
    
    # while loop displaying options and processing informations
    while True:
        try: 
            clientOption = int(input(optionMsg))
            # "Switch" Statement for processing chosen option
            if clientOption == 1:
                carComapny.displayCars()
            elif clientOption == 2:
                carComapny.borrowCars(client1.requestCars())
            elif clientOption == 3:
                carComapny.returnCars(client1.returnCars())
            elif clientOption == 4:
                break
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number");
