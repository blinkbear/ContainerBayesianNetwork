import numpy
import json
import csv
import fileinput


Metrix=[]
Data=[]

class JsonHandle:
    def __init__(self,filepath,filename):
        self.filepath=filepath
        self.filename=filename

    def get_Metrix(self,k,v):
        if isinstance(v,dict):
            for kk in v.keys():
                if kk!="eth1":
                    tmp=k+"_"+kk
                    self.get_Metrix(tmp,v[kk])
        elif isinstance(v,list):
            if len(v)!=0:
                for i in range(len(v)):
                    tmp = k+"_"+str(i)
                    self.get_Metrix(tmp,v[i])

        else:
            if(k not in Metrix):
                Metrix.append(k)

    def get_value(self,k,v):
        if isinstance(v,dict):
            for kk in v.keys():
                if kk!="eth1":
                    tmp=k+"_"+kk
                    self.get_value(tmp,v[kk])
        elif isinstance(v,list):
            if len(v)!=0:
                for i in range(len(v)):
                    tmp = k+"_"+str(i)
                    self.get_value(tmp,v[i])

        else:
            i=Metrix.index(k)
            Data[i]=v





    def handle(self):
        flag=True
        length=0
        for line in fileinput.input(self.filepath):
            jsondata=json.loads(line)
            if len(Metrix)==0:
                for key in jsondata.keys():
                    self.get_Metrix(key, jsondata[key])
                length=len(Metrix)
            global Data
            Data=[0]*length
            for key in jsondata.keys():
               self.get_value(key,jsondata[key])
            with open(self.filename, "a") as csvfile:
                writer = csv.writer(csvfile)
                if flag:
                    writer.writerow(Metrix)
                    flag=False
                writer.writerow(Data)

jh=JsonHandle("dataset1/sql.json","dataset1/sql.csv")
jh.handle()

# jh1=JsonHandle("./data/mariadb3.json","mariadb3.csv")
# jh1.handle()
#
# jh2=JsonHandle("./data/mariadb1.json","mariadb1.csv")
# jh2.handle()
#
# jh1=JsonHandle("./data/memcached.json","memcached.csv")
# jh1.handle()
#
# jh2=JsonHandle("./data/nginx.json","nginx.csv")
# jh2.handle()
