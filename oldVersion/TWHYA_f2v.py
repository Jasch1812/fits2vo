import glob 
import time
from f2v5 import *

fitsList = glob.glob('./TWHYA_BAND7/*.fits')

fv = fits2vo('fits')
fv.xml_pre = './TWHYA_votable/'

start_time = time.time()
t1 = start_time

for fitsfile in fitsList:
  fv.import_fits( fitsfile )
  fv.f2v()
  end_time = time.time()
  run_time = end_time - start_time
  start_time = end_time
  print("{}\t-->\t{} sec".format(fitsfile, run_time))

print("Total time is {} sec".format(end_time-t1))