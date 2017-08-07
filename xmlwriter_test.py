import textwrap
import contextlib

def xml_escape_cdata(s):
  s = s.replace("&", "&amp;")
  s = s.replace("<", "&lt;")
  s = s.replace(">", "&gt;")
  return s

def xml_escape(s):
  s = s.replace("&", "&amp;")
  s = s.replace("'", "&apos;")
  s = s.replace("\"", "&quot;")
  s = s.replace("<", "&lt;")
  s = s.replace(">", "&gt;")
  return s

class xml_writer:
  def __init__(self, file):
    self.write = file.write
    if hasattr(file, "flush"):
      self.flush = file.flush
    self._open = 0
    self._tags = []
    self._data = []
    self._indentation = " " * 64

    self.xml_escape_cdata = xml_escape_cdata
    self.xml_escape = xml_escape

  def _flush(self, indent=True, wrap=False):
    if self._open:
      if indent:
        self.write(">\n")
      else:
        self.write(">")
      self._open = 0

    if self._data:
      data = ''.join(self._data)
      if wrap:
        indent = self.get_indentation_spaces(1)
        data = textwrap.fill(data, initial_indent=indent, subsequent_indent=indent)
        self.write('\n')
        self.write(self.xml_escape_cdata(data))
        self.write('\n')
        self.write(self.get_indentation_spaces())
      else:
        self.write(self.xml_escape_cdata(data))
      self._data = []

  def start(self, tag, attrib={}, **extra):
    self._flush()
    self._data = []
    self._tags.append(tag)
    self.write(self.get_indentation_spaces(-1))
    self.write("<{}".format(tag))
    if attrib or extra:
      attrib = attrib.copy()
      attrib.update(extra)
      attrib = list(attrib.items())
      attrib.sort()
      # print(attrib)
      for k, v in attrib:
        # print("{}->{}".format(k,v))
        if v is not None:
          # print(v)
          v = self.xml_escape(v)
          # print(v)
          self.write(" {}=\"{}\"".format(k, v))
    self._open = 1
    return len(self._tags)

  def get_indentation_spaces(self, offset=0):
    return self._indentation[: len(self._tags)+offset]

  def end(self, tag=None, indent=True, wrap=False):
    tag = self._tags.pop()
    if self._data:
      self._flush(indent, wrap)
    elif self._open:
      self._open=0
      self.write("/>\n")
      return 
    if indent:
      self.write(self.get_indentation_spaces())
    self.write("<{}>\n".format(tag))

  @contextlib.contextmanager
  def tag(self, tag, attrib={}, **extra):
    self.start(tag, attrib, **extra)
    yield
    self.end(tag)

def f_test(x_nm, f_nm):
  f = open(x_nm,'w')
  w = xml_writer(f)

  with w.tag('FITS'):
    with w.tag('STREAM', attrib={'href':f_nm}):
      w._flush()

if __name__ == '__main__':
  f_test('fits_test', 'haha')
