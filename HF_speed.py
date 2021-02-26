import smbus
import time
# Mode 1 setup
bus = smbus.SMBus(1)

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
Device_address = 0x70
register = 0xFE
data = [0xFF]
bus.write_i2c_block_data(Device_address,register,data)

# Mode 1 setup
Device_address = 0x70
register = 0x00
data = [0x81]
bus.write_i2c_block_data(Device_address,register,data)

# LED0_ON_L
Device_address = 0x70
register = 0x06
data = [0x00]
bus.write_i2c_block_data(Device_address,register,data)

# LED0_ON_H
Device_address = 0x70
register = 0x07
data = [0x00]

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
# while 1:
#     data = [0x1E]
#     for i in range(10):
#         data[0] += 1 
#         print(data)
#         bus.write_i2c_block_data(Device_address,register , data)
#         bus.write_i2c_block_data(Device_address,0xFB , [0x7C])
#         bus.write_i2c_block_data(Device_address,0xFD , [0x7C])
#         bus.write_i2c_block_data(Device_address,0xFE , [0x80])
        
#         time.sleep(1)