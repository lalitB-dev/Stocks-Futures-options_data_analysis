from NiftyOp import *
import pandas as pd
import time

response=getData()
rawData=pd.DataFrame(response)
rawop=pd.DataFrame(rawData['filtered']['data']).fillna(0)


def dataFranme(rawop):
    data=[]
    for i in range(0,len(rawop)):
        calloi=callcoi=cltp=putoi=putcoi=pltp=0
        stp= rawop['strikePrice'][i]
        if(rawop['CE'][i]==0):
            calloi=callcoi=0
        else:
            calloi=rawop['CE'][i]['openInterest']
            callcoi=rawop['CE'][i]['changeinOpenInterest']
            cltp=rawop['CE'][i]['lastPrice']

        if (rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi = rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']

        opdata={
            'CALL OI':calloi, 'CALL CHNG OI':callcoi,'CALL LTP':cltp,'STRIKE PRICE':stp,
            'PUT OI':putoi,'PUT CHNG OI':putcoi,'PUT LTP':pltp
        }

        data.append(opdata)

    option_chain=pd.DataFrame(data)

    return option_chain

def main():

    optionchain=dataFranme(rawop)
    TotalCallOI=optionchain['CALL OI'].sum()
    TotalPutOI=optionchain['PUT OI'].sum()
    print(f'Total CALL OI:{TotalCallOI}, Total PUT OI:{TotalPutOI}')
    print(f"OI DIFFERENCE: {TotalCallOI-TotalPutOI}")

count=0
while True:
    print(count)
    main()
    time.sleep(5)
    count+=1
