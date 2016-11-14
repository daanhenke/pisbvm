from debugerino.udpBugger import UDPBugger
from stack import Stack
from examplecode import basic_tests


class VirtualMachine(object):
    def __init__(self):
        self.debugger = UDPBugger()
        self.debugger.broadcast()
        self.debugMode = "spam"
        self.stack = Stack(8, 8)

        self.instruction_counter = 0x0000

        self.code = basic_tests.test_001

        self.lookup_table_alpha = {
            0x00: self.func_nop,
            0x01: self.func_push,
            0x02: self.func_add,
            0x03: self.func_mul,
            0x10: self.func_jump,
            0xFE: self.func_debug_dump_stack,
            0xFF: self.func_halt
        }

    def fetch(self):
        code = self.code[self.instruction_counter % 0xFFFF]
        self.instruction_counter += 1
        return code

    def execute_cycle(self):
        if self.instruction_counter < len(self.code):
            opcode = self.fetch()
            if opcode in self.lookup_table_alpha:
                self.lookup_table_alpha[opcode]()
                self.debugger.log("OP: " + str(opcode))
                self.debugger.log("STACK: " + str(self.stack.array))
                self.debugger.log("STACK POINTER: " + str(self.stack.stack_pointer))
                self.debugger.log("__________________________________________________")
            else:
                self.debugger.log("GOT INVALID OPCODE: " + str(opcode))
        return

    def func_nop(self):
        return

    def func_push(self):
        value = self.code[self.instruction_counter]
        self.instruction_counter += 1
        self.stack.push(value)
        return

    def func_add(self):
        value_second = self.stack.pop()
        value_first = self.stack.pop()

        self.stack.push(value_first + value_second)
        return

    def func_mul(self):
        value_second = self.stack.pop()
        value_first = self.stack.pop()

        self.stack.push(value_first * value_second)
        return

    def func_jump(self):
        address = (self.code[self.instruction_counter] << 8) + self.code[self.instruction_counter + 1]
        self.debugger.log("JUMPING TO: " + str(address))
        self.instruction_counter = address
        return

    def func_debug_dump_stack(self):
        self.debugger.log(str(self.stack.array))

    def func_halt(self):
        self.debugger.log("HALTING")
        return
