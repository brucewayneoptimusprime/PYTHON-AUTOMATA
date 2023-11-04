class NFA:
    def __init__(self):
        # Define NFA states and transitions here
        self.states = {'q0', 'q1'}
        self.input_symbols = {'a', 'b'}
        self.transitions = {
            'q0': {'a': {'q1'}, 'b': {'q0'}},
            'q1': {'a': {'q1'}, 'b': {'q0', 'q1'}}
        }

    def get_reachable_states(self, state, input_symbol):
        return self.transitions[state].get(input_symbol, set())

# Usage
nfa = NFA()
reachable = nfa.get_reachable_states('q0', 'a')
print(reachable)  # Output: {'q1'} or any other set of reachable states
