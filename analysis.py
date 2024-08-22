from logzero import logger
import pandas as pd
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd

class analysis:
      @staticmethod
      def generate_signal(smartApi, duration):   
        todate = dt.now()  
        fromdate = todate - rd(months=3)
        if duration == "1h":
             duration = "ONE_HOUR" 
        elif duration == "30m":
             duration = "THIRTY_MINUTE"    
        elif duration == "15m":
             duration = "FIFTEEN_MINUTE"    
        elif duration == "1d":
             duration = "ONE_DAY"                   
                     
        try:
            historicParam={
            "exchange": "NSE",
            "symboltoken": "467",           
            "interval": duration,            
            "fromdate": fromdate.strftime('%Y-%m-%d %H:%M'), 
            "todate": todate.strftime('%Y-%m-%d %H:%M'), 
            }
            historical_data = smartApi.getCandleData(historicParam)
            if historical_data['message'] != "SUCCESS":
                print('historical_data ',historical_data)                    
            df = pd.DataFrame(historical_data['data'], columns=["timestamp", "open", "high", "low", "close", "volume"])
            df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_localize(None)    
            df['date'] = df['timestamp'].dt.date
            df['time'] = df['timestamp'].dt.time        
            df = df.sort_values(by=['date', 'time'], ascending=[True, False])                                 
            df = df.drop(columns=['timestamp'])       
            df = df[['date', 'time', 'open', 'high', 'low', 'close', 'volume']]
            df = df.dropna()           
            print (df)
            return df              
        except Exception as e:
            logger.exception(f"Historic Api failed: {e}")
            return ""
  