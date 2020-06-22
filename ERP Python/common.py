""" Common module
implement commonly used functions here
"""

import random
import string
import ui
import main


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = ''

    Lletters = string.ascii_lowercase
    Uletters = string.ascii_uppercase
    Specials = ["#", "$", "%", "&", "?", "@"]
    Numbers = string.digits
    generated = random.choice(Lletters) + random.choice(Uletters) + random.choice(Numbers) + random.choice(Numbers) + random.choice(Uletters)+ random.choice(Lletters) + random.choice(Specials) + random.choice(Specials)

    return generated

def choose_by_dic(dic_function, table, *args):
    inputs = ui.get_inputs(["Choose option: "], " ")
    option = inputs[0]
    exit_code = 0
    if option == "1":
        dic_function["1"](table)
    elif option == "2":
        dic_function["2"](table)
    elif option == "3":
        id_ = ui.get_inputs(["Which ID do you want to remove? "],"")
        dic_function["3"](table, id_)
    elif option == "4":
        id_ = ui.get_inputs(["Which ID do you want to update? "],"")
        dic_function["4"](table, id_)
    elif option == "5":
        dic_function["5"](table)
    elif option == "6":
        dic_function["6"](table, *args)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")

    return exit_code


def add_universal(table, title_list):
    new_record = []
    add_index_start_for_name_rows = 1
    list_labels = title_list[add_index_start_for_name_rows:]
    id_record = generate_random(table)
    inputs_list = ui.get_inputs(list_labels, "")
    # Add input to list with nessery attributes
    # Add new ID - random
    new_record.append(id_record)
    # Iteration by rows
    for row in inputs_list:
        new_record.append(row)
    # Append new row to the table.
    table.append(new_record)

    return table


def remove_universal(table, id_):
    # chuse elemets ID from list
    element_index_in_list = 0
    for row in table:
        # use element  ID to check it is in list if it is remove this row
        if id_[element_index_in_list] in row:
            table.remove(row)
        else:
            ID_error()

    return table


def ID_error():
    ui.print_error_message("The ID doesn't exist.")


def update_universal(table, id_, title_list):
    # temp index name
    element_index_id = 0
    element_index_start_without_id = 1

    # CUTING FRAGMENT OF LIST STARTED AFTER ID
    labels = title_list[element_index_start_without_id:]

    # tempelary lists and values
    updated_row = []
    temp_list = []
    counter = 0
    ifWrong = True

    # Main loop
    for row in table:
        # checking is a our ID
        if row[element_index_id] == id_[element_index_id]:
            # if not this loop stat error
            ifWrong = False
            updated_row.append(id_[element_index_id])
            temp_list = ui.get_inputs(labels, "Please put new data:")
            # Checking module
            for rec in temp_list:
                updated_row.append(rec)
            table[counter] = updated_row
        counter += 1
    # Error mesage
    if ifWrong == True:
        ui.print_error_message("Id doesn't exist")

    return table
