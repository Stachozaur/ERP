""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
file_name = "crm/customers.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["ID", "Name", "Email", "Subscribed"]

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """


    while True:
        # List of available option
        list_options = ['Show table',
                        'Add new customer',
                        'Remove customer',
                        'Update customer',
                        'Show ID of customer with longest name',
                        'Show customers which has subscripted the newsletter']
        # printing menu
        ui.print_menu("Customer relation management", list_options, "Main menu press 0")
        # Dick of available option to start equal function
        dic_function = {'1': show_table, "2": add, "3": remove, "4": update, "5": get_longest_name_id,
                        "6": get_subscribed_emails, '0': exit}
        # Start oprion
        common.choose_by_dic(dic_function, table)

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    #title_list = ["ID", "Name", "Email", "Subscribed"]
    ui.print_table(table, title_list)
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    # Universal add tool in common
    table = common.add_universal(table, title_list)

    # Save to file
    data_manager.write_table_to_file(file_name, table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    common.remove_universal(table, id_)

    data_manager.write_table_to_file(file_name, table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    # Main Universal update function use
    common.update_universal(table, id_, title_list)
    # Save to file
    data_manager.write_table_to_file(file_name, table)
    return table


# special functions:
# ------------------

def get_longest_name_id(table, *args):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    longest_name = 0
    name = 1
    id_name = 0
    longest = []
    long_name="z"
    for row in table:
        if longest_name > len(row[name]):
            longest_name = len(row[name])
        
    # for row in table:
    #     if int(longest_name) == int(len(row[name])):
    #         longest.append(row[name])
    #         for name in longest:
    #             if long_name > name:
    #                 long_name = name

    # print(long_name)
    print("\n \t ID of longest name is:  ", row[id_name], "And His name is!: ", row[name])

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table, *args):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code

    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    get_name_by_id_from_table(table, id)



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    item_date = 0
    last_item_date = 0

    for row in table:
        for id in row:
            return row[1]
