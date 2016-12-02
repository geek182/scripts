#!/usr/bin/python
class ShowName(object):

    def __init__(self, firstname):
       self.firstname = firstname

    def GetName(self):
        print "teste:",  self.firstname


myname = ShowName("Leandro")
myname.GetName()
