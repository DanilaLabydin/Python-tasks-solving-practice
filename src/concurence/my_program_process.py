import os
import subprocess


# get the process id
print(os.getpid())

# get the current work diractory
print(os.getcwd())

# run the system process (pass the command name in the method argument)
ret = subprocess.getoutput("date -u | wc")
print(ret)
