class Bit:
    def __init__(self, bit_value, is_parity_bit):
        self.bit_value = bit_value
        self.is_parity_bit = is_parity_bit

class BitSequenceHandler:
    def __init__(self, initial_bit_sequence, parity):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = None
        self.parity = parity
        self.parity_bits_associated_with_data_bits = None

    def generate_data_bits_and_parity_bits(self):
        self.final_bit_sequence = []
        data_bit_count = len(self.initial_bit_sequence)
        data_bit_count_entered = 0
        final_bit_sequence_index = 0
        next_parity_bit = 1
        while data_bit_count_entered < data_bit_count:
            if (final_bit_sequence_index + 1) == next_parity_bit:
                self.final_bit_sequence.append(Bit(bit_value='P', is_parity_bit=True))
                next_parity_bit *= 2
            else:
                self.final_bit_sequence.append(self.initial_bit_sequence[data_bit_count_entered])
                data_bit_count_entered += 1
            final_bit_sequence_index += 1

    def associate_parity_bits_and_data_bits(self):
        self.parity_bits_associated_with_data_bits = {}
        for data_bit_index in range(len(self.final_bit_sequence)):
            data_bit = self.final_bit_sequence[data_bit_index]
            if data_bit.is_parity_bit != True:
                data_bit_index_aux = data_bit_index + 1

                for parity_bit_index in range(len(self.final_bit_sequence[0:data_bit_index]), -1, -1):

                    parity_bit = self.final_bit_sequence[parity_bit_index]
                    parity_bit_added = parity_bit_index + 1
                    if parity_bit.is_parity_bit == True and data_bit_index_aux - parity_bit_added >= 0:
                        if not ((parity_bit_added) in self.parity_bits_associated_with_data_bits):
                            self.parity_bits_associated_with_data_bits[parity_bit_added] = {}
                        
                        self.parity_bits_associated_with_data_bits[parity_bit_added][data_bit_index + 1] = data_bit.bit_value

                        data_bit_index_aux -= parity_bit_added

                        if data_bit_index_aux == 0:
                            break
    
    def calculate_parity_bit_values(self):
        next_parity_bit = 1
        while next_parity_bit in self.parity_bits_associated_with_data_bits:
            comparison_value_with_parity = 0

            for data_bit_index in self.parity_bits_associated_with_data_bits[next_parity_bit]:
                comparison_value_with_parity += self.parity_bits_associated_with_data_bits[next_parity_bit][data_bit_index]
            
            if self.parity == 'pair':
                if comparison_value_with_parity % 2:
                    self.final_bit_sequence[next_parity_bit - 1].bit_value = 1
                else:
                    self.final_bit_sequence[next_parity_bit - 1].bit_value = 0
            if self.parity == 'odd':
                if comparison_value_with_parity % 2:
                    self.final_bit_sequence[next_parity_bit - 1].bit_value = 0
                else:
                    self.final_bit_sequence[next_parity_bit - 1].bit_value = 1

            next_parity_bit *= 2

    def cause_or_correct_an_error_in_the_bit_sequence(self, bit_sequence_error_index):
        if bit_sequence_error_index == 0:
            return None
        elif self.final_bit_sequence[bit_sequence_error_index - 1].bit_value == 1:
            self.final_bit_sequence[bit_sequence_error_index - 1].bit_value = 0
        elif self.final_bit_sequence[bit_sequence_error_index - 1].bit_value == 0:
            self.final_bit_sequence[bit_sequence_error_index - 1].bit_value = 1

    def detect_an_error_in_the_bit_sequence(self):
        original_final_bit_sequence = deepcopy(self.final_bit_sequence)
        self.associate_parity_bits_and_data_bits()
        self.calculate_parity_bit_values()
        bit_sequence_error_index = 0
        for bit_index in range(len(self.final_bit_sequence)):
            if self.final_bit_sequence[bit_index].bit_value != original_final_bit_sequence[bit_index].bit_value:
                bit_sequence_error_index += bit_index + 1
        self.final_bit_sequence = original_final_bit_sequence
        return bit_sequence_error_index
