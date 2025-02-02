"""
This program will collect 5 different numerical values from it's user,
then output a small variety of different bits of info based on those 5 number inputs.
This is just beginning to tap into my full potential as a software developer. While this may look somewhat basic,
it is important to note that this is just scratching the surface of what I am capable of. More advanced and adaptable versions of this and many other kinds of programs can be created using the skills I have.

DISCLAIMER: This program is a DEMO PROGRAM, one I created for the express purpose of giving others a taste of what I am capable of with my computer programming skills.
I do not intend for it to be useful for any real world purpose, and I advise that you don't expect that from it either.

README: For more info about what this program does, and to learn about it's licencing restrictions, please refer to the README.txt file that is packaged with this one

To run this program on your own device, you will need a working instance of a Python interpreter on that device. This is due to the fact that Python is an interpreted language, rather than compiled,
so it normally cannot be ran entirely on it's own, as it is dependant on another program to enterpret it's code and execute it.
"""


def Get_Largest_Increase(value1, value2, value3, value4, value5): # This function collects the values entered by the user, and determines which step up (between different values) is the biggest increase between two values. Can be used with negative numbers as well. 
    Increase1 = value2 - value1
    Increase2 = value3 - value2
    Increase3 = value4 - value3
    Increase4 = value5 - value4
    Largest_Increase = 0
    Largest_Increase_ID = 0
    if Increase1 > Largest_Increase:
        Largest_Increase = Increase1
        Largest_Increase_ID = 1
    if Increase2 > Largest_Increase:
        Largest_Increase = Increase2
        Largest_Increase_ID = 2
    if Increase3 > Largest_Increase:
        Largest_Increase = Increase3
        Largest_Increase_ID = 3
    if Increase4 > Largest_Increase:
        Largest_Increase = Increase4
        Largest_Increase_ID = 4
    Result = "Value = " + str(Largest_Increase) + ", ID = " + str(Largest_Increase_ID)
    return Result

def Get_Smallest_Increase(value1, value2, value3, value4, value5): # This function is pretty much the opposite of the last one above. It does basically the same thing, but outputs the smallest increase, rather than the biggest.
    Increase1 = value2 - value1
    Increase2 = value3 - value2
    Increase3 = value4 - value3
    Increase4 = value5 - value4
    Smallest_Increase = 10000
    Smallest_Increase_ID = 0
    if Increase1 < Smallest_Increase and Increase1 != 0:
        Smallest_Increase = Increase1
        Smallest_Increase_ID = 1
    if Increase2 < Smallest_Increase and Increase2 != 0:
        Smallest_Increase = Increase2
        Smallest_Increase_ID = 2
    if Increase3 < Smallest_Increase and Increase3 != 0:
        Smallest_Increase = Increase3
        Smallest_Increase_ID = 3
    if Increase4 < Smallest_Increase and Increase4 != 0:
        Smallest_Increase = Increase4
        Smallest_Increase_ID = 4
    Result = "Value = " + str(Smallest_Increase) + ", ID = " + str(Smallest_Increase_ID) + "\n"
    return Result
        
        

def Get_Average_Increase(value1, value2, value3, value4, value5): # Gets the average of all the increases and decreases between each of the data points entered by the user.
    Increase1 = value2 - value1
    Increase2 = value3 - value2
    Increase3 = value4 - value3
    Increase4 = value5 - value4
    Result = (Increase1 + Increase2 + Increase3 + Increase4) / 4
    return str(Result)

def Data_Analysis(): # The core function of this program. This one will carry out the tasks of collecting user input for each of the values, and is also responsible for triggering every other function in the program, and displaying the results of the analysis.
    Data_List = [0, 0, 0, 0, 0]
    for i in range(5):
        PointID = i + 1
        Input_Needed = True
        while Input_Needed:
            try:
                Input_Value = int(input("Please enter value for data point #" + str(PointID) + ": "))
                Input_Needed = False
            except:
                print("That is not an integer! Please try again.")
        Data_List[i] = Input_Value
    Average_Increase = Get_Average_Increase(Data_List[0], Data_List[1], Data_List[2], Data_List[3], Data_List[4])
    Largest_Increase = Get_Largest_Increase(Data_List[0], Data_List[1], Data_List[2], Data_List[3], Data_List[4])
    Smallest_Increase = Get_Smallest_Increase(Data_List[0], Data_List[1], Data_List[2], Data_List[3], Data_List[4])
    print("Results: ")
    print("Average Increase: " + Average_Increase)
    print("Largest Increase: " + Largest_Increase)
    print("Smallest Increase: " + Smallest_Increase)

    


print("This program will allow you to enter 5 different numerical values,\n then will output certain details based on said data.\n This is intended as a demo program and should not be expected to\n have any real world value. Please refer to the READMME.txt file that is packaged with\n this program to learn more about it's purpose and licensing restrictions")
Running = True
while Running: # Simple while loop to make sure the program does not cloes on it's own until the user wants it to.
    Data_Analysis()
    Invalid_Reply = True
    while (Invalid_Reply):
        User_Reply = input("Data Analyzation has finished. Would you like to repeat it? (Yes/No): ")
        if (User_Reply == "Yes" or User_Reply == "yes"):
            print("Ok, starting over from the beginning of the process.")
            Invalid_Reply = False
        elif (User_Reply == "No" or User_Reply == "no"):
            Running = False
            Invalid_Reply = False
        else:
            print("Invalid entry. Please try again.")
