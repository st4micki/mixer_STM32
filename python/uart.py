import serial



class Uart(serial.Serial):
    def __init__(self, *args, **kwargs):
        super(Uart,self).__init__(*args, **kwargs)
        # self.baudrate = 9600
        # self.bytesize = serial.EIGHTBITS
        # self.parity = serial.PARITY_NONE
        # self.timeout = 1

        print('serial opened')
        print(f'PORT:     {self.port}')
        print(f'BAUD:     {self.baudrate}')
        print(f'SIZE:     {self.bytesize}')
        print(f'PARITY:   {self.parity}')
        print(f'STOPBITS: {self.stopbits}')
        print(f'TIMEOUT:  {self.timeout}')



