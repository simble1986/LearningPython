#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ltxu

import sys,json,yaml,csv
from optparse import OptionParser
reload(sys)
sys.setdefaultencoding('utf8')

class DataParse(object):
    def __init__(self,dataFile):
        self.dataFile = dataFile
        self.data = None

    def getFileType(self): 
        return self.dataFile.split('.')[1]

    def jsonParse(self):
        f = open(self.dataFile,'r')
        self.data = json.load(f)
        f.close()
#       return self.data 可写可不写
    
    def csvParse(self):
        f = open(self.dataFile,'rb')
        rlst = csv.DictReader(f)
#       rlst = csv.reader(f)
#       csv_list = []
        self.data = []
        for line in rlst:
#          csv_list.append(line)
           self.data.append(line)
        f.close()
#       return csv_list
#       return self.data 可写可不写

    def yamlParse(self):
        f = open(self.dataFile,'r')
        self.data = yaml.load(f)
        f.close()
#       return self.data 可写可不写
    
    def parse(self):
        self.type = self.getFileType()
        if self.type in ['yaml','yml','topo']:
#          self.data = self.yamlParse()
           self.yamlParse()
        elif self.type == 'json':
#          self.data = self.jsonParse()
           self.jsonParse()
        elif self.type in ['csv','txt']:
#          self.data = self.csvParse()
           self.csvParse()
        else:
           print 'Unkown file type!'
        return self.data

if __name__ == '__main__':       
   hbb_data = DataParse(dataFile=sys.argv[1])
   data = hbb_data.parse()
   print data




