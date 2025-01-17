import pandas as pd
import matplotlib.pyplot as plt
import os


# Explore different graph options
#invert y axis on line chart
#add colors to line chart
#group charts
#add colors


#gnuplot

def plot_requests():
    rdf = pd.read_csv("../data/comparisons/requests.csv")

    rdf = pd.DataFrame({"Time per request (ms)": list(rdf.iloc[:,1]),
                       "Time (across all concurrent requests)":list(rdf.iloc[:,2])},
                      index=rdf["Server"])

    rdf.plot.bar(rot=0)
def plot_time_per_requests():
    ndf = pd.read_csv("../data/comparisons/time_per_requests.csv")
    ndf = pd.DataFrame({"Requests per second": list(ndf.iloc[:,1]),
                       "Transfer rate (Kbytes/sec)":list(ndf.iloc[:,2])},index=ndf["Server"])

    ndf.plot.bar(rot=0)
def plot_time_take():
    df = pd.read_csv("../data/comparisons/timetaken.csv")
    df = pd.DataFrame({"Time taken for tests (seconds)":list(df.iloc[:,1])},index=df["Server"])

    df.plot.bar(rot=0)

def plot_connection_times():
    #fig,axes = plt.subplots(ncols=1,nrows=4)
    cdf = pd.read_csv("../data/comparisons/connectionconnect.csv")
    wdf = pd.read_csv("../data/comparisons/connectionwaiting.csv")
    pdf= pd.read_csv("../data/comparisons/connectionprocessing.csv")
    tdf = pd.read_csv("../data/comparisons/connectiontotal.csv")

    
    cdf = pd.DataFrame({"min":list(cdf.iloc[:,1]),
                        "mean":list(cdf.iloc[:,2]),
                        #"[+/-sd]":list(cdf.iloc[:,3]),
                        #"median":list(cdf.iloc[:,4]),
                        "max":list(cdf.iloc[:,5])},index=cdf["Server"])
    cax = cdf.plot.bar(rot=0)
    cax.set_xlabel("Server")
    cax.set_ylabel("Connect times (ms)")
    cax.set_title("Connection times (ms)")
    

    wdf = pd.DataFrame({"min":list(wdf.iloc[:,1]),
                        "mean":list(wdf.iloc[:,2]),
                       # "[+/-sd]":list(wdf.iloc[:,3]),
                        #"median":list(wdf.iloc[:,4]),
                        "max":list(wdf.iloc[:,5])},index=wdf["Server"])
    wax = wdf.plot.bar(rot=0)
    wax.set_xlabel("Server")
    wax.set_ylabel("Waiting times (ms)")
    wax.set_title("Waiting times (ms)")

    pdf = pd.DataFrame({"min":list(pdf.iloc[:,1]),
                        "mean":list(pdf.iloc[:,2]),
                        #"[+/-sd]":list(pdf.iloc[:,3]),
                        #"median":list(pdf.iloc[:,4]),
                        "max":list(pdf.iloc[:,5])},index=pdf["Server"])
    pax = pdf.plot.bar(rot=0)
    pax.set_xlabel("Server")
    pax.set_ylabel("Processing times (ms)")
    pax.set_title("Processing times (ms)")

    tdf = pd.DataFrame({"min":list(tdf.iloc[:,1]),
                        "mean":list(tdf.iloc[:,2]),
                        #"[+/-sd]":list(tdf.iloc[:,3]),
                        #"median":list(tdf.iloc[:,4]),
                        "max":list(tdf.iloc[:,5])},index=tdf["Server"])
    tax = tdf.plot.bar(rot=0)
    tax.set_xlabel("Server")
    tax.set_ylabel("Total times (ms)")
    tax.set_title("Total times (ms)")

    

    

plot_time_take()
plot_requests()
plot_time_per_requests()
plot_connection_times()

#consistent measurements

##requests_df = pd.read_csv("../data/comparisons/requests.csv")
##requests_df.plot.bar(rot=0)



line_chart_df = pd.read_csv("../data/comparisons/served.csv")

line_chart_df.plot(x="Percentage of requests",
                   y=[i for i in line_chart_df.columns if "Percentage of requests" not in i],
                   figsize=(10,5))

plt.xlabel("Percentage of requests served")
plt.ylabel("Time (ms)")
plt.title("Requests served in time")



plt.show()





