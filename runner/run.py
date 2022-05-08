from ast import Global
from utilities.readWriteActions import *
from os.path import exists
import os

ERROR = -1
OBJS = ""
OBJS_LIST = []
HEADER = ""
CC = "gcc"

def run (program, flags, proj_path, standard, lm_flag):

    global OBJS, OBJS_LIST, HEADER, CC
    if proj_path == '<Required>' or proj_path == '':
        print("Project path required")
        return
    
    del_files()
    reset()
    copy_project_files(proj_path)

    E1 = OBJS = objs_field(OBJS)
    E2 = OBJS_LIST = list_field(OBJS_LIST)
    HEADER = header_field(HEADER)

    if E1 == ERROR or E2 == ERROR:
        return

    if exists(f"{proj_path}/Makefile"):
        os.remove(f"{proj_path}/Makefile")
    f = open(f"{proj_path}/Makefile", "x")
    f.write(m_maker(program, OBJS, OBJS_LIST, CC, flags, lm_flag, HEADER))


def reset():
    global OBJS, OBJS_LIST, HEADER
    OBJS = ""
    OBJS_LIST = []
    HEADER = ""
