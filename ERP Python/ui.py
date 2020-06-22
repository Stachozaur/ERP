""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    maxLengths=[] #list of max lenghts in columns
    width=1 #table width

#Column widths
    for j in range(0,len(title_list)): # j-column index
        max=len(title_list[j])
        for i in range(0,len(table)): # i-row index
            length=len((table[i])[j])
            if max<length:
                max=length
        maxLengths.append(max)
        width+=max+5

#Printing titles
    print()
    for j in range(0,len(title_list)):
        print("║ ", title_list[j], end="")
        print(" "*(maxLengths[j]-len(title_list[j])+2), end="")
    print("║")


#Printing table
    print("="*width)
    for i in range(0,len(table)): 
        for j in range(0,len(title_list)):
            print("║ ", (table[i])[j], end="")
            print(" "*(maxLengths[j]-len((table[i])[j])+2), end="")
        print("║")
        print("─"*width)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(label, end=": ")

    if isinstance(result, list):
        for element in result: 
            if isinstance(element, list): #list of lists
                for record in element:
                    print(record, end="  ")
                print()
            else:    
                print(element) #list
    elif isinstance(result, dict):
        list_elem = result.items()
        print(f"{label}")
        for item in list_elem:
            print(f"{item[0]} {item[1]}")

    else:
        print(result)




def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    for value in range(len(list_options)):
        print(f"({value+1}) {list_options[value]}")
    print(exit_message)



def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    for element in range(len(list_labels)):
        inputs.append(input(list_labels[element]))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    print("Error: ", message)

#Test data




'''
titles=['ID', 'Name', 'Info']
emp1=['gy5677fdsfbmsbadjhsagdjasdg76', "Anna Nowak", "x"]
emp2=['g1', "Jan Ko", "hoho"]
emp3=['g133', "Jan Konieczkokoko", "parapapa123"]
emp4=['g1123', "Basia Bobu", "dupa"]
employees=[emp1, emp2, emp3, emp4]
# print_table(employees,titles)
slownik={"key1":"wart1"}
print(slownik.items())
#print_result(employees,"Uzytkownik")
'''