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
    def display_all_buses(lst):
        print "List of buses"
        for bus in lst: 
            print ", ".join(map(lambda tag: tag + ' : ' + str(bus[tag]), bus.keys()))
        View.separator_line()


    @staticmethod
    def add_new():
        print "Add new bus"
        print "Input name, number, and route number"

    @staticmethod
    def error_message():
        print "ERROR! Invalid input"
        View.separator_line()
    
    @staticmethod
    def separator_line():
        print "-----------------------"
