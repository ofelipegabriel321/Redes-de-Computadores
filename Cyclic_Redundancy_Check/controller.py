from models import *
from view import *

class CyclicRedundancyCheckController:

    def __init__(self):
        self.view = View()
        self.message_sent = None
        self.message_received = None
        self.bit_sequence_error_indexes = []
    
    def build_message(self):
        while True:
            try:
                option = int(self.view.message_building_menu())
            except:
                self.view.invalid_option_message()
                continue
            
            if option == 1:
                try:
                    bit_sequence = self.view.insert_bit_sequence()
                    int(bit_sequence)
                except:
                    self.view.invalid_bit_sequence_message()
                    continue
                
                invalid_numbers = False
                
                bit_sequence = list(bit_sequence)
                for bit_index in range(len(bit_sequence)):
                    if not(bit_sequence[bit_index] in ['0', '1']):
                        invalid_numbers = True
                        break
                    bit_sequence[bit_index] = int(bit_sequence[bit_index])
                
                if invalid_numbers:
                    self.view.invalid_bit_sequence_message()
                    continue
                
                try:
                    generator = self.view.insert_generator()
                    int(generator)
                    if generator[0] == '0' or generator[-1] == '0' or len(generator) <= 1:
                        self.view.invalid_bit_sequence_format_message()
                        continue
                except:
                    self.view.invalid_generator_message()
                    continue
                
                generator = list(generator)
                for bit_index in range(len(generator)):
                    if not(generator[bit_index] in ['0', '1']):
                        invalid_numbers = True
                        break
                    generator[bit_index] = int(generator[bit_index])
                
                if invalid_numbers:
                    self.view.invalid_generator_message()
                    continue
                
                self.message_sent = BitSequenceHandler(initial_bit_sequence=bit_sequence, generator=generator) #[1, 1, 1, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1])
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  generator=self.message_sent.generator)
                
                self.view.enter_to_generate_bit_sequence_initial_dividend()
                self.message_sent.generate_bit_sequence_initial_dividend()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  generator=self.message_sent.generator)
                
                self.view.enter_to_calculate_crc_value()
                self.message_sent.calculate_crc_value()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  generator=self.message_sent.generator,
                                                                  crc=self.message_sent.crc)
                
                self.view.enter_to_encode_final_bit_sequence()
                self.message_sent.encode_final_bit_sequence()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  generator=self.message_sent.generator,
                                                                  crc=self.message_sent.crc)
                
            
            elif option == 0:
                break
            else:
                self.view.invalid_option_message()


if __name__ == '__main__':
    CyclicRedundancyCheckController().build_message()
