import VOT as v
import glob

# vt = v.Table_Stage1()
# vt.import_info('calibrated_final_cont.pbcor.info')
# hdfits = './' + vt.head_fits.rsplit('/', 1)[-1]
# print(hdfits)
# vt.fits2vo('./', hdfits)

# del vt
err_log = ''

for f_info in glob.glob('./info2/*.info'):
    vt = v.Table_Stage1()
    print(f_info)
    vt.import_info(f_info)
    # print(vt.core_fitsname)
    # print(vt.fits_abs)
    # vt.setFitsDiscr()
    # print(vt.fv.fits_pre)
    # break
    hdfits = './info2/' + vt.head_fits.rsplit('/', 1)[-1]
    # print(hdfits)
    res = vt.fits2vo('./votable_stage1_test2/', hdfits)
    del vt
    if res:
        err_log += '{}: {}\n'.format(res, hdfits)

with open('./log_2', 'w') as f:
    f.write(err_log)