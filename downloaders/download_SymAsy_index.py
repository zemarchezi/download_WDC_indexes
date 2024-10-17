#%%
import os
import requests
import datetime
from pathlib import Path
#%%

def download_SymAsyH(download_years, sym_h_folder):
    """
    Function to retrieve SYM-H index data from WDC for Geomagnetism Kyoto.
    """
    print("Starting download...")
    
    for year in range(download_years[0], download_years[1]):
        days = (datetime.datetime(year + 1, 1, 1) - datetime.datetime(year, 1, 1)).days

        url = (f"https://wdc.kugi.kyoto-u.ac.jp/cgi-bin/aeasy-cgi?Tens={str(year)[:3]}&Year={str(year)[-1]}"
               f"&Month=01&Day_Tens=0&Days=0&Hour=00&min=00&Dur_Day_Tens={str(days)[:2]}"
               f"&Dur_Day={str(days)[-1]}&Dur_Hour=00&Dur_Min=00&Image+Type=GIF&COLOR=COLOR"
                "&AE+Sensitivity=0&ASY%2FSYM++Sensitivity=0&Output=ASY&Out+format=IAGA2002")
        file_path = os.path.join(sym_h_folder, f"{year}.txt")
        
        # Fetch data from the URL
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors
            
            # Save the content to a file
            with open(file_path, 'w') as file:
                file.write(response.text)
            
            print(f"Downloaded SYM-H data for {year}.")
        
        except requests.RequestException as e:
            print(f"Failed to download data for {year}: {e}")
#%%
if __name__ == "__main__":
    # Set the download years and the folder to save the data
    download_years = (1996, 2024)


    home = Path.home()
    sym_h_folder = os.path.join(home, 'mag_data', 'SYM_H')

    # Ensure the folder exists
    os.makedirs(sym_h_folder, exist_ok=True)
    
    # Download the data
    download_SymAsyH(download_years, sym_h_folder)
# %%
