from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)
'''
Created on 04-May-2013

@author: Manuj
'''
