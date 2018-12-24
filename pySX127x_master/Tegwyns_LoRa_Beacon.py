import sys
import datetime
import array as arr
import numpy as np
from time import sleep

if(__name__=='__main__'):
    from SX127x.LoRa import *
    from SX127x.LoRaArgumentParser import LoRaArgumentParser
    from SX127x.board_config import BOARD
else:
    from pySX127x_master.SX127x.LoRa import *
    from pySX127x_master.SX127x.LoRaArgumentParser import LoRaArgumentParser
    from pySX127x_master.SX127x.board_config import BOARD
    from security_cam import *

BOARD.setup()

parser = LoRaArgumentParser("A simple LoRa beacon")
parser.add_argument('--single', '-S', dest='single', default=False, action="store_true", help="Single transmission")
parser.add_argument('--wait', '-w', dest='wait', default=1, action="store", type=float, help="Waiting time between transmissions (default is 0s)")

ccc= 'Hello World'

g = arr.array('i',[])
n=-1

for x in ccc:
  g.extend([0])
  n = n+1
  y = ord(x)
  g[n] = y
print(g)

j = np.array(g).tolist()



class LoRaBeacon(LoRa):

    tx_counter = 0

    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([1,0,0,0,0,0])

    def on_cad_done(self):
        print("\non_CadDone")
        print(self.get_irq_flags())

    def on_valid_header(self):
        print("\non_ValidHeader")
        print(self.get_irq_flags())

    def on_payload_crc_error(self):
        print("\non_PayloadCrcError")
        print(self.get_irq_flags())

    def on_fhss_change_channel(self):
        print("\non_FhssChangeChannel")
        print(self.get_irq_flags())

        
    def start(self):
        counter = 0
        global args
        sys.stdout.write("\rstart\r")
        self.tx_counter = 0
        counter=counter+1
        stamp = str(counter) + ' ' + str(datetime.datetime.now())
        text=bytearray('PING LoRa Test PI: ' + stamp,'utf-8')
        self.write_payload([0x00, 0x00, 0x00, 0x00] + list(text))
        self.set_mode(MODE.TX)
        print( "Beacon number: %s\n" % counter)
        

lora = LoRaBeacon(verbose=False)
lora.start()


