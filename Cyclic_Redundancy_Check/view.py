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
    
    def insert_bit_sequence(self):
        bit_sequence = input("\nInsert the bit sequence: ")
        return bit_sequence
    
    def insert_generator(self):
        generator = input("\nInsert the generator: ")
    
    