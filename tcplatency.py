import pandas as pd
import numpy as np
import datetime
import time
import matplotlib.pyplot as plot

df1=pd.read_csv("./result/tmp.csv")

for line in df1.columns:
    if line != "cpu" and line != "count":
        df1=df1.drop(columns=[line])

# tmp=1528687441

# l1=[]
# for index,row in df1.iterrows():
#     l1.append(row['networks_eth0_rx_packets'])
#
# l2=[]
# l2.append(0)
# for i in range(1,len(l1)):
#     l2.append(l1[i]-l1[i-1])
#
#
#
# l3=[]
# for index,row in df1.iterrows():
#     l3.append(row['networks_eth0_tx_packets'])
#
# l4=[]
# l4.append(0)
# for i in range(1,len(l3)):
#     l4.append(l3[i]-l3[i-1])

# count={}
# for index,row in df1.iterrows():
#     if count.has_key(str(row["count"])):
#         count[str(row["count"])]=count[str(row["count"])]+1
#     else:
#         count[str(row["count"])]=1
# list=[]
# for key in count.keys():
#     list.append(key)

#
# plot.bar(range(len(list)), [count.get(xtick, 0) for xtick in list], align='center',yerr=0.01)
#
# plot.xticks(range(len(list)), list)
# print([line for line in df1.columns])
x=np.array(df1["cpu"]).tolist()
y=np.array(df1["count"]).tolist()
# x=l2
# y=l4
plot.xlabel("cpu")
plot.ylabel("count")
plot.scatter(x,y)
plot.show()

