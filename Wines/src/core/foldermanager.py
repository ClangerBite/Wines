"""
This module contains specific context managers used in the application.
"""

import os
from contextlib import contextmanager
        
@contextmanager
def GUI_folder():
    """Temporarily change current working directory to path directory."""
    folder = "Wines/src/gui"
    try:
        cwd = os.getcwd()
        os.chdir(folder)
        yield
    finally:
        os.chdir(cwd)

@contextmanager
def label_folder():
    """Temporarily change current working directory to path directory."""
    folder = "Wines/resources/labels"
    try:
        cwd = os.getcwd()
        os.chdir(folder)
        yield
    finally:
        os.chdir(cwd)
        
@contextmanager
def invoice_folder():
    """Temporarily change current working directory to path directory."""
    folder = "Wines/resoruces/invoices"
    try:
        cwd = os.getcwd()
        os.chdir(folder)
        yield
    finally:
        os.chdir(cwd)