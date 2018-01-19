from f2v_core import f2vCore
import astropy.io.fits as fits


class BasicTable (f2vCore):
    def __init__(self, vo_writer, keys_ignord_basic=['', 'COMMENT', 'HISTORY']):
        f2vCore.__init__(self, 'fits', vo_writer, keys_ignord=keys_ignord_basic)
        self._fits_path = ''
        self.LinkKeys = []
        self.table_name = ''
        self.project_id = ''
        self._fits_handle = ''
        self.description = ''

    def set_table_name(self, table_nm):
        if table_nm == 'line':
            self.table_name = 'data_cube'
        elif table_nm == 'polar':
            self.table_name = 'polarization'
        else:
            self.table_name = table_nm

    def importFits(self, fitsfile):
        '''return a fits handle'''
        # self._fitsfile = fitsfile
        try:
            self._fits_handle = fits.open(fitsfile)
        except:
            self._fits_handle = []
        return self._fits_handle

    def setFitsDiscr(self, Beschreibung):
        # fits_nm = self.filename(fits_abs)
        self.description = Beschreibung

    def set_fitsPath(self, fits_abs):
        self._fits_path = 'file://' + fits_abs
        return self

    def get_fitsPath(self):
        return self._fits_path

    def add_FitsLink(self, link_nm, link_cont, link_keys=[]):
        link_keys.append(link_nm)
        ln = self.make_link('image/fits', link_nm, link_cont)
        self.links_dict[link_nm] = ln
        return self

    def add_JPGLink(self, link_nm, link_cont, link_keys=[]):
        link_keys.append(link_nm)
        ln = self.make_link('image/jpeg', link_nm, link_cont)
        self.links_dict[link_nm] = ln
        return self

    def basic_fits2vo(self, fits_hdu, fits_abs, xml_pre_nm, xml_pre_path):
        fits_handleList = self.importFits(fits_hdu)
        if not fits_handleList:
            return 'OpenningError'
        # self.setFitsDiscr()
        self.set_fitsPath(fits_abs)
        # self.fv.set_fits_pre(self.core_fitsname)

        # check whether 'fits_handleList' and 'LinkKeys' have the same length
        while len(self.LinkKeys) < len(fits_handleList):
            self.LinkKeys.append([])

        BasicVO = self.make_votable()
        # print(self.project_id)
        BasicRes = self.make_resource(self.project_id, self.description)
        fp = self.get_fitsPath()
        for i in list(range(len(fits_handleList))):
            fitsHD = fits_handleList[i].header
            hdu = self.hdu_unpack(fitsHD)
            if not hdu:
                return 'ExtractingError'
            lk = self.LinkKeys[i]
            table = self.make_table(BasicVO, self.table_name, hdu, fp, lk)
            BasicRes.tables.append(table)
        BasicVO.resources.append(BasicRes)
        BasicVO.to_xml(xml_pre_path + xml_pre_nm + '.xml')
        return 0

