import subprocess
import sys
import os
multiprocess_wheel = "multiprocess-0.70.15-py38-none-any.whl"
subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-index", os.path.join("/mnt/data/", multiprocess_wheel)])
scipy_wheel = "scipy-1.9.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-index", os.path.join("/mnt/data/", scipy_wheel)])