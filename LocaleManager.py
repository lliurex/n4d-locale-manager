#!/usr/bin/python

import n4d.responses

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
                    if (len(tokens)==2):
                        tokens.append("")
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
        return self.set_locale_base(locale, "/")
    
    def set_locale_base(self,locale, basepath):
        locale_region = locale if "valencian" no in locale else locale.split("@")[0]
        data=self.read_file(basepath + "etc/default/locale")
        self.set_value(data,"LANG",locale)
        self.set_value(data,"LC_ADDRESS",locale_region)
        self.set_value(data,"LC_IDENTIFICATION",locale_region)
        self.set_value(data,"LC_MEASUREMENT",locale_region)
        self.set_value(data,"LC_MONETARY",locale_region)
        self.set_value(data,"LC_NAME",locale_region)
        self.set_value(data,"LC_NUMERIC",locale_region)
        self.set_value(data,"LC_PAPER",locale_region)
        self.set_value(data,"LC_TELEPHONE",locale_region)
        self.set_value(data,"LC_TIME",locale_region)
        self.write_file("/etc/default/locale",data)
        
        return n4d.responses.build_successful_call_response()
    
    
    def set_keyboard(self,layout,variant):
        data=self.read_file("/etc/default/keyboard")
        self.set_value(data,"XKBLAYOUT",layout)
        self.set_value(data,"XKBVARIANT",variant)
        self.write_file("/etc/default/keyboard",data)
        
        return n4d.responses.build_successful_call_response()
