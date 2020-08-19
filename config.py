import os
import logging 


config = {
    'save': True,
    'logfile': os.path.join(os.getcwd(), '.log')
}

def setup(log=True, **kwargs):
    if 'logpath' in kwargs:
        config['logfile'] = os.path.join(kwargs['logpath'], 'pack.log')
    if log:
        logging.basicConfig(filename=config['logfile'], filemode='w', level=logging.DEBUG)