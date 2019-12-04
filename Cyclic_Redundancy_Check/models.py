class BitSequenceHandler:
    def __init__(self, initial_bit_sequence, generator_polynomial):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = None
        self.generator_polynomial = generator_polynomial
        self.crc = None

    def generate_bit_sequence_initial_dividend(self):
        amount_of_zeros = len(self.generator_polynomial) - 1
        self.final_bit_sequence = []
        self.final_bit_sequence += self.initial_bit_sequence + amount_of_zeros * [0]
