import platform
import os

if platform.os=="linux":
    os.system("run.sh")
elif platform.os=="windows":
    os.system("echo UNDER CODING")