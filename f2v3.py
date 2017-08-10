import astropy.io.fits as fits
import astropy.io.votable.treeFits as vo
import glob
import os
import numpy as np

def str_max(string, length):
  len_str = len(string)
  if len_str > length:
    return len_str
  else:
    return length

def hdu_unpack(hdu_header):
  hdu_dict = dict( hdu_header )
  key_arr = []
  val_float = []
  val_str = []
  com_arr = []
  key_len = 0
  val_len = 0
  com_len = 0

  for k in set(hdu_dict.keys()):
    if not k:
      continue
    elif k.upper() == 'HISTORY':
      continue
    elif k.upper() == 'COMMENT':
      continue
    else:
      key_arr.append(k)
      key_len = str_max(str(k), key_len)

      v = hdu_dict[k]
      v_type = type(v).__name__
      if (v_type=='int') or (v_type=='float'):
        val_float.append(str(v))
        val_str.append('')
      else:
        val_float.append('')
        val_str.append(str(v))
        val_len = str_max( str(v), val_len)

      com = hdu_header.comments[k]
      com_arr.append(com)
      # print("{}----{}".format(com, com_len))
      com_len = str_max( str(com), com_len )
  head_len = len(key_arr)
  head_arr = np.array([key_arr, val_float, val_str, com_arr])

  return np.transpose(head_arr), str(key_len)+'*', str(val_len)+'*', str(com_len)+'*'

fitsList = glob.glob('./TWHYA_BAND7/*.fits')
fits0 = fitsList[0]
fits_nm = fits0.rsplit('/',1)[-1]
fits_pre = fits_nm.rsplit('.',1)[-2]
# print(fits_pre)

hdu = fits.open(fits0)[0]

votable = vo.VOTableFile(version='1.2')

resource = vo.Resource()

votable.resources.append(resource)

table = vo.Table(votable)
resource.tables.append(table)
table.description = fits_pre

# h0 = hdu[0]
# hdu_dict = dict(hdu.header)

hdu_arr, klen, vlen, clen = hdu_unpack(hdu.header)

field0 = vo.Field(votable, name='key', datatype='char', arraysize=klen)
field1 = vo.Field(votable, name='value_float', datatype='double')
field2 = vo.Field(votable, name='value_str', datatype='char', arraysize=vlen)#str(vlen)+'*')
field3 = vo.Field(votable, name='comments', datatype='char', arraysize=clen)#str(clen)+'*')
table.fields.append(field0)
table.fields.append(field1)
table.fields.append(field2)
table.fields.append(field3)

# table.array = hdu_arr
hdu_arr = hdu_arr.copy(order='C')
# print(hdu_arr)
row = hdu_arr.shape[0]
table.create_arrays(row)
for i in range(row):
  table.array[i] = hdu_arr[i]

print(table.array)

table.format2 = 'fits'

if( os.path.exists(fits0)):
  table.set_href('file://' + os.path.abspath(fits0))

votable.to_xml(fits_pre+'3.xml')