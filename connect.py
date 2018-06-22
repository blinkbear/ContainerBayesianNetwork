import pandas as pd
import numpy as np
import datetime
import time

df1=pd.read_csv("dataset1/sql.csv")

df2=pd.read_csv("dataset1/sqllatency.out",sep='\t')
df6=pd.read_csv("dataset1/sqlstats.out",sep=" ")
df6=df6.dropna(axis=1,how="all")
df6.columns=["read","cpu","mem"]
df6["read"]=df6["read"]-1
df6["cpu"]=df6["cpu"].str.strip("%").astype(float)/100
df6["mem"]=df6["mem"].str.strip("%").astype(float)/100

for line in df2.columns:
    if line != "avg" and line != "timestamp" and line!="count":
        df2=df2.drop(columns=[line])

df1=df1.drop(columns=['name','preread','id','precpu_stats_online_cpus',
                      'blkio_stats_io_service_bytes_recursive_0_op',
                      'blkio_stats_io_service_bytes_recursive_1_op',
                      'blkio_stats_io_service_bytes_recursive_2_op',
                      'blkio_stats_io_service_bytes_recursive_3_op',
                      'blkio_stats_io_service_bytes_recursive_4_op',
                      'blkio_stats_io_serviced_recursive_0_op',
                      'blkio_stats_io_serviced_recursive_1_op',
                      'blkio_stats_io_serviced_recursive_2_op',
                      'blkio_stats_io_serviced_recursive_3_op',
                      'blkio_stats_io_serviced_recursive_4_op'])
# list=["read","networks_eth0_rx_bytes","networks_eth0_tx_bytes","memory_stats_usage","memory_stats_stats_total_rss_huge",
#       "memory_stats_stats_total_cache"]
# for line in df1.columns:
#     if line not in list:
#         df1=df1.drop(columns=[line])
# df2=df2.drop(columns=['max','min','med','stddev','95_max','95_avg','95_std','99_max','99_avg','99_std'])
#
for line in df1.columns:
    if line != "read":
       if df1[line][0] == df1[line].mean():
           df1=df1.drop(columns=[line])




for line in df1.columns:
    if line!="read":
        tmp=df1[line].shift(1)
        df1[line] = df1[line] - tmp


df1.fillna(0)
source=df1['read'].tolist()
destination=[]
for s in df1['read']:
    s=s.replace("T"," ").split(".")[0]
    destination.append(time.mktime(time.strptime(s, "%Y-%m-%d %H:%M:%S"))+28800)
df3=df1.replace(source,destination)
df4=df2.rename(columns={'timestamp':'read'})
df5=pd.merge(df3,df6,on="read")
df5=pd.merge(df5,df4,on="read")

df5=df5.drop(columns=['read'])



# df5=df5.drop(columns=['memory_stats_stats_pgpgout',
#                       'memory_stats_stats_pgpgin','memory_stats_stats_cache',
#                       'memory_stats_stats_cache','memory_stats_stats_active_file',
#                       'memory_stats_stats_rss',
#                       'memory_stats_stats_pgfault','memory_stats_stats_inactive_file',
#                       'memory_stats_stats_active_anon','networks_eth0_rx_packets'
#                       ,'networks_eth0_tx_packets',
#                       'precpu_stats_system_cpu_usage'])

df5=df5.drop(columns=['networks_eth0_rx_packets','blkio_stats_io_service_bytes_recursive_2_value'
                       ,'networks_eth0_tx_packets','blkio_stats_io_service_bytes_recursive_1_value',
                      'blkio_stats_io_service_bytes_recursive_4_value'])

i=0
for line in df5.columns:
    print(i , line)
    i=i+1

col_rep=[]
for i in range(len(df5.columns)):
    col_rep.append(str(i))

df5.columns=col_rep
df5.to_csv("dataset1/dataset.csv",index=False,sep=',')