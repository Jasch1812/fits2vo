import glob 
import time
from f2v5 import *

fitsList = glob.glob('./omc.con.fits/*.fits')

fv = fits2vo('fits')
fv.xml_pre = './omc.con.fits_votable/'

start_time = time.time()

for fitsfile in fitsList:
  fv.import_fits( fitsfile )
  fv.f2v()
  end_time = time.time()
  run_time = end_time - start_time
  start_time = end_time
  print("{}\t-->\t{} sec".format(fitsfile, run_time))