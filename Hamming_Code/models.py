class BitSequenceHandler:
    def __init__(self, initial_bit_sequence):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = None
        self.parity = None

    def generate_data_bits_and_parity_bits(self):
        self.final_bit_sequence = []
        data_bit_count = len(self.initial_bit_sequence)
        data_bit_count_entered = 0
        final_bit_sequence_index = 0
        next_parity_bit = 1
        while data_bit_count_entered < data_bit_count:
            if (final_bit_sequence_index + 1) == next_parity_bit:
                self.final_bit_sequence.append('P')
                next_parity_bit *= 2
            else:
                self.final_bit_sequence.append(self.initial_bit_sequence[data_bit_count_entered])
                data_bit_count_entered += 1
            final_bit_sequence_index += 1
