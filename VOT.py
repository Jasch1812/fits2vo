import f2v_core as f2v


class NameAnalysis:

    def __init__(self):
        self.core_fitsname = ''

    def filename(self, fullname):
        return fullname.rsplit('/')[-1]

    def isFits(self, fullname):
        return self.filename(fullname).rsplit('.', 1)[-1] == 'fits'

    def set_corename(self, head_fitsname):
        temp_fits = self.filename(head_fitsname)
        self.core_fitsname = temp_fits.rsplit('.', 2)[-3]
        return self

    def fits_cond2(self, f_str, patten):
        nm_list = f_str.rsplit('.', 2)
        if len(nm_list) > 2:
            return (nm_list[-3] == self.core_fitsname) \
               and (nm_list[-2] == patten)
        else:
            return False

    def jpg_cond2(self, f_str, patten):
        nm_list = f_str.rsplit('.', 2)
        if len(nm_list) > 2:
            return (nm_list[-3] == self.core_fitsname) \
               and (nm_list[-2] == patten)
        else:
            return False

    def jpg_cond3(self, f_str, patten):
        nm_list = f_str.rsplit('.', 3)
        if len(nm_list) > 3:
            return (nm_list[-4] == self.core_fitsname) \
               and (nm_list[-3] == patten) \
               and (nm_list[-2] == 'large')
        else:
            return False

    def is_m0Fits(self, fullname):
        if self.isFits(fullname):
            temp_nm = self.filename(fullname)
            return self.fits_cond2(temp_nm, 'm0')
        else:
            return False

    def is_HeadFits(self, fullname):
        if self.isFits(fullname):
            temp_nm = self.filename(fullname)
            return self.fits_cond2(temp_nm, 'head')
        else:
            return False

    def is_contFits(self, fullname):
        if self.isFits(fullname):
            temp_nm = self.filename(fullname)
            return self.fits_cond2(temp_nm, 'cont')
        else:
            return False

    def is_polarFits(self, fullname):
        if self.isFits(fullname):
            temp_nm = self.filename(fullname)
            return self.fits_cond2(temp_nm, 'polar_i')
        else:
            return False

    def isJPG(self, fullname):
        return self.filename(fullname).rsplit('.', 1)[-1] == 'jpg'

    def is_Spec(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond2(temp_nm, 'spec_peak')
        else:
            return False

    def is_SpecLarge(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond3(temp_nm, 'spec_peak')
        else:
            return False

    def is_m0JPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            # print(temp_nm)
            return self.jpg_cond2(temp_nm, 'm0')
        else:
            return False

    def is_m0LargeJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond3(temp_nm, 'm0')
        else:
            return False

    def is_contJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond2(temp_nm, 'cont')
        else:
            return False

    def is_contLargeJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond3(temp_nm, 'cont')
        else:
            return False

    def is_polarJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond2(temp_nm, 'polar_i')
        else:
            return False

    def is_polarLargeJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            return self.jpg_cond3(temp_nm, 'polar_i')
        else:
            return False

    def is_LargeJPG(self, fullname):
        if self.isJPG(fullname):
            temp_nm = self.filename(fullname)
            # print(self.core_fitsname)
            # print(temp_nm)
            # temp_nm = temp_nm.strip(self.core_fitsname)
            # print(temp_nm)
            nm_list = temp_nm.rsplit('.', 2)
            # print(nm_list)
            if len(nm_list) == 3:
                return (nm_list[-3] == self.core_fitsname) and (nm_list[-2] == 'large')
            else:
                return False
        else:
            return False

    def get_Type(self, fullname):
        type_list = ['m0_fits', 'cont_fits', 'polar_fits']
        type_list += ['m0_jpg', 'm0_large_jpg']
        type_list += ['cont_jpg', 'cont_large_jpg']
        type_list += ['polar_jpg', 'polar_large_jpg']
        type_list += ['spec_peak_jpg', 'spec_peak_large_jpg']
        type_list += ['jpg', 'large_jpg']
        type_list += ['other']
        if self.isFits(fullname):
            if self.is_m0Fits(fullname):
                i = 0
            elif self.is_contFits(fullname):
                i = 1
            elif self.is_polarFits(fullname):
                i = 2
            else:
                i = 13
        elif self.isJPG(fullname):
            # print(fullname)
            if self.is_m0JPG(fullname):
                i = 3
            elif self.is_m0LargeJPG(fullname):
                i = 4
            elif self.is_contJPG(fullname):
                i = 5
            elif self.is_contLargeJPG(fullname):
                i = 6
            elif self.is_polarJPG(fullname):
                i = 7
            elif self.is_polarLargeJPG(fullname):
                i = 8
            elif self.is_Spec(fullname):
                i = 9
            elif self.is_SpecLarge(fullname):
                i = 10
            elif self.is_LargeJPG(fullname):
                i = 12
            else:
                i = 11
        else:
            i = 13
        return type_list[i]


class BasicTable (NameAnalysis):
    def __init__(self, keys_ignord_basic=['', 'COMMENT', 'HISTORY']):
        NameAnalysis.__init__(self)
        self.fv = f2v.fits2vo('fits', keys_ignord=keys_ignord_basic)
        self._fits_path = ''
        self.LinkKeys = []
        self.table_name = ''

    def set_table_name(self, table_nm):
        if table_nm == 'line':
            self.table_name = 'data_cube'
        else:
            self.table_name = table_nm

    def importFits(self, fits_head):
        '''return a fits handle'''
        return self.fv.import_fits(fits_head)

    def setFitsDiscr(self):
        # fits_nm = self.filename(fits_abs)
        self.fv.set_fits_pre(self.core_fitsname)

    def set_fitsPath(self, fits_abs):
        self._fits_path = 'file://' + fits_abs
        return self

    def get_fitsPath(self):
        return self._fits_path

    def add_FitsLink(self, link_nm, link_cont, link_keys=[]):
        link_keys.append(link_nm)
        ln = self.fv.make_link('image/fits', link_nm, link_cont)
        self.fv.links_dict[link_nm] = ln
        return self

    def add_JPGLink(self, link_nm, link_cont, link_keys=[]):
        link_keys.append(link_nm)
        ln = self.fv.make_link('image/jpeg', link_nm, link_cont)
        self.fv.links_dict[link_nm] = ln
        return self

    def basic_fits2vo(self, fits_head, fits_abs, xml_pre):
        fits_handleList = self.importFits(fits_head)
        if not fits_handleList:
            return 'OpenningError'
        self.setFitsDiscr()
        self.set_fitsPath(fits_abs)
        # self.fv.set_fits_pre(self.core_fitsname)

#   check whether 'fits_handleList' and 'LinkKeys' have the same length
        while len(self.LinkKeys) < len(fits_handleList):
            self.LinkKeys.append([])

        BasicVO = self.fv.make_votable()
        BasicRes = self.fv.make_resource()
        fp = self.get_fitsPath()
        for i in list(range(len(fits_handleList))):
            fitsHD = fits_handleList[i].header
            hdu = self.fv.hdu_unpack(fitsHD)
            if not hdu:
                return 'ExtractingError'
            lk = self.LinkKeys[i]
            table = self.fv.make_table(BasicVO, self.table_name, hdu, fp, lk)
            BasicRes.tables.append(table)
        BasicVO.resources.append(BasicRes)
        self.fv.xml_pre = xml_pre
        self.fv.f2v(BasicVO)
        return 0


class Table_Stage1 (BasicTable):
    def __init__(self, keys_ignord_stage1=['', 'COMMENT', 'HISTORY']):
        BasicTable.__init__(self, keys_ignord_basic=keys_ignord_stage1)
        self.link_images = []

    def import_info(self, info_file):
        info_cont = []
#   read information from info file
        with open(info_file, 'r') as in_file:
            for line in in_file:
                if (' ' in line): # or ('=' in line):
                    break
                elif line == '':
                    continue
                else:
                    info_cont.append(line.strip())
#   'info_cont' is a list
#        print(info_cont)
#   0: fits type, 1: head fits, 2: data fits, other: auxiliary images
#   remove 'fits type' from the list
        self.set_table_name(info_cont.pop(0))
#   remove the 'head fits' from the list
        head_fits = info_cont.pop(0)
        # print(head_fits)
#   remove the 'data filts' from the list
        data_fits = info_cont.pop(0)
        # print(self.table_name)

        if self.isFits(head_fits):
            self.set_corename(head_fits)

        if self.isFits(data_fits):
            self.fits_abs = data_fits
        else:
            raise Exception('Fits does not exist!')

        # print(head_fits)
        if self.is_HeadFits(head_fits):
            self.head_fits = head_fits
        else:
            raise Exception('head.fits does not exist!')
        # print(self.fits_abs)
        # print(self.head_fits)
        # print(self.core_fitsname)

        for img in info_cont:
            if self.isFits(img):
                img_type = self.get_Type(img)
                self.add_FitsLink(img_type, img, self.link_images)
            elif self.isJPG(img):
                img_type = self.get_Type(img)
                self.add_JPGLink(img_type, img, self.link_images)
            else:
                raise Exception('Unkown file exists!')
        self.LinkKeys.append(self.link_images)
        # print(self.LinkKeys)

    def fits2vo(self, xml_pre, headFits):
        return self.basic_fits2vo(headFits, self.fits_abs, xml_pre)



