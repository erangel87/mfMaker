import os
import os.path
from os import path
import shutil


def copy_project_files(main_dir_path) -> str:
    """
    copy all input project files to outPut folder path
    """
    src = main_dir_path
    trg = 'outPut'
    files = os.listdir(src)

    for fname in files:
        if os.path.isfile(f"{main_dir_path}/{fname}"):
            shutil.copy2(os.path.join(src, fname), trg)


def del_files():
    """
    delete all files from outPut folder
    """
    trg = 'outPut'
    files = os.listdir(trg)

    for fname in files:
        file_path = f'{trg}/{fname}'
        os.remove(file_path)


def objs_field(objs) -> str:
    trg = 'outPut'
    files = os.listdir(trg)
    i = 0
    for fname in files:
        if '.c' in fname:
            fname = fname[:-2]
            if i == 0:
                objs += f'\t\t{fname}.o\\\n'
                i = -2
            else:
                objs += f'\t\t\t{fname}.o\\\n'
    if objs == "":
        print("There is no .c files in this directory")
        return -1
    return objs


def list_field(list_t) -> list:
    trg = 'outPut'
    files = os.listdir(trg)
    i = 0
    for fname in files:
        if '.c' in fname:
            fname = fname[:-2]
            fname += '.o'
            list_t.append(fname)
    if not list_t:
        print("There is no .c files in this directory")
        return -1
    return list_t


def header_field(h_file) -> str:
    trg = 'outPut'
    files = os.listdir(trg)
    for fname in files:
        if '.h' in fname:
            h_file += fname + " "
    return h_file


def m_maker(program, obgs, objs_list, cc, flags, lm_flag, header) -> str:
    make_file = ""

    if lm_flag == 'Y':
        lm_flag = '-lm'
    else:
        lm_flag = ''

    make_file += f'PROGRAM := {program}\nOBJS :={obgs}\n\nCC := {cc}\nFLAGS := {flags}\nHEADER := {header}'
    make_file += f"\n\n$(PROGRAM):	$(OBJS)\n\tgcc $(FLAGS) $(OBJS) -o $@ {lm_flag}"

    line = ''
    c_file = ''
    for obj in objs_list:
        c_file = obj[:-2]
        c_file += ".c"
        line += f'\n\n{obj}:\t {c_file} *h\n\tgcc -c $(FLAGS) $< -o $@ {lm_flag}'
        make_file += line
        line = ''

    make_file += '\n\nclean:\n\trm -rf $(OBJS) $(PROGRAM)'
    print("Makefile created successfully")
    return make_file

