# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
import os
import subprocess

setup(  name             = "n4d-locale-manager",
        version          = "1.0",
        author           = "Enrique Medina Gremaldos",
        author_email     = "quiqueiii@gmail.com",
        url              = "https://github.com/lliurex/n4d-locale-manager",
        data_files  =   [("/usr/share/n4d/python-plugins/",["LocaleManager.py"]),
                        ("/etc/n4d/conf.d/",["LocaleManager.json"])
                        ]
        
     )
