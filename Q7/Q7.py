class NFA_OddOnes:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.input_symbols = {'0', '1'}
        self.transitions = {
            'q0': {'0': {'q0', 'q1'}, '1': {'q1'}},
            'q1': {'0': {'q1'}, '1': {'q0'}}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def is_accepted(self, string):
        current_states = {self.start_state}
        for symbol in string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states |= self.transitions[state][symbol]
            current_states = next_states
        return bool(len(current_states.intersection(self.accept_states)) % 2 == 1)

# Usage
nfa_ones = NFA_OddOnes()
print(nfa_ones.is_accepted("1011"))  # Output: True
print(nfa_ones.is_accepted("1100"))  # Output: False
