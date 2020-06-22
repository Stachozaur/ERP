""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import sys
import os

file_name = "inventory/inventory.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["ID", "Game Name", 'Distributor', 'Data release', 'Available']

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
        list_options = ["Show table", "Add", "Remove", "Update", "Get Available items", "Get average durability by manufacturers"]
        # printing menu
        ui.print_menu("Inventory", list_options, "Main menu press 0")
        # Dick of available option to start equal function
        dic_function = {'1': show_table,
                        "2": add,
                        "3": remove,
                        "4": update,
                        "5": lambda table:  (get_available_items(table,  ui.get_inputs(["add year? "], ""))),
                        "6":get_average_durability_by_manufacturers, '0': exit}
        # Start option
        common.choose_by_dic(dic_function, table)



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code

    ui.print_table(table, title_list)



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
#@year
def get_available_items(table, year):
    print(year)
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table, *args):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
