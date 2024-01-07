import subprocess
import sys
import os
salib_wheel = "salib-1.4.7-py3-none-any.whl"
subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-index", os.path.join("/mnt/data/", salib_wheel)])