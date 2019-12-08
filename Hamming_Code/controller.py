from view import View
from models import *

class HammingCodeController:
    def __init__(self):
        self.view = View()
        self.message_sent = None
        self.message_received = None
        self.bit_sequence_error_indexes = []
    
    def receive_message(self):
        self.message_received = deepcopy(self.message_sent)
        self.message_received.initial_bit_sequence = None
        self.message_received.parity_bits_associated_with_data_bits = None
        while True:
            
            try:
                option = int(self.view.received_message_menu())
            except:
                self.view.invalid_option_message()
                continue
            
            if option == 1:
                self.view.display_bit_sequence_handler_attributes(final_bit_sequence=self.message_received.final_bit_sequence,
                                                                  bit_sequence_error_indexes=self.bit_sequence_error_indexes)
                try:
                    bit_sequence_error_caused_index = self.view.insert_bit_sequence_error()
                    if bit_sequence_error_caused_index == 0 or bit_sequence_error_caused_index > len(self.message_received.final_bit_sequence):
                        self.view.invalid_bit_index_message()
                        continue
                except:
                    self.view.invalid_bit_index_message()
                    continue
                
                self.message_received.cause_or_correct_an_error_in_the_bit_sequence(bit_sequence_error_caused_index)
                if not((bit_sequence_error_caused_index -1) in self.bit_sequence_error_indexes):
                    self.bit_sequence_error_indexes.append(bit_sequence_error_caused_index - 1)
                else:
                    self.bit_sequence_error_indexes.remove(bit_sequence_error_caused_index - 1)
                self.view.display_bit_sequence_handler_attributes(final_bit_sequence=self.message_received.final_bit_sequence,
                                                                    bit_sequence_error_indexes=self.bit_sequence_error_indexes)
            
            elif option == 2:
                self.view.enter_to_detect_an_error_in_the_bit_sequence()
                bit_sequence_error_found_index = self.message_received.detect_an_error_in_the_bit_sequence()
                self.view.display_an_error_in_the_bit_sequence(bit_sequence_error_found_index)
                
                self.view.enter_to_correct_an_error_in_the_bit_sequence()
                
                absolute_check_result = True
                if len(self.bit_sequence_error_indexes) > 1:
                    absolute_check_result = False
                
                check_result = True
                if bit_sequence_error_found_index != 0:
                    check_result = False
                
                self.view.display_check_report(check_result, absolute_check_result)
                
                self.message_received.cause_or_correct_an_error_in_the_bit_sequence(bit_sequence_error_found_index)
                if absolute_check_result is True:
                    self.bit_sequence_error_indexes = []
                else:
                    if not((bit_sequence_error_found_index -1) in self.bit_sequence_error_indexes):
                        self.bit_sequence_error_indexes.append(bit_sequence_error_found_index - 1)
                    else:
                        self.bit_sequence_error_indexes.remove(bit_sequence_error_found_index - 1)
                self.view.display_bit_sequence_handler_attributes(final_bit_sequence=self.message_received.final_bit_sequence,
                                                                  bit_sequence_error_indexes=self.bit_sequence_error_indexes)
            
            elif option == 0:
                break
            else:
                self.view.invalid_option_message()
    
    def build_message(self):
        while True:
            try:
                option = int(self.view.message_building_menu())
            except:
                self.view.invalid_option_message()
                continue
            
            if option == 1:
                try:
                    bit_sequence = int(self.view.insert_bit_sequence())
                except:
                    self.view.invalid_bit_sequence_message()
                    continue
                
                try:
                    parity = self.view.insert_parity()
                    if parity != "pair" and parity != "odd":
                        self.view.invalid_parity_message()
                        continue
                except:
                    self.view.invalid_parity_message()
                    continue
                
                bit_sequence = list(str(bit_sequence))
                for bit_index in range(len(bit_sequence)):
                    bit_sequence[bit_index] = Bit(bit_value=int(bit_sequence[bit_index]), is_parity_bit=False)
                
                self.message_sent = BitSequenceHandler(initial_bit_sequence=bit_sequence, parity=parity)
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  parity=self.message_sent.parity)
                
                self.view.enter_to_generate_data_bits_and_parity_bits()
                self.message_sent.generate_data_bits_and_parity_bits()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  parity=self.message_sent.parity)
                
                self.view.enter_to_associate_parity_bits_and_data_bits()
                self.message_sent.associate_parity_bits_and_data_bits()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  parity=self.message_sent.parity,
                                                                  parity_bits_associated_with_data_bits=self.message_sent.parity_bits_associated_with_data_bits)
                
                self.view.enter_to_calculate_parity_bit_values()
                self.message_sent.calculate_parity_bit_values()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=self.message_sent.initial_bit_sequence,
                                                                  final_bit_sequence=self.message_sent.final_bit_sequence,
                                                                  parity=self.message_sent.parity,
                                                                  parity_bits_associated_with_data_bits=self.message_sent.parity_bits_associated_with_data_bits)
                
                self.receive_message()

            elif option == 0:
                break
            else:
                self.view.invalid_option_message()


if __name__ == '__main__':
    HammingCodeController().build_message()
