class View:
    
    def color_text(self, color):
        color_palette = {"standart color": "\033[0m",
                         "red": "\033[0;31;40m",
                         "green": "\033[0;32;40m",
                         "yellow": "\033[0;33;40m",
                         "white": "\033[0;37;40m",
                         "white with underline": "\033[4;37;40m"}
        return color_palette[color]
    
    def message_building_menu(self):
        option = input(self.color_text("yellow") + ""
                       "\n*----------------+++ MESSAGE BUILDING MENU +++----------------*"
                       "\n| 1 - Insert new bit sequence and generator                   |"
                       "\n| 0 - Exit                                                    |"
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
    
    def invalid_bit_sequence_format_message(self):
        input(self.color_text("red") + ""
              "\nInvalid bit sequence format! The bit sequence must start and end with number 1.\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def invalid_generator_message(self):
        input(self.color_text("red") + ""
              "\nInvalid generator!\n"
              "" + self.color_text("standart color") + ""
              "\nPress ENTER to continue ...")
    
    def insert_bit_sequence(self):
        bit_sequence = input("\nInsert the bit sequence: ")
        return bit_sequence
    
    def insert_generator(self):
        generator = input("\nInsert the generator: ")
        return generator
    
    def enter_to_generate_bit_sequence_initial_dividend(self):
        input("\nPress ENTER to generate bit sequence initial dividend...")
    
    def enter_to_calculate_crc_value(self):
        input("\nPress ENTER to calculate crc value...")
    
    def enter_to_encode_final_bit_sequence(self):
        input("\nPress ENTER to encode final bit sequence...")

    def display_bit_sequence_handler_attributes(self, initial_bit_sequence=False,
                                                final_bit_sequence=False,
                                                generator=False,
                                                crc=False,
                                                bit_sequence_error_indexes=[]):
        bit_sequence_handler_attributes = ""
        
        if initial_bit_sequence != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Initial bit sequence:\n" + self.color_text('standart color')
            for bit_index in range(len(initial_bit_sequence)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' '
                bit_sequence_handler_attributes += str(initial_bit_sequence[bit_index])
        
        if final_bit_sequence != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Final bit sequence:\n" + self.color_text('standart color')
            for bit_index in range(len(final_bit_sequence)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' '
 
                if bit_index in bit_sequence_error_indexes:
                    bit_sequence_handler_attributes += self.color_text('white with underline')
                
                bit_sequence_handler_attributes += str(final_bit_sequence[bit_index]) + self.color_text('standart color')
 
        if generator != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "Generator:\n" + self.color_text('standart color')
            for bit_index in range(len(generator)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' '
                bit_sequence_handler_attributes += str(generator[bit_index])
        
        if crc != False:
            bit_sequence_handler_attributes += "\n\n" + self.color_text('green') + "CRC:\n" + self.color_text('standart color')
            for bit_index in range(len(crc)):
                if bit_index != 0:
                    bit_sequence_handler_attributes += ' '
                bit_sequence_handler_attributes += str(crc[bit_index])
        
        print(bit_sequence_handler_attributes)
