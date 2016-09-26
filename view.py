# Class View

class View:

    @staticmethod
    def menu_start():
        View.separator_line()
        print "1. Get list of available buses"
        print "2. Get list of available routes"
        print "3. Add new bus"
        print "4. Delete bus"
        print "5. Change existing bus"
        print "6. Add new route"
        print "7. Delete route"
        print "8. Change existing route"
        print "9. Search for route by departure"
        print "10. Exit"
        View.separator_line()

    @staticmethod
    def display(lst):
        View.separator_line()
        for bus in lst: 
            print ", ".join(map(lambda tag: tag + ' : ' + str(bus[tag]), bus.keys()))
        View.separator_line()

# Methods for operation with bus
    @staticmethod
    def add_new_bus():
        print "Ad d new bus"
        print "Input name, number, and route number. Enter 0 to route number to leave it empty"

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
        

# Methods for operation with route
    @staticmethod
    def add_new_route():
        print "Add new route"
        print "Input route departure, route number and time"
        View.separator_line()

    @staticmethod
    def delete_route():
        print "Delete existing route"
        print "Enter the number of route to be deleted"

    
    @staticmethod
    def change_route_one():
        print "Choose route with number or enter 0 to skip"

    @staticmethod
    def change_route_two():
        print "Change route items"
        print "Enter new value for item or press enter to skip"

# Search method

    @staticmethod
    def search_for_bus():
        print "Enter the  departure place and hour before bus leave"
        print "Press enter to skip"

# System methods
    @staticmethod
    def error_message():
        print "ERROR! Invalid input"
        View.separator_line()
    
    @staticmethod
    def separator_line():
        print "-----------------------"

    @staticmethod
    def warn_message():
        View.separator_line()
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

    @staticmethod
    def wrong_option():
        print "No existing option"
        View.separator_line()

    @staticmethod
    def exit_message():
        View.separator_line()
        print "Thank you. Goodbye"

    @staticmethod
    def error_serialize_message():
        print "Incorrect file"
        View.separator_line()
