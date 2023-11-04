def check_accepted_nfa_ab_or_ba(string):
    transitions = {
        'q0': {'a': {'q1'}, 'b': {'q2'}},
        'q1': {'b': {'q2'}},
        'q2': {'a': {'q1'}}
    }
    start_state = 'q0'
    accept_states = {'q1', 'q2'}

    current_states = {start_state}
    for symbol in string:
        next_states = set()
        for state in current_states:
            if symbol in transitions[state]:
                next_states |= transitions[state][symbol]
        current_states = next_states
    return bool(current_states.intersection(accept_states))

print(check_accepted_nfa_ab_or_ba("ab"))   # Output: True
print(check_accepted_nfa_ab_or_ba("ba"))   # Output: True
print(check_accepted_nfa_ab_or_ba("abc"))  # Output: False
