# String Disassembler
A tool that takes a memory address of a string and shows you the string at that address via a ram.raw ram dump
Useful for quickly getting strings without needing access to the SPM ghidra server
Uses the binread library and config from Seeky's [evt-disassembler](https://github.com/SeekyCt/evt-disassembler/tree/master)

## How to use
Place a valid ram.raw file in the folder, then run main.py and enter the string's memory address
