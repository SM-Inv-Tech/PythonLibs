#!/usr/bin/env python3

import subprocess
import os
import shutil


def remove_ipynb(path):
    files = os.listdir(path)
    for each_file in files:
        if os.path.isdir(os.path.join(path, each_file)):
            if each_file == ".ipynb_checkpoints":
                shutil.rmtree(os.path.join(path, each_file))
            else:
                remove_ipynb(os.path.join(path, each_file))


if __name__ == "__main__":
    remove_ipynb(os.getcwd())
