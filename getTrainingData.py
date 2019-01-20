import pandas as pd
import os
import urllib
import json



def getFeildList():
    rawData = urllib.urlopen('http://edgaronline.api.mashery.com/v2/corefinancials/qtr?primarysymbols=AAPL&appkey=kvpuyc7kqw5jtk5xmpamaraw').read()
    jsonData = json.loads(rawData)
    fieldList = []
    for num in range(65):
        info = jsonData['result']['rows'][0]['values'][num]['field']
        fieldList.append(info)
    return fieldList




def fetchStock(stockTicker):
    try:
        try:
            rawData = urllib.urlopen('http://edgaronline.api.mashery.com/v2/corefinancials/qtr?primarysymbols='+stockTicker+'&appkey=kvpuyc7kqw5jtk5xmpamaraw').read()
            jsonData = json.loads(rawData)
            fieldList = []
            try:
                for num in range(65):
                    info = jsonData['result']['rows'][0]['values'][num]['field']
                    fieldList.append(info)
                stockDf = pd.DataFrame(columns = fieldList)
                lister = 0
                try:
                    for i in range(16):
                        newRow = []
                        for x in range(65):
                            try:
                                value = jsonData['result']['rows'][i]['values'][x]['value']
                                newRow.append(value)
                            except:
                                newRow.append('NULL')

                        stockDf.loc[i] = newRow
                    truth = True
                    returner = [truth, stockDf]
                    return returner
                except Exception as e:
                    print 'NEW ERROR',str(e)
            except Exception as e:
                print 'ERROR',str(e)
                returner2 = [False]
                return returner2

        except Exception as e:
            print str(e),'error here'
    except Exception as e:
        print(str(e)),'error there'







sp500_df = pd.DataFrame.from_csv("sp500List.csv")
df = pd.DataFrame(columns = getFeildList())
stocksToPull = []
for i in range(500):
    stocksToPull.append(sp500_df.index[i])
print stocksToPull
worked = 0
failed = 0
for i in stocksToPull:
    if fetchStock(i)[0] == False:
        failed = failed+1
        print 'Failed: ',failed

    else:
        df = df.append(fetchStock(i)[1])
        worked = worked+1
        print 'Worked: ',worked


df.to_csv('edgarData.csv')
print 'EdgarData Complete'

#print 'Field list: ',getFeildList()

#for stock in stocksToPull:
#    fetchStock(stock)

#print 'Edgar Data to csv complete'
#df.to_csv('edgarData.csv')
