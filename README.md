# fits2vo

## Files in this directory

'Q0NXaWxkV29yZHMtQm9sZEl0YWxpYy50dGY=.png'	-> a PNG figure of letter "A" from non-MNIST set;

'A_vo_binary.xml'							-> VOTable of the PNG figure with a data stream as 'BINARY';
'A_vo_binary2.xml'							-> VOTable of the PNG figure with a data stream as 'BINARY2';
'A_fits.fits'								-> A fits file converting from the PNG figure;
'A_vo_fits.xml'								-> VOTable of the PNG figure with a extra link of 'FITS' stream;
'fits_test.py'								-> python script converting the PNG to FITS;
'vo_test.py'								-> python script converting the PNG to VOTable with 'TABLEDATA', 'BINARY' or 'BINARY2';
'vo_test2.py'								-> python script converting the PNG to VOTable with FITS link;
'TWHYA_BAND7'								-> a directory of sample fits files of ALMA data;
'treeFits.py'								-> this script originates from 'tree.py' in the official 'astropy' package as 'astropy.io.votable.tree'. It is modified to support for FITS link writing;
'f2v.py'									-> python script converting a fits file to VOTable with all related parameters in 'string' format as PARAMs;
'f2v_2.py'									-> python script convertng a fits file to VOTable with all related parameters in their own format as PARAMs;
'f2v_3.py'									-> python script convertng a fits file to VOTable with all related parameters in their own format in a Table.
