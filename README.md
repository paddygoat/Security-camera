<img src="https://cdn.instructables.com/F7P/6GXM/JQ0SMF58/F7P6GXMJQ0SMF58.SQUARE3.jpg"> 

<p>This blog shows how to build a security system based on detecting or 'inferring' the location of a person using a neural network USB pluggin stick on a Raspberry Pi. An Arduino type receiver is built from scratch to get data from the Raspberry Pi transmitter via the long range LoRa radio frequency protocol and show/sound an alarm. I've tried to show some of the thinking behind the project by laying it out 'as it happened' and there are a full set of python, arduino and PCB etc. files for implementation.</p><p><u>Level of difficulty:</u> Good, but not expert, Raspberry Pi skills required. Soldering skills = easy.</p><p>Most info on the interwebs about LoRa seems to point to the 'Things Network',  but what if we just want basic data transfer between 2 devices and don't need the whole world to witness our data? Peer to peer is quite possibly the answer.</p><p>In this case, a Raspberry Pi with a Dragonino LoRa/GPS hat will send data about the security state of a remote location (eg farm gate) to tell us if people are coming in or if someone has stolen one of our cows. The receiver is an Arduino MKRWAN 1300 which has a dedicated LoRa chip soldered onto it.  BE WARNED: This Arduino is a 3.3V device and will be destroyed by applying 5v to any (or most of) of the pins. Also, never operate either the Dragino hat or the Arduino device without an antenna attached! As far as code is concerned, both instances are really simple, although it took me a while to work out that I had to flash the Arduino with a firmware upgrade to get it to work properly. After plugging in the Dragonino hat, the Raspberry Pi was processed as follows:</p><pre>$ wget &lt;a href="https://codeload.github.com/dragino/rpi-lora-tranceiver/zip/master
$ cd rpi-lora-tranceiver-master/dragino_lora_app
$ make
$ cd rpi-lora-tranceiver-master/dragino_lora_app &&./dragino_lora_app
$ ./dragino_lora_app sender&lt;/p&gt;</pre><p>This data is NOT secure, but there are python scripts that can be used if needed.<br>NB. The RPi MUST have a proper power supply and SPI needs to be activated in the settings. OS used is Raspian stretch. Setting up the Arduino is just as easy. There's just a couple of things to watch out for: Firstly, the Rpi, in my case attempted to transmit 'HELLO' every 3 seconds on 868.1 MHz, so the Arduino needs to be configured accordingly ...... 868.1 MHz = 8681 x 105  = 8681E5. Other regions eg USA will use different sets of frequencies. Download Arduino lora libraries here: (both are required) </p><p><a href="https://github.com/sandeepmistry/arduino-LoRa">https://github.com/sandeepmistry/arduino-LoRa </a></p><p><a href="https://github.com/sandeepmistry/arduino-LoRa"></a> <a href="https://github.com/arduino-libraries/MKRWANAfter"> https://github.com/arduino-libraries/MKRWAN</a></p><p>After installing the libraries in the normal way, open the MKWAN example set and up load 'MKRWANFWUpdate_standalone' to the Arduino and open serial console. You should see the update as it progresses. Next, find the 'LoRa' example set and select 'LoRaReceiver' and upload. Dont forget to edit the frequency as mentioned before! Open the serial console and you should see the HELLO sent from RPI.</p><p><img src="https://cdn.hackaday.io/images/original/1062421544266394231.gif"> </p>
<ul>
<li>Arduino MKRWAN 1300 
<p><a href="https://uk.rs-online.com/web/p/products/1711859/">https://uk.rs-online.com/web/p/products/1711859/</a></p></li><li>
<p>Raspberry Pi 3 </p><p><a href="https://uk.rs-online.com/web/p/products/1373331/">https://uk.rs-online.com/web/p/products/1373331/</a></p></li><li>3 x RS PRO 5V Surface Mount Electromagnetic Buzzer, 97dB <br>
<p><a href="https://uk.rs-online.com/web/p/products/7542053/">https://uk.rs-online.com/web/p/products/7542053/</a></p></li><li>
<p>Switch. PCB Slide Switch Single Pole Double Throw (SPDT) Latching 3 A @ 120 V ac Top </p><p><a href="https://uk.rs-online.com/web/p/products/7347343/">https://uk.rs-online.com/web/p/products/7347343/</a></p></li><li>
<p>L293E. STMicroelectronics L293E, Brushed Motor Driver IC, 36 V 1A 20-Pin, PowerDIP </p><p><a href="https://uk.rs-online.com/web/p/products/8805298/">https://uk.rs-online.com/web/p/products/8805298/</a></p></li><li>
<p>Draganino Seeed Studio Raspberry Pi LoRa/GPS HAT-Support 868M Frequency 868MHz for SX1276/SX1278  </p><p><a href="https://uk.rs-online.com/web/p/products/1793739/">https://uk.rs-online.com/web/p/products/1793739/</a></p></li><li>
<p>PCB Antenna for Arduino </p><p><a href="https://uk.rs-online.com/web/p/gsm-gprs-antennas/7620052/">https://uk.rs-online.com/web/p/gsm-gprs-antennas/7...</a></p></li><li>
<p>Raspberry Pi PiNoir Camera V2 Camera Module, CSI-2, 3280 x 2464 Resolution  </p><p><a href="https://uk.rs-online.com/web/p/products/9132673/">https://uk.rs-online.com/web/p/products/9132673/</a></p></li><li>
<p>Logitech C930e Full HD Webcam </p><p><a href="https://uk.rs-online.com/web/p/products/7950870/">https://uk.rs-online.com/web/p/products/7950870/</a></p></li><li>
<p>Movidius Neural Network Compute Stick NCSM2450.DK1 </p><p><a href="https://uk.rs-online.com/web/p/products/1393655/">https://uk.rs-online.com/web/p/products/1393655/</a></p></li><li>
<p>USB extention cables   12CM USB 2.0 AM AF BLK EXT </p><p><a href="https://uk.rs-online.com/web/p/products/1216568/">https://uk.rs-online.com/web/p/products/1216568/</a></p></li><li>
<p>Case with transparent lid </p><p><a href="https://uk.rs-online.com/web/p/general-purpose-enclosures/0104212/">https://uk.rs-online.com/web/p/general-purpose-enc...</a></p></li><li>
<p>39 Ohm resistor</p></li></ul>

<img src="https://cdn.instructables.com/FQU/TAB2/JQ0SMJPU/FQUTAB2JQ0SMJPU.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FF5/0PK0/JQ0SMJPS/FF50PK0JQ0SMJPS.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FUO/H4VM/JQ0SMJPT/FUOH4VMJQ0SMJPT.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FP4/VTCI/JQ0SMHQ5/FP4VTCIJQ0SMHQ5.SQUARE3.jpg"> 

<img src="https://cdn.instructables.com/FUP/S480/JQ0SMIIR/FUPS480JQ0SMIIR.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FOL/GDJD/JQ0SMF6M/FOLGDJDJQ0SMF6M.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FPL/3ST6/JQ0SMF8P/FPL3ST6JQ0SMF8P.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FEZ/BVGW/JQ0SMF80/FEZBVGWJQ0SMF80.SQUARE3.jpg"> 

<img src="https://cdn.instructables.com/FQZ/P1JE/JQ0SMF5X/FQZP1JEJQ0SMF5X.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/F50/Z0V9/JQ0SMF7B/F50Z0V9JQ0SMF7B.SQUARE3.jpg"> 
<img src="https://cdn.instructables.com/FXX/1AOT/JQ0SMKD7/FXX1AOTJQ0SMKD7.SQUARE3.jpg"> 


<p>Since the neural network module using Python 3 i thought it would be a good idea to get the LoRa transmiiter hat on the Raspberry Pi, the Dragonino, to also be controlled using this version of Python. Fortunately, people have already done this and it's well documented here: <a href="https://github.com/mayeranalytics/pySX127x/issues/21"> https://github.com/mayeranalytics/pySX127x/issues...</a></p><p>However, there are a couple of extra steps that are skipped, so I'll write out the whole procedure here: </p><p>1. Remove the SD card from the RPi and insert it into a suitable PC. </p><p>2. Copy and paste the config.txt file from the /boot folder to your desktop folder. </p><p>3. Change the permissions using chmod 777 in command line, or whatever is convenient, and edit the file by adding: </p><pre>dtoverlay=spi0-cs,cs0_pin=25 </pre><p>to the very top. </p><p>4. Save, and paste back onto the SD card into boot again. This is the only way to quickly and easily edit this file! </p><p>5. Download the Python files from here: <a href="https://github.com/mayeranalytics/pySX127x"> https://github.com/mayeranalytics/pySX127x </a> , extract, and open up the 'board_config.py' in a text editor.  </p><p>6. Use the following values in board_config: </p><pre>DIO0 = 4     
DIO1 = 23     
DIO2 = 24     
DIO3 = 21     
LED = 18     
SWITCH = 7
</pre><p>...... Oh, I nearly forgot, if you're in Europe, we use 868 (ish) Mhz so where it says: </p><pre>low_band = true</pre><p>in board_config, this needs to be changed to 'false'. It's pretty self explanatory if you read the comments next to it. </p><p>7. Find the 'constants.py' file and edit it by adding the following, being careful to use exactly 4 spaces to be compatible with Python formatting: </p><pre>@add_lookup 
class SPI_BAUD_RATE: 
    MAX_SPEED_HZ = 5000 
@add_lookup 
class SPI_MODE:
    SPI_MODE = 0b01 </pre><p>8. Find the LoRa.py file and find the line: </p><pre>spi = BOARD.SpiDev()</pre><p>insert these lines right underneath it: </p><pre>spi.max_speed_hz = SPI_BAUD_RATE.MAX_SPEED_HZ </pre>
<pre>spi.mode = SPI_MODE.SPI_MODE </pre><p>9. Open a terminal and CD to the directory that contains the 'tx_beacon.py' file eg cd /home/pi/Desktop/dragonino/psySX127x-master/ </p><p>10. Where '869' is the frequency in MHz and '7' is the spreading factor, run the beacon program using:  python tx_beacon.py -f 869 -s 7 </p><p>11.  Tune the Arduino to 8690E5 and you should see something like this in the serial console: </p><p>Received packet ' ' with RSSI -33 </p><p>Received packet ' ' with RSSI -23 </p><p>Received packet ' ' with RSSI -33 </p><p>Received packet ' ' with RSSI -26 </p><p>Received packet ' ' with RSSI -25  </p><p>It's working! </p><p>12. If you want to see something a bit more meaningful, open 'tx_beacon.py' with text editor and, near line 65, find: </p><pre>self.write_payload([0x0f])</pre><p>Change this to: </p><pre>self.write_payload([0x57,0x68,0x61,0x74,0x20,0x74,0x68,0x65,0x20,0x66,0x75,0x63,0x6B,0x21]) </pre>
<p>I've not programmed in Python before, but compared to C++ it already seems much easier and a lot more intuitive.</p><p>I worked out that the Lora beacon was the probably right place to start tinkering and that it needed a 'list' of numbers that represent ANSII characters and that these can be decimal or hex values. The actual phrase in the beacon program that transmits the data is on line 65:</p><pre>self.write_payload(j)</pre><p>where j is the payload list, which would normally look something like this for 'Hello World':</p><pre>([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])</pre><p>To get 'Hello World' into this list format the following code is used:</p><pre>import array as arr&lt;br&gt;import numpy as np</pre>
 <pre>c= 'Hello World'
g = arr.array('i',[])
n=-1
for h in range(len(c)):
  g.extend([0]) 
for x in c:
  n = n+1
  y = ord(x)
  g[n] = y
print(g)
j = np.array(g).tolist()</pre><p>The code converts each of the characters in the string to an integer in an integer array, denoted by the letter 'i', of length c, corresponding to the number of characters and spaces in the string. The extend command extends the array to accept more integers. Next, for each of the characters in the string the 'ord' command does the actual character to integer transformation and 'g[n] = y' dumps it into the right place in the array. Last is the array to list command that turns the whole array into the list format. Simples! </p><p>The new LoRa beacon file is called Tegwyns_LoRa_Beacon in the files section of this blog and, assuming it's located in the same place as the original beacon file, it would be run from the command line with:</p><pre>cd /home/pi/Desktop/dragonino_python_fix/pySX127x-master/ && python3 Tegwyns_LoRa_Beacon.py -f 869 -s 7-</pre><p>At this stage it's a good idea, but not essential to use an SDR-RTL USB dongle to detect and analyse the transmitted signal using software like Cubic SDR and it's spectrum analyzer function.</p><p><img src="https://cdn.hackaday.io/images/original/1062421544266394231.gif"> </p>
<p>A couple of key things to note before getting started:</p><p>The correct Neural Compute stick for Raspberry Pi is the  NCSM2450.DK1 and currently (2018) no other Intel sticks will work on the  Pi.Be careful which version of the stick SDK or APi is downloaded - V2 and above is NOT for Raspbian stretch, only Ubuntu 16.04.</p><p>Instructions:</p><p>1. I installed the full version of the latetst version 1 of the SDK and the APi and it did not take too long to install:</p> <pre>$ sudo apt-get update
$ sudo apt-get install
$ git clone https://github.com/movidius/ncsdk.git
$ cd /home/pi/ncsdk && sudo make install
$ cd /home/pi/ncsdk && sudo make examples
</pre>
2.  Test that the stick is working ok: <pre>$ git clone https://github.com/movidius/ncappzoo
$ cd /home/pi/ncappzoo/apps/hello_ncs_py
$ python3 hello_ncs.py 
</pre><p>3. Download this file: https://cdn.hackaday.io/files/1626676959544928/graph and paste it into the /home/pi/ncappzoo/caffe/SSD_MobileNet folder. Do not change it's name or extention.</p>4. Make and run the demo using the following commands: <pre>$ cd /home/pi/ncappzoo/apps/security-cam
$ make run
</pre><p>..... Obviously a camera is required. Mine is a USB logitech and it worked straight away.</p>
<p>It's been a bit of a battle, with a steep Python learning curve, but <br>finally I created a single Python file that enables a time stamp,  detection class, confidence and bounding box coordinates to be sent to  the Arduino base station. Obviously, there's still a number of  dependancies in various directories - some close by and others deeply  embedded in the Python system somewhere, but here's my 'top of the  stack' code:</p> <pre>#!/usr/bin/python3

# ****************************************************************************
# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.
# ****************************************************************************

# Detect objects on a LIVE camera feed using and send data over LoRa network
# Intel® Movidius™ Neural Compute Stick (NCS)

import os
import cv2
import sys
import numpy
import ntpath
import argparse

import mvnc.mvncapi as mvnc

from time import localtime, strftime
from utils import visualize_output
from utils import deserialize_output
from pySX127x_master import basic_test01

import datetime
import array as arr
import numpy as np
from time import sleep


from pySX127x_master.SX127x.LoRa import *
from pySX127x_master.SX127x.LoRaArgumentParser import LoRaArgumentParser
from pySX127x_master.SX127x.board_config import BOARD

#from pySX127x_master import Tegwyns_LoRa_Beacon

BOARD.setup()

parser = LoRaArgumentParser("A simple LoRa beacon")
parser.add_argument('--single', '-S', dest='single', default=False, action="store_true", help="Single transmission")
parser.add_argument('--wait', '-w', dest='wait', default=1, action="store", type=float, help="Waiting time between transmissions (default is 0s)")

myString = ""
#from pySX127x_master.Tegwyns_LoRa_Beacon import *

class LoRaBeacon(LoRa):

    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([1,0,0,0,0,0])
        
    def on_rx_done(self):
        print("\nRxDone")
        print(self.get_irq_flags())
        print(map(hex, self.read_payload(nocheck=True)))
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_cad_done(self):
        print("\non_CadDone")
        print(self.get_irq_flags())

    def on_rx_timeout(self):
        print("\non_RxTimeout")
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
        global args
        sys.stdout.write("\rstart\r")
        stamp = str(datetime.datetime.now())
        text=bytearray('PING LoRa Test PI: ' + stamp + ('  ') + myString,'utf-8')
        self.write_payload([0x00, 0x00, 0x00, 0x00] + list(text))
        self.set_mode(MODE.TX)
        
lora = LoRaBeacon(verbose=False)
args = parser.parse_args(lora)

lora.set_pa_config(pa_select=1)
#lora.set_rx_crc(True)
#lora.set_agc_auto_on(True)
#lora.set_lna_gain(GAIN.NOT_USED)
#lora.set_coding_rate(CODING_RATE.CR4_6)
#lora.set_implicit_header_mode(False)
#lora.set_pa_config(max_power=0x04, output_power=0x0F)
#lora.set_pa_config(max_power=0x04, output_power=0b01000000)
#lora.set_low_data_rate_optim(True)
#lora.set_pa_ramp(PA_RAMP.RAMP_50_us)

#print(lora)
#assert(lora.get_lna()['lna_gain'] == GAIN.NOT_USED)
assert(lora.get_agc_auto_on() == 1)

print("Security cam config:")
print("  Wait %f s" % args.wait)
print("  Single tx = %s" % args.single)
print("")
                    
lora.start()

# "Class of interest" - Display detections only if they match this class ID
CLASS_PERSON         = 15

# Detection threshold: Minimum confidance to tag as valid detection
CONFIDANCE_THRESHOLD = 0.60 # 60% confidant

# Variable to store commandline arguments
ARGS                 = None

# OpenCV object for video capture
camera               = None

# ---- Step 1: Open the enumerated device and get a handle to it -------------

def open_ncs_device():

    # Look for enumerated NCS device(s); quit program if none found.
    devices = mvnc.EnumerateDevices()
    if len( devices ) == 0:
        print( "No devices found" )
        quit()

    # Get a handle to the first enumerated device and open it
    device = mvnc.Device( devices[0] )
    device.OpenDevice()

    return device

# ---- Step 2: Load a graph file onto the NCS device -------------------------

def load_graph( device ):

    # Read the graph file into a buffer
    with open( ARGS.graph, mode='rb' ) as f:
        blob = f.read()

    # Load the graph buffer into the NCS
    graph = device.AllocateGraph( blob )

    return graph

# ---- Step 3: Pre-process the images ----------------------------------------

def pre_process_image( frame ):

    # Resize image [Image size is defined by choosen network, during training]
    img = cv2.resize( frame, tuple( ARGS.dim ) )

    # Convert RGB to BGR [OpenCV reads image in BGR, some networks may need RGB]
    if( ARGS.colormode == "rgb" ):
        img = img[:, :, ::-1]

    # Mean subtraction & scaling [A common technique used to center the data]
    img = img.astype( numpy.float16 )
    img = ( img - numpy.float16( ARGS.mean ) ) * ARGS.scale

    return img

# ---- Step 4: Read & print inference results from the NCS -------------------

def infer_image( graph, img, frame ):
    #from pySX127x_master.Tegwyns_LoRa_Beacon import LoRaBeacon
    #from pySX127x_master import Tegwyns_LoRa_Beacon
    # Load the image as a half-precision floating point array
    graph.LoadTensor( img, 'user object' )

    # Get the results from NCS
    output, userobj = graph.GetResult()

    # Get execution time
    inference_time = graph.GetGraphOption( mvnc.GraphOption.TIME_TAKEN )

    # Deserialize the output into a python dictionary
    output_dict = deserialize_output.ssd( 
                      output, 
                      CONFIDANCE_THRESHOLD, 
                      frame.shape )

    # Print the results (each image/frame may have multiple objects)
    for i in range( 0, output_dict['num_detections'] ):

        # Filter a specific class/category
        if( output_dict.get( 'detection_classes_' + str(i) ) == CLASS_PERSON ):

            cur_time = strftime( "%Y_%m_%d_%H_%M_%S", localtime() )
            print( "Person detected on " + cur_time )
            print(".... Press q to quit ..... ")

            # Extract top-left & bottom-right coordinates of detected objects 
            (y1, x1) = output_dict.get('detection_boxes_' + str(i))[0]
            (y2, x2) = output_dict.get('detection_boxes_' + str(i))[1]
            #print (y1, x1)
            # Prep string to overlay on the image
            display_str = ( 
                labels[output_dict.get('detection_classes_' + str(i))]
                + ": "
                + str( output_dict.get('detection_scores_' + str(i) ) )
                + "%" )
            print (display_str)
            print (y1, x1)
            print (y2, x2)
            # Overlay bounding boxes, detection class and scores
            frame = visualize_output.draw_bounding_box( 
                        y1, x1, y2, x2, 
                        frame,
                        thickness=4,
                        color=(255, 255, 0),
                        display_str=display_str )
            global myString
            myString = display_str + " , " + "(" + str(y1) + "," + str(x1) +")" + "," + "(" + str(y2) + "," + str(x2) +")"
            
###########################################################################################
            lora.start()
###########################################################################################

            # Capture snapshots
            photo = ( os.path.dirname(os.path.realpath(__file__))
                      + "/captures/photo_"
                      + cur_time + ".jpg" )
            cv2.imwrite( photo, frame )

    # If a display is available, show the image on which inference was performed
    if 'DISPLAY' in os.environ:
        cv2.imshow( 'NCS live inference', frame )
        
# ---- Step 5: Unload the graph and close the device -------------------------

def close_ncs_device( device, graph ):
    graph.DeallocateGraph()
    device.CloseDevice()
    camera.release()
    cv2.destroyAllWindows()

# ---- Main function (entry point for this script ) --------------------------

def main():

    device = open_ncs_device()
    graph = load_graph( device )

    # Main loop: Capture live stream & send frames to NCS
    while( True ):
        ret, frame = camera.read()
        img = pre_process_image( frame )
        infer_image( graph, img, frame )

        # Display the frame for 5ms, and close the window so that the next
        # frame can be displayed. Close the window if 'q' or 'Q' is pressed.
        if( cv2.waitKey( 5 ) & 0xFF == ord( 'q' ) ):
            break

    close_ncs_device( device, graph )

# ---- Define 'main' function as the entry point for this script -------------

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                         description="DIY smart security camera PoC using \
                         Intel® Movidius™ Neural Compute Stick." )

    parser.add_argument( '-g', '--graph', type=str,
                         default='../../caffe/SSD_MobileNet/graph',
                         help="Absolute path to the neural network graph file." )

    parser.add_argument( '-v', '--video', type=int,
                         default=0,
                         help="Index of your computer's V4L2 video device. \
                               ex. 0 for /dev/video0" )

    parser.add_argument( '-l', '--labels', type=str,
                         default='../../caffe/SSD_MobileNet/labels.txt',
                         help="Absolute path to labels file." )

    parser.add_argument( '-M', '--mean', type=float,
                         nargs='+',
                         default=[127.5, 127.5, 127.5],
                         help="',' delimited floating point values for image mean." )

    parser.add_argument( '-S', '--scale', type=float,
                         default=0.00789,
                         help="Absolute path to labels file." )

    parser.add_argument( '-D', '--dim', type=int,
                         nargs='+',
                         default=[300, 300],
                         help="Image dimensions. ex. -D 224 224" )

    parser.add_argument( '-c', '--colormode', type=str,
                         default="bgr",
                         help="RGB vs BGR color sequence. This is network dependent." )

    ARGS = parser.parse_args()

    # Create a VideoCapture object
    camera = cv2.VideoCapture( ARGS.video )

    # Set camera resolution
    camera.set( cv2.CAP_PROP_FRAME_WIDTH, 620 )
    camera.set( cv2.CAP_PROP_FRAME_HEIGHT, 480 )

    # Load the labels file
    labels =[ line.rstrip('\n') for line in
              open( ARGS.labels ) if line != 'classes\n']

    main()

# ==== End of file ===========================================================
</pre>
<p>Obviously, we're going to want to use this gadget in the dark with <br>infra red lights, so we need a decent camera with IR capabilities ie no  IR filter. Fortunately, these cameras are a lot cheaper an more compact  than the Logitech USB and they're also very easy to install:</p><p>Firstly, check that camera is enabled in the RPi settings and then, after plugging it into the board, check it works with:</p> <pre>$ raspistill -o image.jpg
</pre>
Next install the following Python dependencies <pre>$ sudo apt-get install python3-picamera
$ pip3 install "picamera[array]"
$ pip3 install imutils
</pre><p> Lastly, use the Pi cam version of the security_cam file, downloadable from here: <a href="https://cdn.hackaday.io/files/1626676959544928/security_camPiCam.py"> https://cdn.hackaday.io/files/1626676959544928/se...</a></p>Run the file using the following command: <pre>$ cd && cd /home/pi/ncappzoo/apps/securityCam && python3 security_camPiCam.py
</pre><p>The security camera is now ready to test out in the wild, although obviously not in the rain! It'll be interesting to see what the transmitter range will be with a decent antenna :) </p><p>One thing to note is that the Noire camera gives very different colour balance reults than the USB camera and this is perfectly normal due to the lack of IR filter on the lens.</p><p>Other than waterproofing, another issue is where to collect the captured photos produced when the device spots a person - maybe a USB stick, to prevent filling up the raspberry Pi SD card?</p>
<p>The security cam Python file can be easily adapted to save the repeated <br>snapshots of detected people by modifying line 235 to something like the  following, where my USB drive is called 'KINSTON':</p> <pre>photo = ( "/media/pi/KINGSTON" + "/captures/photo_" + cur_time + ".jpg" )
</pre>
 In reality, using this USB stick slowed down the program rather drastically! Images can be transferred / deleted easily from the Pi if another PC is used to SSH into the Pi once it's deployed.
 <p>Other than the Arduino MKRWAN 1300, the PCB features a L293E <br>chip for stepping up the voltage and current required for the alarm  system, which is itself a block of 8 LEDs and 3 buzzer beeper chips.  Attempting to run these devices directly off the Arduino would instantly  frazzle the device!After assembly and testing, the whole  thing worked perfectly and, after a bit of experimentation, the best  resister for the red LEDs was 39 Ohms.</p><p>Although most of the components are surface mount, they are all very <br>large and no stencil is required. After checking the polarity of the  LEDs, the PCB was pasted up with solder, populated with the surface  mount components and chucked in the toaster oven for cooking to 260  degrees C. Using a hot air gun is possible, but not recommended.</p>
 <p>As can be seen, this unit is very easy to assemble and just needed to be<br> located in a waterproof case with a transparent front ( <a href="https://uk.rs-online.com/web/p/general-purpose-enclosures/0104212/"> https://uk.rs-online.com/web/p/general-purpose-en...</a> ) . The above components were wedged tightly into the box using thick cardboard and a bit of judicious Origami.</p><p>NB. The camera MUST be up the right way round for the neural network to work properly.</p>
 <p>Nothing too fancy about the code, except I wanted the tone of the beeper<br> to change according to how close the detected person was to the camera.  This would be useful for discerning the difference between someone  posting a letter in the postbox and someone actually walking up the  drive. The code uses string analysis functions to, firstly, confirm that  the data is coherent by searching for the word 'Box' and then finding  the two pairs of coordinates that represent the detection box. If the  detected person is close to the camera, the area of the detection box is  greater and the resulting alarm tone is of higher frequency:</p> <pre>#include 
#include 
String myString =" ";
String myStringReversed =" ";

void setup() 
{
  pinMode(4, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  tone(5,1000,1000);
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(4, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(4, LOW);
  Serial.begin(9600);
//  while (!Serial);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(8690E5)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() 
{
  //delay (1000);
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) 
  {
    // received a packet
    Serial.print("Received packet '");
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(4, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(4, LOW);
    // read packet
    myString =" ";
    myStringReversed =" ";
    int i = 0;
    char c;
    while (LoRa.available()) 
    {
      //c[i] = (char)LoRa.read();
      //Serial.print((char)LoRa.read());
      myString = (char)LoRa.read() + myString;
      i++;
      //Reverse the string:
      c = myString.charAt(0);
      myStringReversed = myStringReversed + c;
    }
    processString();
    //Serial.print("My string: ");Serial.print(myString);
    // print RSSI of packet
    //Serial.print("' with RSSI ");
    //Serial.println(LoRa.packetRssi());

  }
}
void processString()
{
    Serial.print("My string reversed:");Serial.print(myStringReversed);
    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
    int len = myStringReversed.length();
    int j=0;
    char a,b,c,d;
    String coord1 = " ";
    String coord2 = " ";
    String coord3 = " ";
    String coord4 = " ";
    int k =0;
    char x = ',';
    int z=1;
    int y=1;
    int r=1;
    int s=1;
    int v=0;
    while (j &lt; len) 
    {
      a = myStringReversed.charAt(j);
      b = myStringReversed.charAt(j+1);
      c = myStringReversed.charAt(j+2);
      if((a=='B')&&(b=='o')&&(c=='x'))                           // The word 'box' has been identified in the string - k is now greater than 0.
      {
        k = j+5;
        Serial.print("Character B was found at: ");Serial.println(j);
      }
      j++;
    }
    if (k&gt;0)
    {
      v =0;                                                      // int V stops perpetual loops occurring.
      while((z==1)&&(v&lt;200))
      {
        if(myStringReversed.charAt(k)==x)                        // Build up string 'coord' until a comma is reached.
        {
          Serial.print("k");Serial.println(k);
          z=0;
        }
        else
        {
        coord1 = coord1 + myStringReversed.charAt(k);
        k++;
        v++;
        //Serial.print("coord1: ");Serial.println(coord1); 
        }
      } 
      v =0; 
      k++;
      while((y==1)&&(v&lt;200))
      {
        if(myStringReversed.charAt(k)==')')                        // Build up string 'coord' until a comma is reached.
        {
          Serial.print("k");Serial.println(k);
          y=0;
        }
        else
        {
        coord2 = coord2 + myStringReversed.charAt(k);
        k++;
        v++;
        //Serial.print("coord2: ");Serial.println(coord2); 
        }
      }  
      v =0;
      k=k+3;                                                     // Takes account of two brackets and a comma.
      while((r==1)&&(v&lt;200))
      {
        if(myStringReversed.charAt(k)==x)                        // Build up string 'coord' until a comma is reached.
        {
          Serial.print("k");Serial.println(k);
          r=0;
        }
        else
        {
        coord3 = coord3 + myStringReversed.charAt(k);
        k++;
        v++;
        //Serial.print("coord3: ");Serial.println(coord3); 
        }
      }  
      v =0;
      k++;
      while((s==1)&&(v&lt;200))
      {
        if(myStringReversed.charAt(k)==')')                        // Build up string 'coord' until a comma is reached.
        {
          Serial.print("k");Serial.println(k);
          s=0;
        }
        else
        {
        coord4 = coord4 + myStringReversed.charAt(k);
        k++;
        v++;
        //Serial.print("coord4: ");Serial.println(coord4); 
        }
      }  
    }
    Serial.print("coord1: ");Serial.println(coord1);
    Serial.print("coord2: ");Serial.println(coord2);
    Serial.print("coord3: ");Serial.println(coord3);
    Serial.print("coord4: ");Serial.println(coord4);
    int coord10 = coord1.toInt();
    int coord20 = coord2.toInt();
    int coord30 = coord3.toInt();
    int coord40 = coord4.toInt();
    
    int area = (coord40 - coord20) * (coord30 - coord10);
    tone(5,(area/100)+200,100);
    Serial.print("Box area: ");Serial.println(area);
}
</pre>
<p>The 'security_cam.py' file is a generic 'live-object-detection' <br>script and can be modified very easily to detect a total of 20 different  objects. </p><p>If we look at line 119:</p> <pre># "Class of interest" - Display detections only if they match this class ID
CLASS_PERSON         = 15
</pre>
 To detect dogs, just change this to:  <pre># "Class of interest" - Display detections only if they match this class ID
CLASS_DOG         = 12
</pre>
 Also, line 200 needs to be changed as well: <pre>        # Filter a specific class/category
        if( output_dict.get( 'detection_classes_' + str(i) ) == CLASS_PERSON ):
</pre>
 Although the person class worked really well and was quite impressive, the dog class was a little bit underwhelming and not nearly as good as some of the other models I've tested. Nonetheless, here's the full list of classes available with this model:      Aeroplane     Bycycle     Bird     Boat     Bottle     Bus     Car     Cat     Chair     Cow     Diningtable     Dog     Horse     Motorbike     Person     Pottedplant     Sheep     Sofa     Train     TVmonitor
 
