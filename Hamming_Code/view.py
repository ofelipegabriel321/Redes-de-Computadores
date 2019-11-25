class View:
    def message_building_menu(self):
        option = int(input("\n*---+++ MESSAGE BUILDING MENU +++---*"
                           "\n| 1 - Insert new bit sequence       |"
                           "\n| 0 - Exit                          |"
                           "\n*-----------------------------------*"
                           "\nInsert an option: "))
        return option

    def insert_bit_sequence(self):
        bit_sequence = input("\nInsert the bit sequence: ")
        return bit_sequence
