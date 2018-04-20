# -*- coding: utf-8 -*-

"""
    A simple 3 state Busy Beaver Turing Machine

"""

class TuringMachine:
    
    tape = []
    state_table = {}
    
    def __init__(self):
        self.tape = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        self.state_table = {
            ("#", "s0"): ("1", "L", "s1"),
            ("0", "s0"): ("#", "N", "s0"),
            ("1", "s0"): ("1", "N", "h"),
            ("#", "s1"): ("#", "L", "s2"),
            ("0", "s1"): ("#", "N", "s0"),
            ("1", "s1"): ("1", "L", "s1"),
            ("#", "s2"): ("1", "R", "s2"),
            ("0", "s2"): ("#", "N", "s0"),
            ("1", "s2"): ("1", "R", "s0")
        }   

    def print_state(self, state, tape, head):
        return state.rjust(2) + ": " + "".join(tape)
               ## + "\n" + "      " + " " * head + "^"

    def simulate(self, instructions):
        tape = self.tape
        head = 0
        state = "s0"
        output = []
        output.append(self.print_state(state, tape, head))
        print(self.print_state(state, tape, head))
        while state != 'h':
            key = (tape[head], state)
            tape_symbol, head_direction, new_state = instructions[key]
            tape[head] = tape_symbol
            head += 0 if head_direction == "N" else 1 if head_direction == "R" else -1
            state = new_state
            print(self.print_state(state, tape, head))
            output.append(self.print_state(state, tape, head))
            if state == "h":
                print(self.print_state(state, tape, head))
                output.append(self.print_state(state, tape, head))
                break
        last_state = state + ": " + "".join(tape) ## + "\n" + "    " + " " * head + "^"
        return last_state
