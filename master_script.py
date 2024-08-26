import requests
import pandas as pd

master_url= "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
data = requests.get(master_url).json()
df = pd.DataFrame(data)
df["strike"] = pd.to_numeric(df["strike"], errors='coerce')  # Convert to numeric, coercing errors to NaN
df["strike"] = df["strike"].fillna(0)  # Handle NaNs (e.g., fill with 0)
df["strike"] = df["strike"] / 100  # Perform the division
output_file = f"master_scripts_output.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='master_scripts')           
    
print(f"Resampled candle data saved to {output_file} in separate sheets.") 