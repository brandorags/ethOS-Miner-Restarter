#!/usr/bin/env python3


# Copyright (c) 2018 Brandon Ragsdale
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import subprocess
import traceback
import logging
import json

from urllib import request
from time import sleep
from sys import argv


logging.basicConfig(filename='/home/ethos/ethos_miner_restarter/ethos_miner_restarter.log',
                    format='[%(levelname)s] %(asctime)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


def get_rigs():
    custom_panel_id = argv[1]
    panel_dashboard_url = 'http://{0}.ethosdistro.com/?json=yes'.format(custom_panel_id)
    
    panel_dashboard_data = request.urlopen(panel_dashboard_url).read().decode('utf-8')
    panel_dashboard_json = json.loads(panel_dashboard_data)

    rigs = panel_dashboard_json['rigs']

    return rigs


def does_miner_need_restart():
    rigs = get_rigs()

    for rig in rigs:
        miner_condition = rigs[rig]['condition']
        if miner_condition != 'stuck_miners':
            continue

        miner_hashes = rigs[rig]['miner_hashes'].split(' ')
        for miner_hash in miner_hashes:
            if float(miner_hash) == 0:
                return True
    
    return False


def restart_miners():
    subprocess.call('/opt/ethos/bin/minestop', shell=True)
    sleep(10)
    subprocess.call('/opt/ethos/bin/minestart', shell=True)


def reboot_system():
    subprocess.call('/opt/ethos/bin/r', shell=True)


def main():
    miner_needs_restart = does_miner_need_restart()   
    if miner_needs_restart:
        # first, restart the miners
        logging.info('One of the GPUs is not producing hashrates. Restarting miners now.')
        restart_miners()

        # wait for the miners to begin
        # producing hashrates
        sleep(360)

        miner_needs_restart = does_miner_need_restart()
        if miner_needs_restart:
            # the restarting of the miners
            # failed, so reboot the system
            logging.info('One of the GPUs is still not producing hashrates. Rebooting the system now.')
            reboot_system()
        else:
            logging.info('All GPUs are producing hashrates. Exiting script.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        stack_trace = str(e) + '\n' + traceback.format_exc()
        logging.error(stack_trace)
