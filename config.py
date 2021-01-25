import os
import sys
import logging 


config = {
    'save': True,
    'logfile': os.path.join(os.getcwd(), '.log')
}

def setup(log=True, **kwargs):
    if 'logpath' in kwargs:
        config['logfile'] = os.path.join(kwargs['logpath'], 'pack.log')
    if log:
        handlers = [
            logging.FileHandler(filename=config['logfile'],mode='w'),
            logging.StreamHandler(sys.stdout)
        ]
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
            handlers=handlers
            )