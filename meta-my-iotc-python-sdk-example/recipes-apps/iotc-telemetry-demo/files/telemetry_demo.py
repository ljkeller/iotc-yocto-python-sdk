#!/usr/bin/env python3
'''
    Basic sample loading credentials from file and sending data to endpoint
'''
import time
import sys
from model.JsonDevice import JsonDevice


def main(argv):
    '''Main function'''
    
    CREDENTIALS_PATH = argv[1:][0]
    device = JsonDevice(CREDENTIALS_PATH)
    device.connect()

    while True:
        data_sent = device.send_device_states()
        print(data_sent)
        time.sleep(10)

if __name__ == "__main__":
    main(sys.argv)
