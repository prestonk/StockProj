import pandas as pd
import os
import urllib
import json
import re
import numpy as np


df = pd.DataFrame.from_csv("edgarData.csv")

for i in df.iteritems():
    if i[0] == 'amended':
        del df['amended']
    if i[0] == 'audited':
        df['audited'].replace("FASLE", 0).replace("TRUE", 1)
    if i[0] == 'cik':
        del df['cik']
    if i[0] == 'companyname':
        del df['companyname']
    if i[0] == 'crosscalculated':
        del df['crosscalculated']
    if i[0] == 'currencycode':
        del df['currencycode']
    if i[0] == 'dcn':
        del df['dcn']
    if i[0] == 'deferredcharges':
        del df['deferredcharges']
    if i[0] == 'discontinuedoperations':
        del df['discontinuedoperations']
    if i[0] == 'formtype':
        del df['formtype']
    if i[0] == 'marketoperator':
        del df['marketoperator']
    if i[0] == 'markettier':
        del df['markettier']
    if i[0] == 'original':
        del df['original']
    if i[0] == 'periodenddate':
        del df['periodenddate']
    if i[0] == 'periodlength':
        del df['periodlength']
    if i[0] == 'periodlengthcode':
        del df['periodlengthcode']
    if i[0] == 'preliminary':
        del df['preliminary']
    if i[0] == 'primaryexchange':
        del df['primaryexchange']
    if i[0] == 'primarysymbol':
        del df['primarysymbol']
    if i[0] == 'receiveddate':
        del df['receiveddate']
    if i[0] == 'restated':
        del df['restated']
    if i[0] == 'siccode':
        del df['siccode']
    if i[0] == 'sicdescription':
        del df['sicdescription']
    if i[0] == 'usdconversionrate':
        del df['usdconversionrate']

for x in df.iteritems():
    print x[0]
