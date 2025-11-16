class Currency:

    def __init__(self,value,arr):
        self.value = value
        self.arr = arr

    def Rupees(self):
        while True:
            try:
                print("\nConvert your Indian Rupee into:-")
                print("1.United States Dollars")
                print("2.Euro")
                print("3.Canadian Dollars")
                print("4.Exit")

                conversion_choice = int(input("\nEnter your currency to convert into: "))

                if conversion_choice == 1:
                    result = f"The {self.value} Rupee is equal to {self.value/88.69:.5f} USD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 2:
                    result = f"The {self.value} Rupee is equal to {self.value/103.03:.5f} Euro."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 3:
                    result = f"The {self.value} Rupee is equal to {self.value/62.99:.5f} CAD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 4:
                    print("\nIf You want to convert Indian Rupee come again........")
                    print(line)
                    break

                else:
                    print("\nInvalid Input Please Try Again........")
                    print(line)

            except ValueError:
                print("Enter Integer in Front of currency to convert in...........")
                print(line)

    def Dollars(self):
        while True:
            try:
                print("\nConvert your United States Dollars into:-")
                print("1.Indian Rupee")
                print("2.Euro")
                print("3.Canadian Dollars")
                print("4.Exit")

                conversion_choice = int(input("\nEnter your currency to convert into: "))

                if conversion_choice == 1:
                    result = f"The {self.value} USD is equal to {self.value*88.69:.5f} Rupee."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 2:
                    result = f"The {self.value} USD is equal to {self.value/1.16:.5f} Euro."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 3:
                    result = f"The {self.value} USD is equal to {self.value/0.71:.5f} CAD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 4:
                    print("\nIf You want to convert United States Dollars come again........")
                    print(line)
                    break

                else:
                    print("\nInvalid Input Please Try Again........")
                    print(line)

            except ValueError:
                print("Enter Integer in Front of currency to convert in...........")
                print(line)

    def Euro(self):
        while True:
            try:
                print("\nConvert your Euro into:-")
                print("1.Indian Rupee")
                print("2.United States Dollars")
                print("3.Canadian Dollars")
                print("4.Exit")

                conversion_choice = int(input("\nEnter your currency to convert into: "))

                if conversion_choice == 1:
                    result = f"The {self.value} Euro is equal to {self.value*103.03:.5f} Rupee."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 2:
                    result = f"The {self.value} Euro is equal to {self.value*1.16:.5f} USD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 3:
                    result = f"The {self.value} Euro is equal to {self.value/0.61:.5f} CAD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 4:
                    print("\nIf You want to convert Euro come again........")
                    print(line)
                    break

                else:
                    print("\nInvalid Input Please Try Again........")
                    print(line)

            except ValueError:
                print("Enter Integer in Front of currency to convert in...........")
                print(line)

    def Canadian_Dollar(self):
        while True:
            try:
                print("\nConvert your Canadian Dollars into:-")
                print("1.Indian Rupee")
                print("2.Euro")
                print("3.United States Dollars")
                print("4.Exit")

                conversion_choice = int(input("\nEnter your currency to convert into: "))

                if conversion_choice == 1:
                    result = f"The {self.value} CAD is equal to {self.value*62.99:.5f} Rupee."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 2:
                    result = f"The {self.value} CAD is equal to {self.value*0.61:.5f} Euro."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 3:
                    result = f"The {self.value} CAD is equal to {self.value*0.71:.5f} USD."
                    self.arr.append(result)
                    print(f"\n{result}")
                    print(line)

                elif conversion_choice == 4:
                    print("\nIf You want to convert Canadian Dollars come again........")
                    print(line)
                    break

                else:
                    print("\nInvalid Input Please Try Again........")
                    print(line)

            except ValueError:
                print("Enter Integer in Front of currency to convert in...........")
                print(line)

def history(arr):
    while True:
        try:
            print("\nWhat Do you want to do with history?")
            print("1.Show History")
            print("2.Clear History")
            print("3.Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print('Your Conversion History:-\n',arr)
                print(line)

            elif choice == 2:
                arr.clear()
                print(arr)
                print(line)

            elif choice == 3:
                print("Exiting History........................")
                print(line)
                break

            else:
                print("Invalid Choice Please Try Again")
                print(line)

        except ValueError:
            print("Invalid Input,Please Enter integer value...........")
            print(line)

def Main():

    arr = []
    while True:
        try:
            print('--------------Menu--------------')
            print("1.Convert Currency")
            print("2.History")
            print("3.Exit")

            try:
                final_choice = int(input("Enter Your Choice: "))
            
            except ValueError:
                print("Invalid Input, Please Enter Integer Value.")

            if final_choice == 1:
                value = float(input("\nEnter the value to convert: "))
                value = round(value,5)

                currency = str(input("\nEnter the currency your value is in [USD,INR,EUR,CAD]: ").upper().strip())

                Currency_Converter = Currency(value,arr)

                if currency in ['INR','RUPEE']:
                    Currency_Converter.Rupees()

                elif currency in ['USD','DOLLAR']:
                    Currency_Converter.Dollars()

                elif currency in ['EUR','EURO']:
                    Currency_Converter.Euro()

                elif currency in ['CAD']:
                    Currency_Converter.Canadian_Dollar()

                else:
                    print("\nInvalid Input Please Try Again..........")
                    print(line)
            
            elif final_choice == 2:
                history(arr)

            elif final_choice == 3:
                print("Exiting...................")
                break

            else:
                print("Invalid Input,Please Try Again.........")

        except ValueError:
            print("\nPlease enter Float/Integer value..........")
            print(line)

line = '-' * 100
print("Welcome to our Currency Converter")
print('We can currently convert between 4 currencies USD,IND,EUR,CAD')
print('We will add More currencies in due Time.........')

print("--------------NOTE--------------")
print("The Answers and Inputs given by the program will be till 5 decimal places..............")
print('Now Enjoy Your Conversion------------------------------------------------------->')

Main()