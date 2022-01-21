from http.client import responses
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
responses = df["responses"].tolist()

# code to show the plot of raw responses
# fig = ff.create_distplot([responses], ["temp"], show_hist=False)
# fig.show()

#code to find mean and std deviation of 100 responses points
# responsesset = []
# for i in range(0, 100):
#     random_index= random.randint(0,len(responses))
#     value = responses[random_index]
#     responsesset.append(value)
# mean = statistics.mean(responsesset)
# std_deviation = statistics.stdev(responsesset)
#
# print("Mean of sample:- ",mean)
# print("std_deviation of sample:- ",std_deviation)

##  code to find the mean of 100 responses points 1000 times and plot it
#function to get the mean of the given responses samples
# pass the number of responses points you want  as counter
def random_set_of_mean(counter):
    responsesset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(responses)-1)
        value = responses[random_index]
        responsesset.append(value)
    mean = statistics.mean(responsesset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["responses"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

# Pass the number of time you want the mean of the responses points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

#Code to find the mean of the raw responses ("population responses")
population_mean = statistics.mean(responses)
print("population mean:- ", population_mean)

# code to find the standard deviation of the sample responses
def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()
