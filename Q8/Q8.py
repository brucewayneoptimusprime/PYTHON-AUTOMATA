class NFAFromRegex:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.input_symbols = {'a', 'b', 'c'}
        self.transitions = {
            'q0': {'a': {'q1'}},
            'q1': {'b': {'q2'}, 'c': {'q2'}},
            'q2': {}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1', 'q2'}

    def is_accepted(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol in self.transitions[current_state]:
                current_state = next(iter(self.transitions[current_state][symbol]))
            else:
                return False
        return current_state in self.accept_states

# Usage
nfa_regex = NFAFromRegex()
print(nfa_regex.is_accepted("abbbc"))  # Output: True or False based on input
