class View:
    def message_building_menu(self):
        option = int(input("\n*----------------+++ MESSAGE BUILDING MENU +++----------------*"
                           "\n| 1 - Insert new bit sequence and parity                      |"
                           "\n| 0 - Exit                                                    |"
                           "\n*-------------------------------------------------------------*"
                           "\nInsert an option: "))
        return option
    
    def received_message_menu(self):
        option = int(input("\n*----------------+++ RECEIVED MESSAGE MENU +++----------------*"
                           "\n| 1 - Cause, detect and correct an error in the bit sequence  |"
                           "\n| 2 - Check received bit sequence (not including errors)      |"
                           "\n| 0 - Exit to message building menu                           |"
                           "\n*-------------------------------------------------------------*"
                           "\nInsert an option: "))
        return option

    def insert_bit_sequence(self):
        bit_sequence = input("\nInsert the bit sequence: ")
        return bit_sequence
    
    def enter_to_generate_data_bits_and_parity_bits(self):
        input("\nPress ENTER to generate data bits and parity bits of the final"
              "message (not yet determining the value of the parity bits)...")
    
    def enter_to_associate_parity_bits_and_data_bits(self):
        input("\nPress ENTER to associate parity bits and data bits...")
    
    def enter_to_calculate_parity_bit_values(self):
        input("\nPress ENTER to calculate parity bit values...")
