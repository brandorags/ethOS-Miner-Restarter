# ethOS Miner Restarter
ethOS Miner Restarter is a Python script that checks the hashrate production of your mining rig and will restart any GPUs that are not mining to make sure your hard-earned money isn't going to waste.   

## Required Software
- ethOS Operating System
- Python 3

While the above requirements may be obvious to state, this is to inform users who have come to this repository looking for a similar solution but have a different operating system. If you are using an operating system other than ethOS, ethOS Miner Restarter will not work.

## How to Use
#### Step 1 - Download ethOS Miner Restarter
First, create a new directory from your home directory (`/home/ethos`):
```
mkdir ethos_miner_restarter
```
Second, navigate to the newly created directory:
```
cd ethos_miner_restarter
```
Third, download ethOS Miner Restarter from this repository:
```
wget https://raw.githubusercontent.com/brandorags/ethOS-Miner-Restarter/master/ethos_miner_restarter.py
```
#### Step 2 - Create a Cron Job for ethOS Miner Restarter
By creating a cron job, you can ensure that ethOS Miner Restarter will run at a scheduled time indefinitely, even if your rig is rebooted.

First, make ethOS Miner Restarter executable:
```
chmod 755 ethos_miner_restarter.py
```
Second, create a new cron job by opening the crontab editor (the following instructions assume you are using `nano` as your editor of choice):
```
crontab -e
```
Third, insert the following line at the bottom of the editor:
```
*/15 * * * * /home/ethos/ethos_miner_restarter/ethos_miner_restarter.py CUSTOM_PANEL_ID >/dev/null 2>&1
```
while taking note that `CUSTOM_PANEL_ID` is the custom name that you gave your ethOS dashboard subdomain (i.e., `http://CUSTOM_PANEL_ID.ethosdistro.com`). 

After inserting the line, press ctrl+x to save and close the editor. The cron job will take effect immediately and will run ethOS Miner Restarter every 15 minutes.
## Troubleshooting
The first time ethOS Miner Restarter is run, it will create a log file called `ethos_miner_restarter.log` in the same directory as the script. If ethOS Miner Restarter isn't working as intended, refer to this log file.  
## License
This software is licensed under the MIT License. For more information, see the [LICENSE](https://raw.githubusercontent.com/brandorags/ethOS-Miner-Restarter/master/LICENSE).
## Donate
ethOS Miner Restarter is absolutely free for anyone to use. However, if this software has made a difference for you, feel free to give a donation!

ETH - `0x45eeaBf24A6A2B6884CF70CEf0051D5993ec577C`

BTC - `1HJcTFBkxKnPVybA8rc1t4KARb7fMWH9ic`