import astropy.io.fits as fits
import astropy.io.votable.treeFits as vo
import glob
import os
import numpy as np

class fits2vo:

  def __init__(self, formt, keys_ignord = ['', 'COMMENT', 'HISTORY']):
    self._format = formt
    self._keysRM = keys_ignord
    self._href = ''
    self.xml_end = ''
    self.xml_pre = ''
    self._key_len = 0
    self._val_len = 0
    self._com_len = 0
    self._hdu_list = []
    self._fits_handle = ''

  def clean(self):
    del self._hdu_list[:]
    self._href = ''
    self._key_len = 0
    self._val_len = 0
    self._com_len = 0


  def str_max(self, string, length):
    #measure the maxium length of string in a column
    len_str = len(string)
    if len_str > length:
      return len_str
    else:
      return length

  def hdu_unpack(self):
    '''converting the HDU of fits into a list. 
     Each element in the list is a 4-element list,
     which is in the form of [key, float-value, string-value, comment].
     The value is either float or string, so if the value itself is in type of float,
     string-value is a empty string.'''
     #read HDU of a fits
    hdu_dict = dict( self._header )
    hdu_keys = list( set(hdu_dict.keys()) )
    # remove some keys user-defined
    if self._keysRM:
      for rmKey in self._keysRM:
        if rmKey in hdu_keys:
          hdu_keys.remove( rmKey )
  
    hdu_keys.sort()
    for i in range( len(hdu_keys) ):
      k = hdu_keys[i]
      v = self._header[k]
      v_type = type(v).__name__ #get the type of the value
      com = self._header.comments[k] # get the comment
      #measure the maxium lengths of the key and comment
      self._key_len = self.str_max(str(k), self._key_len) 
      self._com_len = self.str_max( str(com), self._com_len )

      #appending of 4-element list of the paramenter in HDU
      if (v_type=='int') or (v_type=='float'):
        self._hdu_list.append([k, str(v), '', com])
      else:
        self._hdu_list.append([k, '', str(v), com])
        self._val_len = self.str_max( str(v), self._val_len)

  def import_fits( self, fitsfile ):
    self._fitsfile = fitsfile
    self._fits_handle = fits.open( self._fitsfile )[0]
    # print(self._fits_handle)
    self._header = self._fits_handle.header
    # print(self._header)
    self.fits_nm = fitsfile.rsplit('/', 1)[-1]
    self.fits_pre = self.fits_nm.rsplit('.', 1)[-2]

  # def href_setter(self):
  #   if self._href:
  #     return self._href
  #   else:
  #     if(os.path.exists(fits0)):
  #       return 'file://' + os.path.abspath(fits0)

  def href_setter(self):
    if(os.path.exists( self._fitsfile )):
      return 'file://' + os.path.abspath(self._fitsfile)

  @property 
  def href(self):
    return self._href

  # @href.setter
  # def href(self, href=''):
  #   if not href:
  #     self._href = href
  #   else:
  #     self._href = self.href_setter()

  def _votable_maker(self):
    if self._hdu_list:
      self.clean()
    self.hdu_unpack()
    # print("1->{}".format(self.href))

    if not self.href:
      self._href = self.href_setter()
    # print("2->{}".format(self.href))

    votable = vo.VOTableFile(version='1.2')
    resource = vo.Resource()
    resource.description = self.fits_pre
    votable.resources.append( resource )

    table = vo.Table(votable)
    field0 = vo.Field(votable, name='key', datatype='char', arraysize=str(self._key_len))
    field1 = vo.Field(votable, name='value_float', datatype='double')
    field2 = vo.Field(votable, name='value_str', datatype='char', arraysize=str(self._val_len) )#str(vlen)+'*')
    field3 = vo.Field(votable, name='comments', datatype='char', arraysize=str(self._com_len) )#str(clen)+'*')
    table.fields.append(field0)
    table.fields.append(field1)
    table.fields.append(field2)
    table.fields.append(field3)
    table.para_array = self._hdu_list
    table.format = self._format
    # print(self.href)
    table.set_href( self.href )
    resource.tables.append(table)

    votable.to_xml( self.xml_pre + self.fits_pre + self.xml_end + '.xml')

  def f2v(self):
    # self.href = href_p 
    self._votable_maker( )


if __name__ == '__main__':
  fitsList = glob.glob('./TWHYA_BAND7/*.fits')
  fits0 = fitsList[0]

  fv = fits2vo('fits')

  fv.import_fits( fits0 )
  fv.xml_end = '7'
  fv.f2v()