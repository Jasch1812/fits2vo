import astropy.io.fits as fits
import astropy.io.votable.treeFits as vo
import glob
import os

fitsList = glob.glob('./TWHYA_BAND7/*.fits')

fits0 = fitsList[0]
fits_nm = fits0.rsplit('/',1)[-1]
fits_pre = fits_nm.rsplit('.',1)[-2]
print(fits_pre)

hdu = fits.open(fits0)[0]

votable = vo.VOTableFile(version='1.2')

resource = vo.Resource()

votable.resources.append(resource)

table = vo.Table(votable)
resource.tables.append(table)
table.description = fits_pre

# h0 = hdu[0]
hdu_dict = dict(hdu.header)

for k in set(hdu_dict.keys()):
  if not k:
    continue
  if k == 'HISTORY':
    continue
  else:
    v = hdu_dict[k]
    v_type = type(hdu_dict[k]).__name__
    # print(type(v_type))
    if v_type == 'int':
      para = vo.Param(votable, name = k, datatype='int', value=int(v) )
    elif v_type == 'float':
      para = vo.Param(votable, name = k, datatype='double', value=v )
    else:
      para = vo.Param(votable, name = k, datatype='char', arraysize='*', value=str(v) )
    table.params.append(para)

table.format = 'fits'

if( os.path.exists(fits0)):
  table.set_href('file://' + os.path.abspath(fits0))

votable.to_xml(fits_pre+'2.xml')