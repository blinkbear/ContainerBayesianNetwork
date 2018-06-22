import pandas as pd
import numpy as np
import datetime
import time
import matplotlib.pyplot as plot

df1=pd.read_csv("nginx.out",sep='\t')
df2=pd.read_csv("tomcat1Tcp.out",sep='\t')
df3=pd.read_csv("tomcat2Tcp.out",sep='\t')
df4=pd.read_csv("tomcat3Tcp.out",sep='\t')
df5=pd.read_csv("tomcat4tcp.out",sep='\t')
df6=pd.read_csv("tcpmem.out",sep='\t')
df7=pd.read_csv("maxscale.out",sep='\t')
df8=pd.read_csv("dbtcp.out",sep='\t')

for line in df1.columns:
    if line != "timestamp" and line != "med":
        df1=df1.drop(columns=line)
        df2=df2.drop(columns=line)
        df3=df3.drop(columns=line)
        df4=df4.drop(columns=line)
        df5=df5.drop(columns=line)
        df6=df6.drop(columns=line)
        df7=df7.drop(columns=line)
        df8=df8.drop(columns=line)
print(df1["med"].mean())
print(df2["med"].mean())
print(df3["med"].mean())
print(df4["med"].mean())
print(df5["med"].mean())
print(df6["med"].mean())
print(df7["med"].mean())
print(df8["med"].mean())
# df=pd.merge(df1,df2,on="timestamp")
# df=pd.merge(df,df3,on="timestamp")
# df=pd.merge(df,df4,on="timestamp")
# df=pd.merge(df,df5,on="timestamp")
# df=pd.merge(df,df6,on="timestamp")
# df=pd.merge(df,df7,on="timestamp")
# df=pd.merge(df,df8,on="timestamp")
# # df.rename(columns=["timestamp","nginx","tomcat1","tomcat2","tomcat3","tomcat4","memcached","maxscale","mariadb"])
# df=df.drop(columns="timestamp")
# df.to_csv("./result/tcplatency.csv",index=False,sep=',')