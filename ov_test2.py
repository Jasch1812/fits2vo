import astropy.io.votable.treeFits as vo 
from scipy import misc
import numpy as np 
import os


# nm = glob.glob('/home/johann/Desktop/*.png')[0]
# imArr = misc.imread(nm).astype(np.int32)
# r, c = imArr.shape
# print imArr.dtype

votable = vo.VOTableFile(version='1.3')

resource = vo.Resource()

votable.resources.append(resource)

table = vo.Table(votable)
resource.tables.append(table)
table.description = 'Lette A from non-MNIST set'

table.format = 'fits'

fits_path = "./A_fits.fits"
if( os.path.exists(fits_path)):
  table.set_href('file://' + os.path.abspath(fits_path))



votable.to_xml('A_vo_fits.xml')