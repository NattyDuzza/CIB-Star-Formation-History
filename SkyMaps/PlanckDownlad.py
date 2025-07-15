import os
import wget

base_url = "https://g-456d30.0ed28.75bc.data.globus.org/public/planck/planck_pr4/fullsky"

files = [
    "npipe6v20_143_map.fits",
    "npipe6v20_217_map.fits",
    "npipe6v20_353_map.fits",
    "npipe6v20_545_map.fits",
    "npipe6v20_857_map.fits"]

for file in files:
    url = f"{base_url}/{file}"
    print(f"Downloading {file} from {url}")
    wget.download(url, out=f"/home/nathand/Documents/AstroCode/SkyMaps/{file}")
    print(f"\n{file} downloaded successfully.")


