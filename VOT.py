import f2v_core as f2v 

x = []

with open('TW_Hya_HCO.pbcor.info', 'r') as file:
    for line in file:
        if ' ' in line:
            break
        else:
            x.append(line.strip())


nm = []

for i in x[1:]:
    nm.append(i.rsplit('/')[-1])

# print(len(nm))
for n in nm:
    print(n.rsplit('.',3))

for n in nm:
    if 'fits' == n[-4:]:
        if 'head' in n:
            print("Head Fits -> {}".format(n))
        elif 'm0' == n.rsplit('.',3)[-2]:
            print("m0 Fits -> {}".format(n))
        else:
            print("Fits -> {}".format(n))
    elif 'jpg' in n:
        if 'spec_peak.large' in n:
            print('Spectrum Peak Large -> {}'.format(n))
        elif 'spec_peak' in n:
            print('Spectrum -> {}'.format(n))
        elif 'm0.large' in n:
            print('m0 Large JPG -> {}'.format(n))
        elif 'm0' in n:
            print('m0 JPG -> {}'.format(n))
        else:
            print('JPG -> {}').format(n)
    else:
        print("Rest -> {}".format(n))

class CubeTable:

class ContinuumTable:
    pass

class VOTable:
    def __init__(self):
        pass

    def filename(self, fullname):
        return fullname.rsplit('/')[-1]

    def isFits(self, fullname):
        return self.filename(fullname).rsplit('.',1)[-1] == 'fits'

    def is_m0Fits(self, fullname):
        if self.isFits(fullname):
            return self.filename(fullname).rsplit('.', 2)[-2]=='m0'
        else:
            return False

    def is_HeadFits(self, fullname):
        if self.isFits(fullname):
            return self.filename(fullname).rsplit('.', 2)[-2]=='head'
        else:
            return False

    def isPureFits(self, fullname):
        if not self.isFits(fullname):
            return False
        elif self.is_HeadFits(fullname):
            return False
        elif self.is_m0Fits(fullname):
            return False
        else:
            return True

    def isJPG(self, fullname):
        return self.filename(fullname).rsplit('.',1)[-1]=='jpg'

    def is_Spec(self, fullname):
        if self.isJPG(fullname):
            self.filename(fullname).rsplit('.',2)[-2] == 'spec_peak'
        else:
            return False

    def is_LargeSpec(self, fullname):
        if self.isJPG(fullname):
            nm_list = self.filename(fullname).rsplit('.',3)
            return (nm_list[-3]=='spec_peak') and (nm_list[-2]=='large')
        else:
            return False

    def is_m0JPG(self, fullname):
        if self.isJPG(fullname):
            return self.filename(fullname).rsplit('.',2)=='m0'
        else: 
            return False 

    def is_m0LargeJPG(self, fullname):
        if self.isJPG(fullname):
            nm_list = self.filename(fullname).rsplit('.',3)
            return (nm_list[-3]=='m0') and (nm_list[-2]=='large')
        else: 
            return False

    def isPureJPG(self, fullname):
        if not self.isJPG(fullname):
            return False
        elif self.is_Spec(fullname):
            return False
        elif self.is_LargeSpec(fullname):
            return False
        elif self.is_m0JPG(fullname):
            return False
        elif self.is_m0LargeJPG(fullname):
            return False
        else:
            return True

