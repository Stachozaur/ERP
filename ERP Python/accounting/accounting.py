""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = "accounting/items.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["ID", "Month", "Day", 'Year', "Type", "Amount"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    # you code
    while True:
        # List of available option
        list_options = ["Show table", "Add", "Remove", "Update", "The biggest sell in this year", "Average amount"]
        # printing menu
        ui.print_menu("Accounting", list_options, "Main menu press 0")
        # Dick of available option to start equal function
        dic_function = {'1': show_table, "2": add, "3": remove, "4": update, "5": which_year_max,
                        "6": avg_amount, '0': exit}
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


    # your code
    #title_list = ["ID", "Month", "Day", 'Year', "Type", "Amount"]
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

def which_year_max(table,*args):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    yearly_profit = {}
    for item in table:
        if item[4] == 'in':
            if item[3] not in yearly_profit.keys():
                yearly_profit.update({item[3]: float(item[5])})
            else:
                yearly_profit[item[3]] += float(item[5])
        elif item[4] == 'out':
            if item[3] not in yearly_profit.keys():
                yearly_profit.update({item[3]: (float(item[5]) * -1)})
            else:
                yearly_profit[item[3]] -= float(item[5])
    max_profit = max(yearly_profit.values())
    for key, value in yearly_profit.items():
        if value == max_profit:
            ui.print_result(int(key), '')
            return int(key)


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
