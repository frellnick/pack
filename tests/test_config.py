import os
import logging 


config = {
    'save': True,
    'logfile': os.path.join(os.getcwd(), 'test.log')
}

def setup(log=True):
    if log:
        logging.basicConfig(filename=config['logfile'], filemode='w', level=logging.DEBUG)