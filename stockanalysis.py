import urllib2
import time
import datetime

stocksToPull = ['CRM', 'AAPL', 'AMZN', 'CELG', 'CERN', 'ILM', 'IBM', 'NVDA', 'TSLA', 'FB', 'SCTY', 'TWTR']


def pullData(stock):
    try:
        fileLine = stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        print 'pulling '+stock+' from Yahoo Finance...'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

        try:
            readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.spit('\n')
            mostRecentLine = splitExisting[-2]

        except Exception as e:
            print 'somethings not working 2'

    except Exception as e:
        print 'somethings not working'

for eachStock in stocksToPull:
    pullData(eachStock)
