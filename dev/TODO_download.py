#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:04:16 2021

@author: ghiggi
"""
### default to n_threads as ltenas3 (5) ? 
### try remapping with NN
### time access to GOES data: local vs. ffspec s3 vs. zarr workaround


from ftplib import FTP_TLS
import ssl
ftp_site = "arthurhouftps.pps.eosdis.nasa.gov"
FTP_TLS.ssl_version = ssl.PROTOCOL_TLSv1_2
ftps = FTP_TLS()
ftps.debugging = 2
ftps.connect(ftp_site,21)
ftps.login(’uname’,’password’)
ftps.prot_p()

# https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2ADPR.06/


# https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2ADPR.06/2020/005/

# NASA GESDISC DATA ARCHIVE
# https://disc.gsfc.nasa.gov/earthdata-login (more authorization)
# https://disc.gsfc.nasa.gov/data-access
# https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Download%20Data%20Files%20from%20HTTPS%20Service%20with%20wget

# GES DISC via HTTPS, remove .xml files

## List data files 
ftp ls
wget -q -nH -nd “<URL>” -O - | grep <filename_pattern> | cut -f4 -d\"
wget -q -nH -nd “<URL>” -O - | grep <filename_pattern> | awk -F'\"' '{print $4}'

wget -q -nH -nd "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXSLV.5.12.4/1981/" -O - | grep MERRA2_100 | cut -f4 -d\"
wget -q -nH -nd "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXSLV.5.12.4/1981/" -O - | grep MERRA2_100 | awk -F'\"' '{print $4}'

## Download 
ftp mget
wget <auth> --content-disposition <URL_file>

# Specific file
wget --load-cookies C:\.urs_cookies --save-cookies C:\.urs_cookies --auth-no-challenge=on --keep-session-cookies --user=<your username> --ask-password --content-disposition  https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXSLV.5.12.4/1981/MERRA2_100.tavgM_2d_slv_Nx.198101.nc4
# To download multiple data files in the directory:
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies -r -c -nH -nd -np -A 'nc4' --content-disposition "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXSLV.5.12.4/1981/"
# - with patterns
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies -r -c -nH -nd -np -A '*19811*nc4' --content-disposition "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXSLV.5.12.4/1981/"

# Deploy scripting methods to list and download data in bulk


### Pangeo Data Lobby
# https://gitter.im/pangeo-data/Lobby
# https://discourse.pangeo.io/latest/ 


## pyDAP: access to OPENDAP

## requests & urlib
https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+Python