from copy import deepcopy

class BitSequenceHandler:
    def __init__(self, initial_bit_sequence, generator_polynomial):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = None
        self.generator_polynomial = generator_polynomial
        self.crc = [0] * (len(self.generator_polynomial) - 1)

    def generate_bit_sequence_initial_dividend(self):
        self.final_bit_sequence = self.initial_bit_sequence + self.crc
    
    def apply_xor(self, list_1, list_2):
        xor_result = []
        for index in range(len(list_1)):
            if list_1[index] == list_2[index]:
                xor_result += [0]
            else:
                xor_result += [1]
        return xor_result
