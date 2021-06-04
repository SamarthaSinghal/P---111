import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import statistics as st
import pandas as pd
import random as rn
df = pd.read_csv ("medium_data.csv")
data = df["Math_score"].tolist()
mean = st.mean(data)
std = st.stdev(data)
print ("mean",mean)
print ("standarddeviation",std)
def randomset (counter):
    dataset = []
    for i in range (0,counter):
        randomindex = rn.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
meanlist = []
for i in range (0,1000):
    setofmean = randomset (100)
    meanlist.append(setofmean)
mean = st.mean(meanlist)
std = st.stdev(meanlist)
print("mean",mean)
print("standarddeviation",std)

firststdstart,firststdend = mean-std,mean+std
secondstdstart,secondstdend = mean-(2*std),mean+(2*std)
thirdstdstart,thirdstdend = mean-(3*std),mean+(3*std)
print ("std1",firststdstart,firststdend)
print ("std2",secondstdstart,secondstdend)
print ("std3",thirdstdstart,thirdstdend)
fig = ff.create_distplot([meanlist],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.17],mode = "lines",name = "standarddeviation1"))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = "lines",name = "standarddeviation1"))
fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.17],mode = "lines",name = "standarddeviation2"))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = "lines",name = "standarddeviation2")) 
fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.17],mode = "lines",name = "standarddeviation3"))
fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = "lines",name = "standarddeviation3")) 
fig.show()
df = pd.read_csv("data1.csv")
data = df ["Math_score"].tolist()
mean1 = st.mean(data)
print ("mean1",mean1)
fig = ff.create_distplot([meanlist],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = "lines",name = "meanofsample"))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = "lines",name = "standarddeviation1"))
fig.show()
df = pd.read_csv("data2.csv")
data = df ["Math_score"].tolist()
mean2 = st.mean(data)
print ("mean2",mean2)
fig = ff.create_distplot([meanlist],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean2,mean2],y = [0,0.17],mode = "lines",name = "meanofsample"))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = "lines",name = "standarddeviation1"))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = "lines",name = "standarddeviation2"))
fig.show()
df = pd.read_csv("data3.csv")
data = df ["Math_score"].tolist()
mean3 = st.mean(data)
print ("mean3",mean3)
fig = ff.create_distplot([meanlist],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean3,mean3],y = [0,0.17],mode = "lines",name = "meanofsample"))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = "lines",name = "standarddeviation2"))
fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = "lines",name = "standarddeviation3"))
fig.show()
zscore = (mean1-mean)/std
print (zscore)
zscore = (mean2-mean)/std
print (zscore)
zscore = (mean3-mean)/std
print (zscore)