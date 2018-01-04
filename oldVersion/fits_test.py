from astropy.io import fits
from scipy import misc
import numpy as np 
import glob

nm = glob.glob('./*.png')[0]
imArr = misc.imread(nm).astype(np.int32)
r, c = imArr.shape

hdu = fits.PrimaryHDU( imArr )
# print( type(hdu) )
hdulist = fits.HDUList([hdu])
hdulist.writeto('A_fits.fits')

# votable.to_xml('vo_tabledata_A.xml')
