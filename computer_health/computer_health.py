#!/usr/bin/env python3
##
# create a script that checks main characteristics of a computer's disk space(disk usage, cpu usage)
# and a cpu's payload
#
import shutil
import psutil

#
# create a function that displays a total, used, free space and a percent of free space
# @return a message that contains the requirement information
#
def computer_check():
    # compute all requirement information
    du = shutil.disk_usage('/')
    du_total = du.total / 2 ** 30
    du_used = du.used / 2 ** 30
    du_free = du.free / 2 ** 30
    du_free_percent = du.free / du.total * 100
    cpu_payload = psutil.cpu_percent(1)

    # return the result with all information
    return (f'Total space: {du_total:.2f} GB \n'
            f'Used space: {du_used:.2f} GB \n'
            f'Free space: {du_free:.2f} GB \n'
            f'Percent of free space: {du_free_percent:.2f}\n'
            f'CPU payload: {cpu_payload}')


print(computer_check())
