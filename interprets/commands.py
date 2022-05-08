from usage.text import usage
import os
import os.path
from os import path
import re
from runner.run import run

commands = ["options", "help", "run", "set_project_path", "set_flags", "set_standard", "set_program_name", "exit", "clear"]
standards = ["-std=c17", "-std=c11", "-std=99", "-std=90", "-std=gnu17", "-std=gnu11",
             "-std=gnu99", "-std=gnu98", "-std=gnu90", "-std=c++17", "-std=c++14", "-std=c++11", "-std=c++198"]

D_PROGRAM = "main"
PROGRAM = D_PROGRAM
D_FLAGS = "-g -Wall"
FLAGS = D_FLAGS
LM_FLAG = ''
proj_path = "<Required>"
d_standard = "system default - recommended"
standard = d_standard
use_ml = "NO"


def interpreter(command) ->str:
    command_split = command.split(" ")    # split command, set_project_path /home/ubuntu/Desktop -> [set_project_path, /home/ubuntu/Desktop].
    c = command_split.copy()              
    c_a = get_next_section_in_command(c)  # command_argument.  
    command_word = command_split[0]
    if command_word == commands[0]:       # commands[0] -> options  |
        options_c()                       #                        \|/
    
    elif command_word == commands[1]:
        help_c()

    elif command_word == commands[2]:
        run(PROGRAM, FLAGS, proj_path, standard, LM_FLAG)

    elif command_word == commands[3]:
        set_project_path_c(c_a)

    elif command_word == commands[4]:
        set_flags_c(c)

    elif command_word == commands[5]:
        set_standard_c(c_a)

    elif command_word == commands[6]:
        set_program_name_c(c_a)

    elif command_word == commands[7]:
        exit_c()

    elif command_word == 'clear':
        clear_c()
    else:
        print(f"Unknown command <{command_word}>")
    

def options_c():
    print(f"\n\tProject Path:\t\t{proj_path}\n\n\tProgram Name:\t\t{PROGRAM}\n\n\t"\
    f"Flags To Use:\t\t{FLAGS}\n\n\tUsing math.h:\t\t{use_ml}\n\n\tStandard:\t\t{standard}\n")
    # printf"\n\tName     Current Setting  Required                                      \
    # \n\t--------     ---------------  --------"                                        \
    # "\n\tProject Path: {proj_path} yes"                                                \
    # "\n\tFlags To Use: {FLAGS}     no"                                                 \
    # "\n\tProgram Name: {PROGRAM}   no"                                                 \
    # "\n\tStandard    : {standard}  no\n")                                               

def help_c():
    print(usage)

def run_c():
    pass

def set_project_path_c(dir_path):
    global proj_path
    if os.path.isdir(dir_path):
        proj_path = dir_path + '.'[:-1]
    else:
        if dir_path == '' or dir_path == 'set_project_path':
            print('Error: missing arguments')
        else:
            print("cannot access the specified path, try to correct the project path")


def set_flags_c(flags):
    global FLAGS, LM_FLAG, use_ml
    FLAGS = ''
    for flag in flags:
        FLAGS += flag + ' '
    FLAGS = ' '.join(FLAGS.split())
    if FLAGS == '' or FLAGS == 'set_flags':
        print('Error: missing arguments')
        FLAGS = D_FLAGS
    if '-lm' in FLAGS:
        FLAGS = FLAGS.replace("-lm", "")
        LM_FLAG = "Y"
        use_ml = "YES"


  

def set_standard_c(stand):
    global standard
    standard = ''
    standard = stand
    if standard not in standards:
        print(f"Unknown standard < {stand} >")
        standard = d_standard



def set_program_name_c(p_name):
    global PROGRAM
    PROGRAM = ''
    PROGRAM = p_name
    if PROGRAM == '' or PROGRAM == 'set_program_name':
        print('Error: missing arguments')
        PROGRAM = D_PROGRAM


def exit_c():
    exit(0)


def clear_c():
    clear = lambda: os.system('clear')
    clear()


def get_next_section_in_command(c_array) -> str:
    if len(c_array) > 1:
        c_array.pop(0)
        for c in c_array:
            if c != '' and c != ' ':
                return c
    return c_array[0]