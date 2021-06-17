#!/usr/bin/python

import os
import shlex

UNKNOWN=0
ASSIGNMENT=1

def read_file(path):
    data=[]
    f=open(path,"r")
    
    for line in f.readlines():
        tokens=list(shlex.shlex(line,posix=True))
        if (len(tokens)>0):
            if (tokens[1]=="="):
                data.append([ASSIGNMENT,tokens])
            else:
                data.append([UNKNOWN,line])
        else:
            data.append([UNKNOWN,line])
        
    f.close()
    
    return data

def write_file(path,data):
    f=open(path,"w")
    for line in data:
        if(line[0]==ASSIGNMENT):
            f.write("{0}={1}\n".format(line[1][0],line[1][2]))
        else:
            f.write(line[1])
    f.close()

def set_value(data,name,value):
    setted=False
    
    for line in data:
        if (line[0]==ASSIGNMENT and line[1][0]==name):
            line[1][2]=value
            setted=True
            break
        
    if not setted:
        data.append([ASSIGNMENT,[name,"=",value]])

def set_locale(locale):
    data=read_file("/etc/default/locale")
    set_value(data,"LANG",locale)
    set_value(data,"LC_ADDRESS",locale)
    set_value(data,"LC_IDENTIFICATION",locale)
    set_value(data,"LC_MEASUREMENT",locale)
    set_value(data,"LC_MONETARY",locale)
    set_value(data,"LC_NAME",locale)
    set_value(data,"LC_NUMERIC",locale)
    set_value(data,"LC_PAPER",locale)
    set_value(data,"LC_TELEPHONE",locale)
    set_value(data,"LC_TIME",locale)
    write_file("/etc/default/locale",data)

def set_keyboard(layaout,variant):
    data=read_file("/etc/default/keyboard")
    set_value(data,"XKBLAYOUT",layout)
    set_value(data,"XKBVARIANT",variant)
    write_file("/etc/default/keyboard",data)

