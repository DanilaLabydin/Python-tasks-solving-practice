#!/usr/bin/env python3
import shutil
import psutil
import os


def computer_check():
    # compute all requirement information
    du = shutil.disk_usage('/')
    du_total = du.total / 2 ** 30
    du_used = du.used / 2 ** 30
    du_free = du.free / 2 ** 30
    du_free_percent = du.free / du.total * 100
    cpu_payload = psutil.cpu_percent(1)

    # return the result with all information
    return (f'Total space: {du_total:.2f} GB\n'
            f'Used space: {du_used:.2f} GB\n'
            f'Free space: {du_free:.2f} GB\n'
            f'Percent of free space: {du_free_percent:.2f}\n'
            f'CPU payload: {cpu_payload}')


def check_reboot():
    """Returns True if the computer has a pending reboot"""
    if not os.path.exists("/run/reboot-required"):
        return f'The computer has not a pending reboot'
    else:
        return f'The computer has a pending reboot'


def main():
    print(computer_check())
    print(check_reboot())
    print('HOME:' + os.environ.get('HOME', ""))
    print('SHELL:' + os.environ.get('SHELL', ''))
    print('FRUIT:' + os.environ.get('FRUIT', 'you are a fool'))


if __name__ == '__main__':
    main()
