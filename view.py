# Class View

class View:

    @staticmethod
    def menu_start():
        print "1. Get list of available buses"
        print "2. Add new bus"
        print "3. Delete bus"
        print "4. Change existing bus"
        print "5. Add new route"
        print "6. Delete route"
        print "7. Change existing route"
        print "8. Exit"
        View.separator_line()

    @staticmethod
    def display(lst):
        print "List of buses"
        for bus in lst: 
            print ", ".join(map(lambda tag: tag + ' : ' + str(bus[tag]), bus.keys()))
        View.separator_line()


    @staticmethod
    def add_new_bus():
        print "Add new bus"
        print "Input name, number, and route number"
        View.separator_line()

    @staticmethod
    def delete_bus():
        print "Delete exeisting bus"
        print "Enter the number of bus to be deleted"

    @staticmethod
    def change_bus_one():
        print "Choose bus with number or enter 0 to skip"

    @staticmethod
    def change_bus_two():
        print "Change bus items"
        print "Enter new value for item or enter 0 to skip"

    @staticmethod
    def error_message():
        print "ERROR! Invalid input"
        View.separator_line()
    
    @staticmethod
    def separator_line():
        print "-----------------------"

    @staticmethod
    def warn_message():
        print "This number is alreay exist. Number was generated automaticaly"
        View.separator_line()

    @staticmethod
    def success_message():
        print "Successfull operation"
        View.separator_line()

    @staticmethod
    def wrong_number_message():
        print "No existing number"
        View.separator_line()
