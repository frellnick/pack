# archive.py

import shutil
import os
import zipfile
from zipfile import ZipFile

from archivor.build_metadata import agg_translations

import logging 

archlog = logging.getLogger(__name__)



def create_temp(dirpath):
    def _strip(path):
        return path.strip('/')

    temppath = _strip(dirpath)+'_temp'
    if os.path.isdir(temppath):
        return temppath
    os.mkdir(temppath)
    return temppath


def copy_files(source, destination, filenames=None):
    def _fpath(source, filename):
        return os.path.join(source, filename)

    if filenames is None:
        flist = os.listdir(source)
    else:
        flist = filenames

    for filename in flist:
        archlog.info(f'Copying {filename} from {source} to {destination}')
        shutil.copy(_fpath(source, filename), destination)



def build_zip(filepaths, filenames, zippath):
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
        archlog.info('Compression set to: ZIP_DEFLATED.')
    except:
        compression = zipfile.ZIP_STORED
        archlog.info('Compression set to: ZIP_STORED.')
        
    with ZipFile(zippath, 'w') as zpf:
        for fname, arcname in zip(filepaths, filenames):
            archlog.info(f'Adding file to archive: {fname} as {arcname}.')
            zpf.write(fname, arcname)




def create_archive(dirpath, translations, zipname, filenames: list = None):

    temppath = create_temp(dirpath)
    archlog.info(f'Making temporary directory: {temppath}.')

    metapath = os.path.join(temppath, 'metadata.json')
    agg_translations(translations, filepath=metapath)
    archlog.info(f'Metadata aggregated and dumped to: {metapath}')

    archlog.info('Copying files into temp directory.')
    if filenames is not None:
        filenames = filenames.append('metadata.json')
    copy_files(dirpath, temppath, filenames=filenames)

    filepaths = [os.path.join(temppath, name) for name in os.listdir(temppath)]
    zippath =  os.path.join(dirpath, zipname)
    if os.path.isfile(zippath):
        archlog.warn('ZipFile already exists.  Overwrite not implemented.')
    archlog.info(f'Sending the follwing files to zipbuilder @{zippath} \n {filepaths}')
    build_zip(filepaths=filepaths, filenames=os.listdir(temppath), zippath=zippath)

    clean_temp(temppath)
    return zippath




def clean_temp(temppath):
    shutil.rmtree(temppath)