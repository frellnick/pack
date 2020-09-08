# utils.py
import numpy as np
import logging

ulog = logging.getLogger(__name__)



def check_datetime(values):
    return False


def utf8len(s):
    try:
        return len(s.encode('utf-8'))
    except Exception as e:
        if np.isnan(s):
            return 0
        else:
            return len(str(s).encode('utf-8'))


def signif_dig(n):
    def _count_digits(n):
        c = str(n).replace('.', '')
        c = c.strip()
        return len(c)
    
    cp = str(n).split('.')

    try:
        assert len(cp) < 3, 'Number not formatted properly'
        return _count_digits(n)
    except Exception as e:
        ulog.warning(f'Error analyzing number: {n}')
        ulog.error(e)
        return None


def count_mantissa(n):
    def _count_left(n):
        try:
            return max(len(cp[0].lstrip('0')), 1)
        except:
            return 0

    def _count_right(n):
        try:
            return max(len(cp[1].rstrip('0')), 1)
        except:
            return 0
    
    cp = str(n).split('.')

    try:
        assert len(cp) < 3, 'Number not formatted properly'
        r = _count_right(cp)
        return r
    except Exception as e:
        ulog.warning(f'Error analyzing number: {n}')
        ulog.error(e)
        return None