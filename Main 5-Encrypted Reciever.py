# terminal_controlled_bot_wireless

from microbit import *
import radio
# ascii_shift_cipher
 
from microbit import *
 
key = -5
 
def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result

from cyberbot import *
import radio

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        packet = ascii_shift(key, packet)
        print("Receive: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
        radio.send(packet)
        print("Send Encrypted: ", )
        print(packet)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")