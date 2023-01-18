"""
This module contains a context manager used in the application to temporarily 
change the current working directory to another directory. Allows location of 
the data folders to be easily changed.
"""

import os
from contextlib import contextmanager

gui_folder = "Wines/src/gui"
label_folder = "Wines/resources/labels"
invoice_folder = "Wines/resources/invoices"
dbase_folder = "Wines/resources/database"
        
@contextmanager
def directory(folder):
    try:
        cwd = os.getcwd()
        os.chdir(folder)
        yield
    finally:
        os.chdir(cwd)