import os
import telebot
from wakeonlan import send_magic_packet

################################--Setup--###################################################

BOT_TOKEN = "1234567890:AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQq" # Replace this with a bot token that you can get from @BotFather
bot = telebot.TeleBot(BOT_TOKEN)
user_id = 987654321 # Replace this with your telegram account's user id(to make sure that only your account can access the commands).
pc_hostname = "somepc" # Replace this with your pc's hostname.
pc_ip = '192.168.0.100' # Replace this with your pc's local IP address.
pc_mac = '1A-2B-3D-4C-5D-6E' # Replace this with your pc's MAC address.
pc_ssh_user = 'user' # Replace this with your username that is on you pc.
pc_ssh_passwd = 'your_password' # Replace this with your password.

##################################--Lang--#####################################################

# Here you can customize the bot's responses. 
Turning_on = "Turning the computer on..."
Turning_off = "Turning the computer off..."
Already_on = "The computer is already on"
Already_off = "The computer is already off"
Status_on = "The computer is on."
Status_off = "The computer is off."
No_permission = "You cannot use this command!"

################################--Functions--###################################################

def pcon():
    send_magic_packet(pc_mac, ip_address=pc_ip, port=9)

def pcoff():
    os.system('sshpass -p ' + pc_ssh_passwd + ' ssh ' + pc_ssh_user + '@' + pc_hostname + ' shutdown /s /t 0')

def ping(host):
    response = os.system("ping -c 1 -i 0.2 " + host)
    if response == 0:
        status = "true"
    else:
        status = "false"
    return(status)

################################--Commands--####################################################

#remotely turn on
@bot.message_handler(commands=['remote_on'])
def handle_wol(message):
    if message.from_user.id == user_id:
        if ping(pc_hostname) == "false":
            bot.send_message(message.chat.id, Turning_on)
            pcon()
        else:
            bot.send_message(message.chat.id, Already_on)
    else:
        bot.send_message(message.chat.id, No_permission)

#check status
@bot.message_handler(commands=['status'])
def handle_status(message):
    if message.from_user.id == user_id:
        if ping(pc_hostname) == "true":
            bot.send_message(message.chat.id, Status_on)
        else:
            bot.send_message(message.chat.id, Status_off)
    else:
        bot.send_message(message.chat.id, No_permission)

#remotely turn off
@bot.message_handler(commands=['remote_off'])
def handle_status(message):
    if message.from_user.id == user_id:
        if ping(pc_hostname) == "true":
            bot.send_message(message.chat.id, Turning_off)
            pcoff()
        else:
            bot.send_message(message.chat.id, Already_off)
    else:
        bot.send_message(message.chat.id, No_permission)

bot.infinity_polling()
