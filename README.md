# telegram-pc-control-bot
Telegram bot that allows you to remotely turn your computer on or off and view it's status.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/Vladusas/telegram-pc-control-bot.git
   ```
2. Install all the dependencies:
   ```bash
   sudo apt install python3 python3-pip screen nano
   pip install wakeonlan telebot
   ```
3. Run `cd telegram-pc-control-bot`.
4. Run `nano main.py`.
5. Edit the setup section:
   - Replace `BOT_TOKEN` with a bot token that you can get from @BotFather
   - Replace `user_id` with your telegram account's user id(to make sure that only your account can access the commands).
   - Replace `pc_hostname` with your pc's hostname.
   - Replace `pc_ip` with your pc's local IP address.
   - Replace `pc_mac` with your pc's MAC address.
   - Replace `pc_ssh_user` with your username that is on you pc.
   - Replace `pc_ssh_passwd` with your password.
6. Run `./start.sh`.
7. Now you can power on/off your computer and check if it is online using:
   - `/remote_on` To power on your computer remotely.
   - `/remote_off` To power off your computer remotely.
   - `/status` To check the status of your computer.

Note that to power your computer off using this bot you have to install an openssh server.
Also note that this script has to be installed on another computer that is running Linux, is on the same local network and preferably is always on.
If somethig doesen't work open an issue in the Issues tab.

## FAQ
1. "it doesen't work!"
   - Sorry, it does for me.
