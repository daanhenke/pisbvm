class Stack(object):
    def __init__(self, bit_size, slot_size):
        self.mask = 2 ** bit_size
        self.slot_size = slot_size
        self.array = [0] * slot_size
        self.stack_pointer = -1

    def cur(self):
        return self.array[self.stack_pointer]

    def push(self, value):
        self.stack_pointer = (self.stack_pointer + 1)
        self.array[self.stack_pointer] = value % self.mask
        #print self.stack_pointer

    def pop(self):
        value = self.cur()
        self.stack_pointer = (self.stack_pointer - 1)
        #print self.stack_pointer
        return value
