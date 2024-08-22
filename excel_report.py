import pandas as pd
from datetime import datetime as dt

class report:
    @staticmethod
    def generate_report(df_15min,df_30min,df_1hr,df_1day):   
       output_file = f"{dt.now().strftime('%Y-%m-%d')}_output.xlsx"
       with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
           df_15min.to_excel(writer, sheet_name='15_minutes')
           df_30min.to_excel(writer, sheet_name='30_Minutes')
           df_1hr.to_excel(writer, sheet_name='1_Hours')           
           df_1day.to_excel(writer, sheet_name='1_day')
           
       print(f"Resampled candle data saved to {output_file} in separate sheets.") 
      