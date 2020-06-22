""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
file_name = "store/games.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["ID", "Title", "Manufacturer", "Price", "In stock"]
ID_NUMBER = 0
TITLE_NUMBER = 1
MANUFACTURER_NUMBER = 2
PRICE_NUMBER = 3
IN_STOCK_NUMBER = 4

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
                        'Get number of games for each manufacturer',
                        'Get average size of game stock for each manufacturer']
        # printing menu
        ui.print_menu("Store", list_options, "Main menu press 0")
        # Dick of available option to start equal function
        dic_function = {'1': show_table,
                        "2": add,
                        "3": remove,
                        "4": update,
                        "5": get_counts_by_manufacturers,
                        "6": get_average_by_manufacturer,
                        '0': exit
                        }
        # Start oprion
        common.choose_by_dic(dic_function, table)

    # your code


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
    # id_ = ui.get_inputs('wprowadz', '')
    # your code
    #id_index_of_row = 0
    '''
    element_index_in_list = 0
    for row in table:
        if id_[element_index_in_list] in row:
            table.remove(row)
    '''
    common.remove_universal(table, id_)

    data_manager.write_table_to_file(file_name, table)
    #return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
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

def get_counts_by_manufacturers(table, *args):
    """
    Question: How many different kinds of game are available for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    manufacturers = set(row[MANUFACTURER_NUMBER] for row in table)

    counts_by_manufacturers = {m:0 for m in manufacturers}

    for m in manufacturers:
        for row in table:
            if row[MANUFACTURER_NUMBER] == m:
                counts_by_manufacturers[m] += 1
    
    # Delete this after you fix the print_result() to also print dictionaries:
    counts_by_manufacturers = [(k,v) for k, v in counts_by_manufacturers.items()]

    ui.print_result(counts_by_manufacturers, 'Number of games for each manufacturer')
    return counts_by_manufacturers


def get_average_by_manufacturer(table):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
        number
    """

    manufacturers = set(row[MANUFACTURER_NUMBER] for row in table)

    the_manufacturer = ui.get_inputs(['Enter the manufacturer: '], '')[0]

    print(the_manufacturer)

    average_by_manufacturer = 0
    game_count = 0

    for row in table:
        if row[MANUFACTURER_NUMBER] == the_manufacturer:
            average_by_manufacturer += int(row[IN_STOCK_NUMBER])
            game_count += 1

    try:
        average_by_manufacturer /= game_count
        ui.print_result(average_by_manufacturer, f'Average size of {the_manufacturer}\'s game stock is')
    except ZeroDivisionError:
        common.ID_error()