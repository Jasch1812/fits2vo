import astropy.io.votable.tree as vo 
from scipy import misc
import numpy as np 
import glob
from astropy.io.votable import parse


nm = glob.glob('./*.png')[0]
imArr = misc.imread(nm).astype(np.int32)
r, c = imArr.shape
# print imArr.dtype

votable = vo.VOTableFile()

resource = vo.Resource()

votable.resources.append(resource) # appending resource into votable

table = vo.Table(votable)
resource.tables.append(table)
table.description = 'Lette A from non-MNIST set'

group = vo.Group(table)
table.groups.append(group)
para = vo.Param(votable, name='label', datatype='char', arraysize='1', value='A')
group.entries.append(para)


# table.fields.extend([ \
#       vo.Field(votable, name="filename", datatype="char", arraysize="*"), \
#       vo.Field(votable, name="matrix", datatype="double", arraysize="2x2")]) 

for i in range(c):
  # id = 'ID="col%s"' % i
  field_ref=vo.FieldRef(table, ref="col%s" % i)
  group.entries.append(field_ref)
  table.fields.append(vo.Field(votable, ID="col%s" % i, name="D%s" % i, datatype='int'))
  
# table.create_arrays(2)
# table.array[0] = ('test1.xml', [[1,0], [0,-1]])
# table.array[1] = ('test2.xml', [[0,-1], [1,0]])

table.create_arrays(r)
for i in range(r):
  table.array[i] = imArr[i]

votable.to_xml('A_vo_tabledata.xml')
# votable.to_xml('A_vo_binary.xml', tabledata_format='binary')
# votable.to_xml('A_vo_binary2.xml', tabledata_format='binary2')