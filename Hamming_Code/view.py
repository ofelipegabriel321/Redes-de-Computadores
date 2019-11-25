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
    
    def enter_to_generate_data_bits_and_parity_bits(self):
        input("\npress ENTER to generate data bits and parity bits of the final"
              "message (not yet determining the value of the parity bits)...")


if __name__ == '__main__':
    view = View()
    view.enter_to_generate_data_bits_and_parity_bits()