#!/usr/bin/python3
import keyboard

print("=========== Key Logger ===========")

keys = keyboard.record(until = 'ENTER')
keyboard.play(keys)
