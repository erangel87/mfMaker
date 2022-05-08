#!/usr/bin/env python3

import readline
from pyfiglet import Figlet
from interprets.commands import *
from completer.completer import Completer


completer = Completer(commands)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
f = Figlet(font='slant')
c_input = ''
enter_key = ''
word = 'MF\n   MAKER'


print(f.renderText(word))
while c_input != 'exit':
    try:
        c_input = input("@@/mf_maker>>")
        input_sp = c_input.split(" ")
        if c_input == enter_key:
            continue
        if input_sp[0] in commands:
            interpreter(c_input)
        else:
            print(f"Unknown command <{c_input}>")
    except:
      print(f"Unknown command <{c_input}>") if  c_input != 'exit' else exit(0)
