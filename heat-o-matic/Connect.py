from mecom import MeComSerial, ResponseException, ResponseTimeout, WrongChecksum, DEFAULT_QUERIES, COMMAND_TABLE
from serial import SerialException
from serial.serialutil import PortNotOpenError
import time

class tec_controller(object): 
    
    """
    Controlling multiple TEC devices via single serial bus.
    """

    def _tearDown(self):
        self.session().stop()

    def __init__(self, port=None, scan_timeout=10, channel=[1,2], queries=DEFAULT_QUERIES, *args, **kwars):
        self.channel = channel
        self.port = port
        self.scan_timeout = scan_timeout
        self.queries = queries
        self.session = []
        self.addresses = {}
        self._connect()
    
    # FLOW:
    # 1. find COM ports to connect to 
    # 2. query identify() on each COM port, to find the devices on the bus
    def _connect(self):
        # open session
        if self.port is not None:
            self.session = MeComSerial(serialport=self.port)
        else:
            self.query_COM_ports()
                        
            if len(self.session) == 0:
                    raise PortNotOpenError
            else: 
                self.find_addresses()   
            print(f'connected to devices: {self.addresses}')
            
    def query_COM_ports(self):
        #querying COM ports on the computer
        #to be sure that I am not missing any devices
        i=1
        while len(self.session) < 2 and i < 257:
            try:
                print(f'trying port COM{i}')               
                self.session.append(MeComSerial("COM"+str(i)))       
                print(f'found device on port COM{i}')
            except SerialException:
                pass
            #wait for a bit
            time.sleep(0.1)
            i+=1
            
    def find_addresses(self):
        # best to store tuples in a dict
        # (key, value) = (device_address, (serial_object, device_name))
        for port in self.session:
            self.find_addresses_on_port(port)
        print(f'found devices: {self.addresses}')
        
    def find_addresses_on_port(self, port):
        for i in range(1,255):
            try:                     
                print(f'querying if a device exists with address {i}')
                response = port.identify(address=i)
                print(f'address: {response}')
                self.addresses[i] = (port, self.get_device_type(i, port))
                break
            except ResponseTimeout:
                pass
            #wait for a bit
            time.sleep(0.1) 
        

    def session(self):
        if self.session is None:
            self._connect()
        return self.session
            
    # def get_data(self):
    #     data = {}
        
    #     for description in self.queries:
    #         id, unit = COMMAND_TABLE[description]
    #         try:
    #             value = self.session().get_parameter(parameter_id=id, address=self.address, parameter_instance=self.channel[0])
    #             data.update({description: (value, unit)})
    #         except (ResponseException, WrongChecksum) as ex:
    #             self.session().stop()
    #             self.session = None
    #     return data
    
    def get_device_type(self, device_id, port=None):
        if port is None:
            port = self.addresses[device_id][0]
        name = port.get_parameter(parameter_name = "Device Type", address=device_id, parameter_instance=self.channel[0])
        return name
            
    def set_enable(self, device_id, enable=True):
        """
        Enable or disable control loop
        :param enable: bool
        :param channel: int
        :return:
        """
        port = self.addresses[device_id][0]
        value, description = (1, "on") if enable else (0, "off")

        if self.addresses[device_id][1] == 1123:
            port.set_parameter(value=value, parameter_name="Status", address=device_id, parameter_instance=self.channel[0])
           # port.set_parameter(value=value, parameter_name="Status", address=device_id, parameter_instance=self.channel[1])
        else:
            #then the device is the 1090
            port.set_parameter(value=value, parameter_name="Status", address=device_id, parameter_instance=self.channel[0])


    def set_temp(self, value, device_id):
        """
        Set object temperature of channel to desired value.
        :param value: float
        :param channel: int
        :return:
        """
        port = self.addresses[device_id][0]
        value = float(value)
        print(f'setting temperature to {value}')
        if self.addresses[device_id][1] == 1123:
            print(port.set_parameter(parameter_id=3000, value=value, address= device_id, parameter_instance=self.channel[0]))
            port.set_parameter(parameter_id=3000, value=value, address=device_id, parameter_instance=self.channel[1])
        else:
            #then the device is the 1090
            print(port.set_parameter(parameter_id=3000, value=value, address= device_id, parameter_instance=self.channel[0]))
            
if __name__ == "__main__":    

    tecs = tec_controller()
    tecs.set_enable(1, True)
    tecs.set_temp(20, 1)
    