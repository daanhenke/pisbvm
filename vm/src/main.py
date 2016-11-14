import time
from VirtualMachine import VirtualMachine

vm = VirtualMachine()

while True:
    vm.execute_cycle()
    time.sleep(0.5)
