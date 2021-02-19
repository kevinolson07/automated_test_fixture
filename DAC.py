import smbus

bus = smbus.SMBus(1)
Device_address = 0x57

bus.write_i2c_block_data(Device_address,0x80 , [0x00,0x01])
bus.write_i2c_block_data(Device_address,0x2F , [0x00,0x00])

# DAC channels 
DAC_A = 0x20
DAC_B = 0x21
DAC_C = 0x22
DAC_D = 0x23
DAC_E = 0x24
DAC_F = 0x25
DAC_G = 0x26
DAC_H = 0x27
All_DAC = 0x2F

# DAC values
DAC_value_1 = [0x00, 0x00]
DAC_value_2 = [0x80, 0x00]
DAC_value_3 = [0xFF, 0x00]

while 1:
    x = 1
    while x:
        command_byte = int(input("Select which DAC you would like to edit: "))
        if command_byte == 1:
            DAC_select = DAC_A
            x = 0
        elif command_byte ==2:
            DAC_select = DAC_B
            x = 0
        elif command_byte ==3:
            DAC_select = DAC_C
            x = 0
        elif command_byte ==4:
            DAC_select = DAC_D
            x = 0
        elif command_byte ==5:
            DAC_select = DAC_E
            x = 0
        elif command_byte ==6:
            DAC_select = DAC_F
            x = 0
        elif command_byte ==7:
            DAC_select = DAC_G
            x = 0
        elif command_byte == 8:
            DAC_select = DAC_H
            x = 0
        elif  command_byte == 9:
            DAC_select = All_DAC
            x = 0
        else:
            print("Invalid input")
    y = 1 
    while y:
        data_byte = int(input("Select a DAC value: "))
        if data_byte == 1:
            DAC_value = DAC_value_1
            y = 0
        elif data_byte ==2:
            DAC_value = DAC_value_2
            y = 0
        elif data_byte ==3:
            DAC_value = DAC_value_3
            y = 0
        else: 
            print("Invalid value")
        
    bus.write_i2c_block_data(Device_address,DAC_select , DAC_value)