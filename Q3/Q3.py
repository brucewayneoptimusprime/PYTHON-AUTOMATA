class NFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.input_symbols = {'a', 'b'}
        self.transitions = {
            'q0': {'a': {'q1'}, 'b': {'q0', 'q1'}},
            'q1': {'b': {'q1'}}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def get_epsilon_closure(self, states):
        epsilon_closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            if '' in self.transitions[state]:
                for eps_state in self.transitions[state]['']:
                    if eps_state not in epsilon_closure:
                        epsilon_closure.add(eps_state)
                        stack.append(eps_state)

        return frozenset(epsilon_closure)

    def nfa_to_dfa(self):
        dfa_states = set()
        dfa_transitions = {}
        dfa_start_state = self.get_epsilon_closure({self.start_state})
        dfa_accept_states = set()

        stack = [dfa_start_state]
        while stack:
            current_states = stack.pop()
            dfa_states.add(current_states)
            for symbol in self.input_symbols:
                next_states = set()
                for state in current_states:
                    if symbol in self.transitions[state]:
                        next_states |= self.transitions[state][symbol]
                epsilon_closure = self.get_epsilon_closure(next_states)
                if epsilon_closure not in dfa_states:
                    stack.append(epsilon_closure)
                if current_states not in dfa_transitions:
                    dfa_transitions[current_states] = {}
                dfa_transitions[current_states][symbol] = epsilon_closure

        for state in dfa_states:
            if state.intersection(self.accept_states):
                dfa_accept_states.add(state)

        return dfa_states, dfa_transitions, dfa_start_state, dfa_accept_states

# Usage
nfa = NFA()
dfa_states, dfa_transitions, dfa_start, dfa_accept = nfa.nfa_to_dfa()
print("DFA States:", dfa_states)
print("DFA Transitions:", dfa_transitions)
print("DFA Start State:", dfa_start)
print("DFA Accept States:", dfa_accept)
