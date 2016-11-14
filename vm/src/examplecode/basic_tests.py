### BASIC EXAMPLE PISBVM CODE ###

test_001 = [
    0x00,               #NOP
    0x00,               #NOP
    0x00,               #NOP
    0x01, 0x69,         #PUSH 0x69
    #0xFE,               #DMPS
    0x01, 0x01,         #PUSH 0x01
    #0xFE,               #DMPS
    0x02,               #ADD
    #0xFE,               #DMPS
    0x01, 0x02,         #PUSH 0x02
    #0xFE,               #DMPS
    0x03,               #MUL
    #0xFE,               #DMPS
    0x10, 0x00, 0x04,   #JUMP 0x0003
    0xFF                #HALT
]