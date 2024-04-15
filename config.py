# Config: command line arguments for the program

import argparse

class Config:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ramfile", "-r")
        parser.add_argument("--address", "-a")
        args = parser.parse_args()

        # --ramfile path, -r path
        # Path to the MEM1 RAM dump
        if args.ramfile is not None:
            self.dump_path = args.ramfile
        else:
            self.dump_path = "ram.raw"

        # --address addr, -a addr
        # Address of the string to disassemble
        if args.address is not None:
            self.addr = int(args.address, 16)
        else:
            self.addr = int(input("addr: "), 16)
