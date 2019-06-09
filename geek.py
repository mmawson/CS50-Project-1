#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
@author: mattmawson
"""

class Geek:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def __str__(self):
#        print(f"Id: {self.id}")
#        print(f"Name: {self.name}")
#        print(f"Password {self.password}")
        return f"Id: {self.id}" + "\n" + f"Name: {self.name}" + "\n" + f"Password: {self.password}"
