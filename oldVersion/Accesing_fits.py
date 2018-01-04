import os
import urllib.request
import tarfile
from astropy.io import fits
#import logging
#import warnings

global D_DIR
D_DIR = '.'

def download_and_extract(url):
  # make the filename
  name = url.rsplit('/',1)[-1]
  filename = os.path.join(D_DIR, name)

  #Download the file if not found
  if not os.path.isfile(filename):
     urllib.request.urlretrieve(url, filename) # python3.x
#    urllib.urlretrieve(url, filename) #python 2.7

  # Decompress (if needed) and copy the selected file to the D_DIR
  sdir = filename.rsplit('ReferenceImages', 1)[0] + 'ReferenceImages'
  if not os.path.isdir(sdir):
    tar = tarfile.open( filename )
    tar.extractall(path = D_DIR)
    tar.close()

twhydra_url = 'https://almascience.nrao.edu/almadata/sciver/TWHya/TWHYA_BAND7_ReferenceImages.tgz'
download_and_extract( twhydra_url )

hdulist = fits.open("TWHYA_BAND7_ReferenceImages/TWHydra_CO3_2line.image.mom0.fits")
twhydra = hdulist[0]
print(twhydra.header.keys())
