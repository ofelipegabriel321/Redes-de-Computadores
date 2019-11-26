from view import View
from models import BitSequenceHandler

class HammingCodeController:
    def __init__(self):
        self.view = View()

    def run(self):
        while True:
            option = self.view.message_building_menu()
            

            if option == 1:
                bit_sequence = self.view.insert_bit_sequence()
                parity = self.view.insert_parity()

                bit_sequence = list(bit_sequence)
                for bit_index in range(len(bit_sequence)):
                    bit_sequence[bit_index] = int(bit_sequence[bit_index])

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


            elif option == 0:
                break
            else:
                self.view.invalid_option_message()


if __name__ == '__main__':
    HammingCodeController().run()
