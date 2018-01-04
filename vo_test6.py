from f2v6 import *
import astropy.io.votable.tree as vo
import os.path as path

# f2v = fits2vo('fits')
# f2v.import_fits('./testfits/multi.fits')
# hd = f2v._fits_handle
# print(hd)

# for im in hd:
#   del f2v._key_list[:]
#   f2v.hdu_unpack(im.header)
  
#   for item in f2v._hdu_list:
#     print(item)
#   print('-'*30)

votable = vo.VOTableFile()
resource = vo.Resource()
s_path = path.abspath('./testfits/single.fits')
m_path = path.abspath('./testfits/multi.fits')
l1 = vo.Link(content_type='image/fits', title='stamp1', href=s_path)
t1 = vo.Table(votable, name='Prime', href=m_path)
l2 = vo.Link(content_type='image/fits', title='stamp1', href=s_path)
t1.links.append(l2)
t1._get_binary_data_stream(iterator=['1', 'STREAM',{'href':m_path},'1'], config=1)
resource.links.append(l1)
resource.tables.append(t1)

votable.resources.append(resource)

votable.to_xml('link_table.xml')