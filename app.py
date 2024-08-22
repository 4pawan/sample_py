import pandas as pd
from SmartApi import SmartConnect
from logzero import logger
import pyotp
import time
from analysis import analysis as da
from excel_report import report as r
from config import config

api_key = config.api_key
username = config.username
pwd = config.pwd
token = config.token
smartApi = SmartConnect(api_key)
try:
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

conn = smartApi.generateSession(username, pwd, totp)

if conn['status'] == False:
    logger.error(conn)    
    
df_1hr = da.generate_signal(smartApi,"1h")
df_15min = da.generate_signal(smartApi,"15m")
df_30min = da.generate_signal(smartApi,"30m")
time.sleep(60)
df_1day = da.generate_signal(smartApi,"1d")
r.generate_report(df_15min,df_30min,df_1hr,df_1day)