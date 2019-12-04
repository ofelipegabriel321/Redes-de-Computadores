class BitSequenceHandler:
    def __init__(self, initial_bit_sequence, generator_polynomial):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = None
        self.generator_polynomial = generator_polynomial
