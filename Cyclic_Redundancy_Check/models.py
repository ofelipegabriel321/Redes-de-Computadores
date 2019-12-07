from copy import deepcopy

class BitSequenceHandler:
    def __init__(self, initial_bit_sequence, generator):
        self.initial_bit_sequence = initial_bit_sequence
        self.final_bit_sequence = []
        self.generator = generator
        self.crc = [0] * (len(self.generator) - 1)

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
    
    def calculate_crc_value(self):
        dividend = deepcopy(self.final_bit_sequence)
        available_dividend = list(reversed(dividend))
        divisor = self.generator
        quotient = []
        remainder = []

        add_zero_in_quotient = False

        while True:
            if available_dividend == []:
                if len(remainder) == len(divisor):
                    quotient += [0]
                    remainder = self.apply_xor(remainder, divisor)
                    while True:
                        try:
                            if remainder[0] == 1:
                                break
                            else:
                                remainder = remainder[1:len(remainder)]
                        except:
                            break
                break
            
            while True:
                try:
                    if remainder[0] == 1:
                        break
                    else:
                        remainder = remainder[1:len(remainder)]
                except:
                    break
            while len(remainder) < len(divisor):
                if available_dividend == []:
                    quotient += [0]
                    break
                remainder.append(available_dividend.pop())

                while len(remainder) < len(divisor):
                    if available_dividend == []:
                        if quotient != []:
                            quotient += [0]
                        break
                    remainder.append(available_dividend.pop())
                    if quotient != []:
                        quotient += [0]
                
                if available_dividend == []:
                    break
            
            if available_dividend != []:
                quotient += [1]
                remainder = self.apply_xor(remainder, divisor)
        remainder = (len(divisor) - 1 - len(remainder)) * [0] + remainder

        self.crc = remainder

    def encode_final_bit_sequence(self):
        self.final_bit_sequence = self.initial_bit_sequence + self.crc

    def check_final_bit_sequence(self):
        self.calculate_crc_value()
        if 1 in self.crc:
            return False
        return True
