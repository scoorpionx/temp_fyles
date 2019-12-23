import os
import shutil


def tempDesktop():
    del_dir = f"C:\\Windows\\Temp"
    shutil.rmtree(del_dir, ignore_errors=True)
    if del_dir == False:
        os.makedirs(del_dir)