class View:
    def color_text(self, color):
        color_palette = {"standart color": "\033[0m",
                         "red": "\033[0;31;40m",
                         "green": "\033[0;32;40m",
                         "yellow": "\033[0;33;40m",
                         "blue": "\033[0;34;40m",
                         "white": "\033[0;37;40m",
                         "red with underline": "\033[4;31;40m",
                         "white with underline": "\033[4;37;40m"}
        return color_palette[color]
    
    def message_building_menu(self):
        option = input(self.color_text("yellow") + ""
                       "\n*----------------+++ MESSAGE BUILDING MENU +++----------------*"
                       "\n| 1 - Insert new bit sequence and parity                      |"
                       "\n| 0 - Exit                                                    |"
                       "\n*-------------------------------------------------------------*"
                       "\nInsert an option: "
                       "" + self.color_text("standart color"))
        return option
    
    def received_message_menu(self):
        option = input(self.color_text("yellow") + ""
                       "\n*----------------+++ RECEIVED MESSAGE MENU +++----------------*"
                       "\n| 1 - Cause an error in the bit sequence                      |"
                       "\n| 2 - Check and try correct the bit sequence                  |"
                       "\n| 0 - Exit to message building menu                           |"
                       "\n*-------------------------------------------------------------*"
                       "\nInsert an option: "
                       "" + self.color_text("standart color"))
        return option
    
    def invalid_option_message(self):
        input(self.color_text("red") + ""
              "\nInvalid option!\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def invalid_bit_sequence_message(self):
        input(self.color_text("red") + ""
              "\nInvalid bit sequence!\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def invalid_parity_message(self):
        input(self.color_text("red") + ""
              "\nInvalid parity!\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def invalid_bit_index_message(self):
        input(self.color_text("red") + ""
              "\nInvalid bit index!\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def insert_bit_sequence(self):
        bit_sequence = input("\nInsert the bit sequence: ")
        return bit_sequence
    
    def insert_parity(self):
        parity = input("\nInsert parity (pair or odd): ")
        return parity
    
    def insert_bit_sequence_error(self):
        bit_sequence = int(input("\nInsert the index at which the error occurs in the bit sequence: "))
        return bit_sequence
    
    def enter_to_generate_data_bits_and_parity_bits(self):
        input("\nPress ENTER to generate data bits and parity bits of the final"
              "message (not yet determining the value of the parity bits)...")
    
    def enter_to_associate_parity_bits_and_data_bits(self):
        input("\nPress ENTER to associate parity bits and data bits...")
    
    def enter_to_calculate_parity_bit_values(self):
        input("\nPress ENTER to calculate parity bit values...")
    
    def enter_to_detect_an_error_in_the_bit_sequence(self):
        input("\nPress ENTER to detect an error in the bit sequence...")
    
    def enter_to_correct_an_error_in_the_bit_sequence(self):
        input("\nPress ENTER to correct an error in the bit sequence...")
    
    def display_bit_sequence_handler_attributes(self, initial_bit_sequence=False,
                                                final_bit_sequence=False,
                                                parity=False,
                                                parity_bits_associated_with_data_bits=False,
                                                bit_sequence_error_indexes=[]):
        bit_sequence_handler_attributes = ""
        
        if initial_bit_sequence != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Initial bit sequence:\n" + self.color_text('standart color')
            for bit_index in range(len(initial_bit_sequence)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' ' + str(initial_bit_sequence[bit_index].bit_value)
                else:
                    bit_sequence_handler_attributes += str(initial_bit_sequence[bit_index].bit_value)
        
        if final_bit_sequence != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Final bit sequence:\n" + self.color_text('standart color')
            next_parity_bit = 1
            for bit_index in range(len(final_bit_sequence)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' '
                
                if bit_index in bit_sequence_error_indexes:
                    if bit_index + 1 == next_parity_bit:
                        bit_sequence_handler_attributes += self.color_text('red with underline')
                        next_parity_bit *= 2
                    else:
                        bit_sequence_handler_attributes += self.color_text('white with underline')
                else:
                    if bit_index + 1 == next_parity_bit:
                        bit_sequence_handler_attributes += self.color_text('red')
                        next_parity_bit *= 2
                    else:
                        bit_sequence_handler_attributes += self.color_text('white')
                
                bit_sequence_handler_attributes += str(final_bit_sequence[bit_index].bit_value) + self.color_text('standart color')
        
        if parity != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Parity:\n" + self.color_text('standart color') + parity
        
        if parity_bits_associated_with_data_bits != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Parity bits associated with data bits:\n" + self.color_text('standart color')
            for parity_bit_index in sorted(parity_bits_associated_with_data_bits):
                bit_sequence_handler_attributes += self.color_text('red') + str(parity_bit_index) + self.color_text('standart color')
                for data_bit_index in sorted(parity_bits_associated_with_data_bits[parity_bit_index]):
                    bit_sequence_handler_attributes += '  ' + self.color_text('blue') + str(data_bit_index) + self.color_text('standart color') + ':'
                    bit_sequence_handler_attributes += str(parity_bits_associated_with_data_bits[parity_bit_index][data_bit_index])
                bit_sequence_handler_attributes += "\n"
        
        print(bit_sequence_handler_attributes)
    
    def display_an_error_in_the_bit_sequence(self, bit_sequence_error_index):
        print("\nThe error occurred at bit", bit_sequence_error_index)
