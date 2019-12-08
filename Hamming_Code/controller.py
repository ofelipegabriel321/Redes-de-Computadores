from view import View
from models import Bit, BitSequenceHandler

class HammingCodeController:
    def __init__(self):
        self.view = View()
        self.bit_sequence_error_indexes = []

    def run(self):
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

                bit_sequence_handler = BitSequenceHandler(initial_bit_sequence=bit_sequence, parity=parity)
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=bit_sequence_handler.initial_bit_sequence,
                                                                  parity=bit_sequence_handler.parity)

                self.view.enter_to_generate_data_bits_and_parity_bits()
                bit_sequence_handler.generate_data_bits_and_parity_bits()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=bit_sequence_handler.initial_bit_sequence,
                                                                  final_bit_sequence=bit_sequence_handler.final_bit_sequence,
                                                                  parity=bit_sequence_handler.parity)
                
                self.view.enter_to_associate_parity_bits_and_data_bits()
                bit_sequence_handler.associate_parity_bits_and_data_bits()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=bit_sequence_handler.initial_bit_sequence,
                                                                  final_bit_sequence=bit_sequence_handler.final_bit_sequence,
                                                                  parity=bit_sequence_handler.parity,
                                                                  parity_bits_associated_with_data_bits=bit_sequence_handler.parity_bits_associated_with_data_bits)
                
                self.view.enter_to_calculate_parity_bit_values()
                bit_sequence_handler.calculate_parity_bit_values()
                self.view.display_bit_sequence_handler_attributes(initial_bit_sequence=bit_sequence_handler.initial_bit_sequence,
                                                                  final_bit_sequence=bit_sequence_handler.final_bit_sequence,
                                                                  parity=bit_sequence_handler.parity,
                                                                  parity_bits_associated_with_data_bits=bit_sequence_handler.parity_bits_associated_with_data_bits)

                while True:
                    bit_sequence_handler.initial_bit_sequence = None
                    bit_sequence_handler.parity_bits_associated_with_data_bits = None
                    
                    try:
                        option = int(self.view.received_message_menu())
                    except:
                        self.view.invalid_option_message()
                        continue

                    if option == 1:
                        self.view.display_bit_sequence_handler_attributes(final_bit_sequence=bit_sequence_handler.final_bit_sequence)
                        try:
                            bit_sequence_error_caused_index = self.view.insert_bit_sequence_error()
                            if bit_sequence_error_caused_index == 0 or bit_sequence_error_caused_index > len(bit_sequence_handler.final_bit_sequence):
                                self.view.invalid_bit_index_message()
                                continue
                        except:
                            self.view.invalid_bit_index_message()
                            continue

                        bit_sequence_handler.cause_or_correct_an_error_in_the_bit_sequence(bit_sequence_error_caused_index)
                        if not((bit_sequence_error_caused_index -1) in self.bit_sequence_error_indexes):
                            self.bit_sequence_error_indexes.append(bit_sequence_error_caused_index - 1)
                        else:
                            self.bit_sequence_error_indexes.remove(bit_sequence_error_caused_index - 1)
                        self.view.display_bit_sequence_handler_attributes(final_bit_sequence=bit_sequence_handler.final_bit_sequence,
                                                                          bit_sequence_error_indexes=self.bit_sequence_error_indexes)
                    
                    elif option == 2:
                        self.view.enter_to_detect_an_error_in_the_bit_sequence()
                        bit_sequence_error_found_index = bit_sequence_handler.detect_an_error_in_the_bit_sequence()
                        self.view.display_an_error_in_the_bit_sequence(bit_sequence_error_found_index)

                        self.view.enter_to_correct_an_error_in_the_bit_sequence()
                        bit_sequence_handler.cause_or_correct_an_error_in_the_bit_sequence(bit_sequence_error_found_index)
                        self.bit_sequence_error_indexes = []
                        self.view.display_bit_sequence_handler_attributes(final_bit_sequence=bit_sequence_handler.final_bit_sequence,
                                                                          bit_sequence_error_indexes=self.bit_sequence_error_indexes)
                    
                    elif option == 0:
                        break
                    else:
                        self.view.invalid_option_message()

            elif option == 0:
                break
            else:
                self.view.invalid_option_message()


if __name__ == '__main__':
    HammingCodeController().run()
