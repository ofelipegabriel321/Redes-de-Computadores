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
