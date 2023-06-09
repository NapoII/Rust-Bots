################################################################################################################################
# Telegram_Bot_einrichten.py
from Imports import*
import webbrowser

webbrowser.open("https://core.telegram.org/bots#3-how-do-i-create-a-bot")
pyautogui.alert(text='Zuerst musst du dir einen Telegram Bot erstellen\n und dir den Token zu deinem Bot Kopieren!', title='Rust - SellBot - Telegram Set-Up', button='Lets Go!')


Telegram_token = "5357034455:AAE785813q8L1np9oBoq0S6Vmyr9MB2F_oU"
config_dir = "Rust - SellBot/config.ini"

Token = pyautogui.prompt(text='Gib den Telegram Bot Token hier ein:', title='Rust - SellBot - Telegram Set-Up' , default='5357034455:AAE785813q8L1np9oBoq0S6Vmyr9MB2F_oU')
write_config(config_dir, "Telegram", "Telegramm_token", str(Token))

pyautogui.alert(text='Schreibe deinen Telegram Bot nun an mit: !id . Danach drücke Hier auf "Weiter". ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')

while True:
    try:
        Last_Chat_data = Last_Chat(Telegram_token)
    except:
        while True:
            pyautogui.alert(text='Schreibe deinen Telegram Bot nun an mit: !id . Danach drücke Hier auf "Weiter". ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')
            Last_Chat_data = Last_Chat(Telegram_token)
    if Last_Chat_data[0] == "" or Last_Chat_data[0] != "!id":
        pyautogui.alert(text='Schreibe deinen Telegram Bot nun an mit: !id . Danach drücke Hier auf "Weiter". ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')
        Last_Chat_data = Last_Chat(Telegram_token)

    if Last_Chat_data[0] == "!id":
        print ("\nID gefunden!\n")
        break

Chat_ID =(Last_Chat_data[1])
write_config(config_dir, "Telegram", "chat_Id", str(Chat_ID))

webbrowser.open("https://imgur.com/account/settings/apps")
pyautogui.alert(text='Erstelle nun ein Imgur Token. ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')

CLINT_ID_imgur = pyautogui.prompt(text='Gib die Imgur Client ID hier ein:', title='Rust - SellBot - Telegram Set-Up' , default='fb9b5757ec16f06')
CLINT_Secret_imgur = pyautogui.prompt(text='Gib den Imgur Client Secret hier ein:', title='Rust - SellBot - Telegram Set-Up' , default='c8eadb8777f5bbebf4c408fa039420e18e153cc8')


write_config(config_dir, "Imgur", "CLINT_ID_imgur", str(CLINT_ID_imgur))
write_config(config_dir, "Imgur", "CLINT_Secret_imgur", str(CLINT_Secret_imgur))


pyautogui.alert(text='Fertig der Telegram Bot wurde eingerichtet. ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')

TeleBot_Say("Fertig der Telegram Bot wurde eingerichtet.\n schreibe  /scr  um die Bildfunkzion zu testen.", Chat_ID, Token)
chat_date_id = 0
chat_date_id_ref = 1

fullscrean = parse_int_tuple(read_config(config_dir, "Imgur", "fullscrean"))

while True:
    Last_chat_Data = Last_Chat(Telegram_token)

    if Last_chat_Data[0] == "/scr" and chat_date_id != chat_date_id_ref:

        log ("Screanshot wurde an den Telebot gesendet.")
        Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_Bilder)
        TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, Chat_ID, Telegram_token )
        chat_date_id_ref = Last_chat_Data[2]
        break
    else:
        TeleBot_Say("Schreibe nun  /scr  in den Telegram Chat um die Bild funktzion zu Testen! ", Chat_ID, Token)
        pyautogui.alert(text='Schreibe nun  /scr  in den Telegram Chat um die Bild funktzion zu Testen! ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')


TeleBot_Say(" Der Telegram Bot ist einsatzbereit für den Rust Sell Bot", Chat_ID, Token)
write_config(config_dir, "Telegram", "Bot_aktiv", "True")
pyautogui.alert(text='Fertig!. ', title='Rust - SellBot - Telegram Set-Up', button='Weiter')






