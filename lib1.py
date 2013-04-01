##########!/usr/bin/python
##coding:utf-8
def echo(str):
    print str
    
def echo2(str):
    print str    
    
class log:
    print("Начало определения методов")
    def __init__(self,file):
	print "file init"
    def log1(self,str):
	print str
    
    def logtest(self):
	self.log1("test")
	
    