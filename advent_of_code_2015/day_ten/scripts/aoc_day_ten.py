import itertools
 
if __name__ == "__main__":
    class DigitSequence:
        def __init__(self):
            self.sequence = "1113222113"
        def update_sequence(self):
            new_sequence = ""
            for k, g in itertools.groupby(self.sequence):
                n_copy = str(len(list(g)))
                digit = str(k)
                new_sequence = "".join([new_sequence, n_copy, digit])
                self.sequence = new_sequence

    digit_sequence = DigitSequence()

    for i in range(40):
        digit_sequence.update_sequence()

    len(digit_sequence.sequence)  # Part One Answer

    digit_sequence_parttwo = DigitSequence()

    for i in range(50):
        digit_sequence_parttwo.update_sequence()

    len(digit_sequence_parttwo.sequence)  # Part Two Answer
 