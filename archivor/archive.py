# archive.py

import shutil
import os
from zipfile import ZipFile

from archivor.build_metadata import agg_translations

def create_temp(dirpath):
    temppath = dirpath+'_temp'
    if os.path.isdir(temppath):
        return temppath
    os.mkdir(temppath)
    return temppath


def copy_files(source, destination):
    def _fpath(source, filename):
        return os.path.join(source, filename)

    for filename in os.listdir(source):
        shutil.copy(_fpath(source, filename), destination)


def create_archive(dirpath, translations, zipname):
    def build_zip(filepaths, zippath):
        with ZipFile(zippath, 'w') as zpf:
            for f in filepaths:
                zpf.write(f)

    temppath = create_temp(dirpath)
    metapath = os.path.join(temppath, 'metadata.json')
    agg_translations(translations, filepath=metapath)
    copy_files(dirpath, temppath)

    filepaths = [os.path.join(temppath, name) for name in os.listdir(temppath)]
    zippath =  os.path.join(dirpath, zipname)
    build_zip(filepaths,zippath)

    clean_temp(temppath)

    return zippath


def clean_temp(temppath):
    shutil.rmtree(temppath)