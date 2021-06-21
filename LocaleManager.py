#!/usr/bin/python

import os
import shlex

class LocaleManager:
    UNKNOWN=0
    ASSIGNMENT=1

    def read_file(self,path):
        data=[]
        f=open(path,"r")
        
        for line in f.readlines():
            tokens=list(shlex.shlex(line,posix=True))
            if (len(tokens)>0):
                if (tokens[1]=="="):
                    data.append([self.ASSIGNMENT,tokens])
                else:
                    data.append([self.UNKNOWN,line])
            else:
                data.append([self.UNKNOWN,line])
            
        f.close()
        
        return data

    def write_file(self,path,data):
        f=open(path,"w")
        for line in data:
            if(line[0]==self.ASSIGNMENT):
                f.write("{0}={1}\n".format(line[1][0],line[1][2]))
            else:
                f.write(line[1])
        f.close()

    def set_value(self,data,name,value):
        setted=False
        
        for line in data:
            if (line[0]==self.ASSIGNMENT and line[1][0]==name):
                line[1][2]=value
                setted=True
                break
            
        if not setted:
            data.append([self.ASSIGNMENT,[name,"=",value]])

    def set_locale(self,locale):
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

    def set_keyboard(self,layaout,variant):
        data=read_file("/etc/default/keyboard")
        set_value(data,"XKBLAYOUT",layout)
        set_value(data,"XKBVARIANT",variant)
        write_file("/etc/default/keyboard",data)
