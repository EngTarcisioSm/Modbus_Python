import serial

class Modbus_Serial():
    def __init__(self):
        self.ports_available = list()

        self.ser = serial.Serial()

        self.timeout = 0
        
        # processos 
        self.check_ports()

    def start_serial(self, port, baudrate, bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0):
        #timeout é uma variavel do tipo float em que sua unidade representa segundo 
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.bytesize = bytesize
        self.ser.parity = parity
        self.ser.stopbits = stopbits
        self.ser.xonxoff = xonxoff
        self.ser.rtscts = rtscts

        if baudrate == 1200:
            self.timeout = 0.032
            self.ser.timeout 
        elif baudrate == 2400:
            self.timeout = 0.016
            self.ser.timeout 
        elif baudrate == 4800:
            self.timeout = 0.008
            self.ser.timeout 
        elif baudrate == 9600:
            self.timeout = 0.004
            self.ser.timeout 
        elif baudrate >= 19200:
            self.timeout = 0.002
            self.ser.timeout 
        else: 
            self.timeout = 1
        
        self.ser.timeout = self.timeout

        try:
            self.ser.open()
        except:
            print('deu merda')

    def stop_serial(self):
        try:
            self.ser.close()
        except:
            print('deu merda')

    def check_ports(self):
        number_port = 0 
        for port in range(1,100):
            try:
                port = '' + 'COM' + str(port)
                ser = serial.Serial(port)
                self.ports_available.append(port)
            except:
                pass
    
    def write_serial(self, msg):
        self.ser.write(b'hello') 
        pass
    
    def read_serial(self):
        pass


if __name__ == "__main__":

    teste = Modbus_Serial()
    print(teste.ports_available)

    teste.start_serial('COM7', 19200)
    print(teste.timeout)
    teste.write_serial("bla")
    teste.stop_serial()