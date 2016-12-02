#!/usr/bin/python
class ShowName(object):

    def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname

    def GetName(self):
        print "teste:",  self.firstname, self.lastname


myname = ShowName("Leandro", "Azevedo")
myname.GetName()
