class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.input_symbols = {'a', 'b', 'c'}
        self.transitions = {
            'q0': {'a': 'q1'},
            'q1': {'b': 'q2', 'c': 'q1'},
            'q2': {}
        }
        self.start_state = 'q0'
        self.accept_states = {'q2'}

    def check_accepted_string(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False
        return current_state in self.accept_states

# Usage
dfa = DFA()
print(dfa.check_accepted_string("abbbc"))  # Output: True or False based on input
