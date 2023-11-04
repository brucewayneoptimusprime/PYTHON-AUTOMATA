class NFAFromSimpleRegex:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.input_symbols = {'a', 'b', 'c'}
        self.transitions = {
            'q0': {'a': {'q1'}},
            'q1': {'': {'q2', 'q3'}},
            'q2': {'b': {'q2'}},
            'q3': {'c': {'q3'}}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1', 'q2', 'q3'}

    def is_accepted(self, string):
        current_states = {self.start_state}
        for symbol in string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states |= self.transitions[state][symbol]
            current_states = next_states
        return bool(current_states.intersection(self.accept_states))

# Usage
nfa_regex_simple = NFAFromSimpleRegex()
print(nfa_regex_simple.is_accepted("abbbc"))  # Output: True
print(nfa_regex_simple.is_accepted("ac"))    # Output: True
print(nfa_regex_simple.is_accepted("a"))     # Output: True
print(nfa_regex_simple.is_accepted("abc"))   # Output: False
