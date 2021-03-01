import smbus
import time
# Mode 1 setup
bus = smbus.SMBus(1)



while 1:
    min_freq = int(input("enter minimum frequency (GREATER THAN 24Hz): "))
    max_freq = int(input("enter maximum frequency (GREATER THAN 24Hz): "))
    lift_off = int(input("Enter the liftoff frequency: "))
    touch_down = int(input("Enter the touchdown frequency: "))
    cycles = int(input("Enter the number of cycles: "))
    delay = int(input("Enter delay between cycles: "))
    for a in range(cycles):
        freq = min_freq
        for i in range(min_freq,max_freq+1):
            # Mode 1 setup
            Device_address = 0x70   
            register = 0x00
            data = [0x11]
            bus.write_i2c_block_data(Device_address,register,data)

            # Mode 2 setup
            Device_address = 0x70
            register = 0x01
            data = [0x04]
            bus.write_i2c_block_data(Device_address,register,data)

            # Prescaler setup
            prescale = (25000000/(4096*freq))-1
            Device_address = 0x70
            register = 0xFE
            data = [prescale]
            freq +=1
            bus.write_i2c_block_data(Device_address,register,data)

            # Mode 1 setup
            Device_address = 0x70
            register = 0x00
            data = [0x81]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED0_OFF_L
            Device_address = 0x70
            register = 0x08
            data = [0xFE]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED0_OFF_H
            Device_address = 0x70
            register = 0x09
            data = [0x07]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED1_OFF_L
            Device_address = 0x70
            register = 0x0C
            data = [0xFE]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED1_OFF_H
            Device_address = 0x70
            register = 0x0D
            data = [0x07]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED2_OFF_L
            Device_address = 0x70
            register = 0x10
            data = [0xFE]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED2_OFF_H
            Device_address = 0x70
            register = 0x11
            data = [0x07]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED3_OFF_L
            Device_address = 0x70
            register = 0x14
            data = [0xFE]
            bus.write_i2c_block_data(Device_address,register,data)

            # LED3_OFF_H
            Device_address = 0x70
            register = 0x15
            data = [0x07]
            bus.write_i2c_block_data(Device_address,register,data)
            time.sleep(1)
        # Mode 1 setup
        Device_address = 0x70   
        register = 0x00
        data = [0x11]
        bus.write_i2c_block_data(Device_address,register,data)

        # Mode 2 setup
        Device_address = 0x70
        register = 0x01
        data = [0x04]
        bus.write_i2c_block_data(Device_address,register,data)

        # Prescaler setup
        prescale = 0
        Device_address = 0x70
        register = 0xFE
        data = [prescale]
        freq +=1
        bus.write_i2c_block_data(Device_address,register,data)
        time.sleep(delay)