import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates= ["Timestamp"])

data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Ratings by Date'
    },
    subtitle: {
        text: 'According to the reviews provided'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Date: 2018 to 2021.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Rating: 3.5 to 5.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app() :
    wp = jp.QuasarPage()

    divider = jp.QDiv(a = wp, classes = "q-pa-sm")
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center")
    divider = jp.QDiv(a = wp, classes = "q-pa-sm")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis", classes = "text-h5 text-center")
    divider = jp.QDiv(a = wp, classes = "q-pa-l")

    hc = jp.HighCharts(a = wp, options = chart_def)

    x = day_average.index
    y = day_average["Rating"]

    hc.options.xAxis.categories = list(x)
    hc.options.series[0].data = list(y)
 


    return wp

jp.justpy(app)