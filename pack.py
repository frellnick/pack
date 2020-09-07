# pack.py

from profile import Profiler
from translator import OracleTranslator
from archivor import create_archive

import os
import datetime

from config import setup
import logging

log = logging.getLogger(__name__)



def run_pack(data_dir, **kwargs):
    setup(logpath=data_dir)
    date = datetime.datetime.now()
    fdate = '-'.join([str(x) for x in [date.year, date.month, date.day]])
    log.info(f'Setup complete.  Beginning pack of {data_dir} on {date}.')
    log.info(f'Optional arguments used: {kwargs}')
    
    filenames = os.listdir(data_dir)
    log.info(f'Found the following files: \n {filenames}.')

    data_paths = _clean_list(
        _build_paths(flist=filenames, root=data_dir), '.log'
    )
    filenames = _clean_list(filenames, '.log')

    
    log.info('Beginning Profiling and Translation.')
    translations = []

    cleanfiles = []

    for i, f in enumerate(data_paths):
        prf = Profiler()
        fname = prf.load_csv(f, low_memory=False, save_copy=True)
        cleanfiles.append(fname)
        tablename = os.path.basename(os.path.normpath(fname))
        tlr = OracleTranslator(tablename=tablename)
        translations.append(tlr(prf.profile))
        log.info(f'Successfully cleaned and profiled {filenames[i]}')

    if 'zipname' in kwargs:
        zipname = kwargs['zipname']
    else:
        zipname = f'PARTNERID_TESTFILE_{fdate}.zip'

    log.info(f'Aggregating translated metadata and attempting build of: {zipname}')
    log.info(f'Using files: {cleanfiles}')
    zippath = create_archive(
        translations=translations, 
        dirpath=data_dir, 
        zipname=zipname,
        filenames=cleanfiles,
        )

    

def _build_paths(flist, root):
    return [os.path.join(root, f) for f in flist]

def _clean_list(flist, phrase, other=['.zip']):
    def _clear_clist(f, clist):
        checks = [s in f for s in clist]
        return sum(checks) == 0

    clist = [phrase]
    clist.extend(other)
    return [f for f in flist if _clear_clist(f, clist)]


def _check_valid_path(path):
    fullpath = os.path.join(os.getcwd(), path)
    relpath = path
    
    if os.path.isdir(relpath):
        return relpath
    elif os.path.isdir(fullpath):
        return fullpath
    else:
        raise ValueError(f'Could not find {path}')



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Package folder of data for UDRC Import.')

    parser.add_argument('path', help='path to data directory')
    parser.add_argument('--zipname', help='Specify output zip filename.')

    args = parser.parse_args()

    kwargs={}
    if args.zipname:
        kwargs['zipname'] = args.zipname

    run_pack(
        data_dir=_check_valid_path(args.path),
        **kwargs,
        )

