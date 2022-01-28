import pandas as pd 
import plotly.figure_factory as pf
import random
import statistics as st
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
populationMean=st.mean(data)
populationStDev=st.stdev(data)
print(populationMean)
print(populationStDev)

fig=pf.create_distplot([data],["math score"],show_hist=False)
#fig.show()

def randomSetOfMeans():
    dataset=[]
    for i in range (0,100):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    random_mean=st.mean(dataset)
    return random_mean

mean_list=[]
for i in range(0,1000):
    sample_mean=randomSetOfMeans()
    mean_list.append(sample_mean)

mean=st.mean(mean_list)
stdev=st.stdev(mean_list)
print(mean)
print(stdev)

stdev_1_start=mean-stdev
stdev_1_end=mean+stdev

stdev_2_start=mean-(2*stdev)
stdev_2_end=mean+(2*stdev)

stdev_3_start=mean-(3*stdev)
stdev_3_end=mean+(3*stdev)

fig=pf.create_distplot([mean_list],["sampling math score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[stdev_1_start,stdev_1_start],y=[0,0.2],mode="lines",name="stdev1start"))
fig.add_trace(go.Scatter(x=[stdev_2_start,stdev_2_start],y=[0,0.2],mode="lines",name="stdev2start"))
fig.add_trace(go.Scatter(x=[stdev_3_start,stdev_3_start],y=[0,0.2],mode="lines",name="stdev3start"))

fig.add_trace(go.Scatter(x=[stdev_1_end,stdev_1_end],y=[0,0.2],mode="lines",name="stdev1end"))
fig.add_trace(go.Scatter(x=[stdev_2_end,stdev_2_end],y=[0,0.2],mode="lines",name="stdev2end"))
fig.add_trace(go.Scatter(x=[stdev_3_end,stdev_3_end],y=[0,0.2],mode="lines",name="stdev3end"))

df1=pd.read_csv("data1.csv")
data1=df1["Math_score"].tolist()
data1mean=st.mean(data1)
print(data1mean)
fig.add_trace(go.Scatter(x=[data1mean,data1mean],y=[0,0.3],mode="lines",name="data1mean"))

df2=pd.read_csv("data2.csv")
data2=df2["Math_score"].tolist()
data2mean=st.mean(data2)
print(data2mean)
fig.add_trace(go.Scatter(x=[data2mean,data2mean],y=[0,0.3],mode="lines",name="data2mean"))

df3=pd.read_csv("data3.csv")
data3=df3["Math_score"].tolist()
data3mean=st.mean(data3)
print(data3mean)
fig.add_trace(go.Scatter(x=[data3mean,data3mean],y=[0,0.3],mode="lines",name="data3mean"))




fig.show()
Z_score1=(data1mean-mean)/stdev
print(Z_score1)

Z_score2=(data2mean-mean)/stdev
print(Z_score2)

Z_score3=(data3mean-mean)/stdev
print(Z_score3)