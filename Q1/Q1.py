class NFA_A:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.input_symbols = {'a'}
        self.transitions = {
            'q0': {'a': {'q1'}},
            'q1': {'a': {'q1'}}
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
        return bool(current_states.intersection(self.accept_states))

nfa_a = NFA_A()
print(nfa_a.is_accepted("aaa"))  # Output: True
print(nfa_a.is_accepted("aba"))  # Output: False
