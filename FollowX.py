import os
import time
import random
import requests
import datetime
import threading
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class colors:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PINK = '\033[95m'
    CYAN = '\033[96m'    
    NONE = '\033[0m'

def log(error):
    with open(os.getcwd() + "/FollowXLog.txt", "a") as file:
        file.write(error + "\n")

class API:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged = False
        self.signed = False
        self.hyper = False
        self.failed = False
        self.okok = False

    def start(self):
        self.run = True
        self.stopped = False

    def stop(self):
        self.run = False
        self.stopped = True

    def asleep(self, x):
        for _ in range(x):
            if self.stopped:
                break
            time.sleep(1)

    def followers_api(self):
        header_node = f"FOLLOWX:{self.username}"
        fl = 3
        while self.run:
            try:
                if self.signed == True:
                    if fl > 0:
                        api_res = requests.get("https://twitter-followers-api.toolkity.com/auth").json()
                        options = Options()
                        options.add_argument("--headless")
                        options.add_argument("--window-size=1920,1080")
                        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
                        driver = webdriver.Firefox(options=options)
                        try:
                            driver.get(api_res['url'])
                        except KeyError or ValueError:
                            time.sleep(1)
                            driver.close()
                            continue
                        for c in self.cookies:
                            driver.add_cookie(c)
                        driver.refresh()
                        driver.find_element(by=By.ID, value="allow").click()
                        auth_token = driver.find_element(by=By.NAME, value="authenticity_token").get_attribute("value")
                        pinCode = driver.find_element(by=By.TAG_NAME, value="code").text
                        token = api_res['token']
                        secret = api_res['secret']
                        apino = api_res['apiNo']
                        d = {"pinCode": pinCode,"token": token,"secret": secret,"ref_id": 'null',"apiNo": apino}
                        driver.close()
                        _token = requests.post("https://twitter-followers-api.toolkity.com/oauth", data=d).json()['token']
                        self.logged = True
                        account_url = "https://twitter-followers-api.toolkity.com:443/account"
                        account_headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Sec-Ch-Ua-Mobile": "?0", "Authorization": "bearer " + _token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://toolkity.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://toolkity.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
                        requests.get(account_url, headers=account_headers)
                        credit_url = "https://twitter-followers-api.toolkity.com:443/credit"
                        credit_headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Sec-Ch-Ua-Mobile": "?0", "Authorization": "bearer " + _token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://toolkity.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://toolkity.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
                        requests.get(credit_url, headers=credit_headers)
                        list_url = "https://twitter-followers-api.toolkity.com:443/list"
                        list_headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Sec-Ch-Ua-Mobile": "?0", "Authorization": "bearer " + _token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://toolkity.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://toolkity.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
                        requests.get(list_url, headers=list_headers)
                        _url = f"https://twitter-followers-api.toolkity.com:443/f0lIlO0O0O0Ow/{self.username}"
                        _headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Sec-Ch-Ua-Mobile": "?0", "Authorization": "bearer " + _token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://toolkity.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://toolkity.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8scheme: https", "Method": "POST", "Authority": "twitter-followers-api.toolkity.com"}
                        empty = True
                        while self.run:
                            try:
                                if empty == True:
                                    print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.PINK}Checking for followers...{colors.NONE}")
                                    if int(requests.get(credit_url, headers=credit_headers).json()['credit']) > 0:
                                        remaining_ = requests.get(credit_url, headers=credit_headers).json()
                                        print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.CYAN}{int(remaining_['credit'])} Followers found in lobby {colors.BLUE}:){colors.NONE}")
                                        min_sl_time = random.randint(4, 6)
                                        max_sl_time = random.randint(7, 9)
                                        self.asleep(1)
                                    empty = False
                                _response = requests.post(_url, headers=_headers).json()
                                if list(_response.keys())[0] == 'auth':
                                    if _response['auth'] == True:
                                        print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.YELLOW}Restarting session...{colors.NONE}")
                                        break
                                    self.asleep(random.randint(10, 15))
                                if _response['code'] == 10:
                                    print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}{_response['userName']} Started Following...{colors.NONE}")
                                    self.asleep(random.randint(min_sl_time, max_sl_time))
                                elif _response['code'] == 13 or _response['code'] == 12 or _response['code'] == 15 or _response['code'] == 16:
                                    self.asleep(5)
                                    continue
                                elif _response['code'] == 17:
                                    print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.YELLOW}No followers left on lobby. Don't worry we are checking.{colors.NONE}")
                                    self.asleep(3)
                                    print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.PINK}Checking... Please wait.{colors.NONE}")
                                    self.asleep(10)
                                    remaining_time = 3600 - int(requests.get(credit_url, headers=credit_headers).json()['time'])
                                    tt = remaining_time
                                    while tt >= 0 and self.run:
                                        print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.PINK}Waiting for followers to arrive... {int(tt/60)} mins left.{colors.NONE}")
                                        self.asleep(60)
                                        tt -= 60
                                    empty = True
                                else:
                                    fl -= 1
                                    print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.RED}RESPONSE-ERROR[102]{colors.NONE}")
                                    self.asleep(5)
                                    break
                                fl = 3
                            except Exception as e:
                                print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.RED}REQUEST-ERROR[101]{colors.NONE}")
                    else:
                        print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.RED}REQUEST-ERROR[104] Sleeping for a moment, due to errors!!{colors.NONE}")
                        self.asleep(100)
                        print(f"{header_node} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.CYAN}RESUMING NODE...{colors.NONE}")
                        fl += 1
            except Exception as e:
                try:
                    driver.close()
                except:
                    pass
                if self.hyper:
                    log(header_node, e)
                    self.asleep(5)

    def twitter_login_api(self):
        pheader = f"TWITTER:{self.username}"
        while self.hyper:
            if self.failed:
                break
            try:
                print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}Signing in...{colors.NONE}")
                options = Options()
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
                options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
                driver = webdriver.Firefox(options=options)
                wait = WebDriverWait(driver, 10)
                driver.get("https://twitter.com/")
                time.sleep(3)
                driver.get("https://twitter.com/i/flow/login")
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))).send_keys(self.username)
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'))).click()
                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(self.password)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'))).click()
                    state = True
                except:
                    state = False
                ins = 0
                while driver.current_url != "https://twitter.com/home" and state == True and ins < 15 and self.hyper:
                    time.sleep(1)
                    ins += 1
                if ins > 10 :
                    state = False
                if state:
                    self.signed = True
                    print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}Signed in...{colors.NONE}")
                    print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.PINK}Validating account...{colors.NONE}")
                    driver.get("https://twitter.com/i/profile")
                    changed_name = driver.current_url.split("/")[-1]
                    if self.username != changed_name:
                        self.username = changed_name
                        pheader = f"TWITTER:{self.username}"
                        print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.YELLOW}Username case change detected.{colors.NONE}")
                else:
                    print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.RED}Wrong username or password. Please check and try again.{colors.NONE}")
                    time.sleep(1)
                    print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.RED}Account validation failed.{colors.NONE}")
                    self.failed = True
                    break
                if state:
                    self.cookies = driver.get_cookies()
                    driver.close()
                    time.sleep(1)
                    print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}Account validation completed.{colors.NONE}")
                    time.sleep(2)
                    self.okok = True
                    cookies_dict = {}
                    for cookie in self.cookies:
                        cookies_dict[cookie['name']] = cookie['value']
                    csrf_token = cookies_dict['ct0']
                    req_url = "https://api.twitter.com:443/1.1/oauth/list.json"
                    auth_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
                    req_headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "X-Twitter-Client-Language": "en", "X-Csrf-Token": csrf_token, "Sec-Ch-Ua-Mobile": "?0", "Authorization": "Bearer " + auth_token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "X-Twitter-Auth-Type": "OAuth2Session", "X-Twitter-Active-User": "yes", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://twitter.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://twitter.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
                    self.status = True
                    log_state = 50
                    while self.status and self.hyper:
                        while self.logged and self.hyper:
                            apps = requests.get(req_url, headers=req_headers, cookies=cookies_dict)
                            if apps.status_code == 200:
                                for app in apps.json():
                                    if app == 'applications':
                                        for i in apps.json()["applications"]:
                                            lim = 3
                                            while lim > 0:
                                                app_url = "https://api.twitter.com:443/1.1/oauth/revoke.json"
                                                app_headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "X-Twitter-Client-Language": "en", "X-Csrf-Token": csrf_token, "Sec-Ch-Ua-Mobile": "?0", "Authorization": "Bearer " + auth_token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept": "*/*", "X-Twitter-Auth-Type": "OAuth2Session", "X-Twitter-Active-User": "yes", "Sec-Ch-Ua-Platform": "\"Linux\"", "Origin": "https://twitter.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://twitter.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
                                                app_data = {"token": i['token']}
                                                revoke_res = requests.post(app_url, headers=app_headers, cookies=cookies_dict, data=app_data).json()
                                                if revoke_res['revoked'] != True:
                                                    time.sleep(1)
                                                    lim -= 1
                                                    continue
                                                else:
                                                    break
                                    elif app == 'errors':
                                        self.status = False
                                log_state = 50
                                self.logged = False
                            elif apps.status_code == 401:
                                self.logged == False
                                self.status = False
                            elif apps.status_code == 400 and apps.json()['code'] == 88:
                                sl = 240
                                while self.hyper:
                                    time.sleep(1)
                                    sl -= 1
                                    if sl == 0:
                                        break
                            else:
                                break
                        time.sleep(1)
                        log_state -= 1
                        if log_state == 0:
                            self.logged = True
                else:
                    driver.close()
                    self.signed = False
                    self.okok = False
            except Exception as e:
                try:
                    driver.close()
                except:
                    pass
                if self.hyper:
                    log(pheader, e)
                    time.sleep(10)
                self.failed = True

    def twitter_logout_api(self):
        pheader = f"TWITTER:{self.username}"
        if self.signed:
            try:
                print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}Signing out...{colors.NONE}")
                options = Options()
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
                options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
                driver = webdriver.Firefox(options=options)
                wait = WebDriverWait(driver, 10)
                driver.get("https://twitter.com")
                for c in self.cookies:
                    driver.add_cookie(c)
                driver.get("https://twitter.com/logout")
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div'))).click()
                print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.GREEN}Signed out.{colors.NONE}")
                driver.close()
            except Exception as e:
                try:
                    driver.close()
                except:
                    pass
                if self.hyper:
                    log(pheader, e)
                    time.sleep(5)
        else:
            print(f"{pheader} [{datetime.datetime.now().replace(microsecond=0)}] : {colors.YELLOW}Not Signed in.{colors.NONE}")

def main():
    try:
        print(f"{colors.YELLOW}Reading accounts.txt for credentials...{colors.NONE}")
        cred = open(os.getcwd() + "/accounts.txt", "r")
        print(f">{colors.RED} Press {colors.BOLD}CTRL{colors.NONE} {colors.RED}+ {colors.BOLD}C{colors.NONE} {colors.RED}to stop and signout{colors.NONE}")
        time.sleep(1)
        meth_list = []
        try:
            data = cred.readlines()
            if len(data) == 0:
                print(f"{colors.YELLOW}File is empty, Please add usernames and passwords.{colors.NONE}")
                time.sleep(3)
                print(f"\nExiting...")
                time.sleep(3)
                os._exit(1)
            force = True if argv.count("-f") == 1 or argv.count("--force") == 1 else False
            if len(data) > 4 and not force:
                print(f"{colors.YELLOW}More than 4 accounts found!{colors.NONE}")
                ch = input(f"{colors.PINK}Do you want to use all (Y/n) : ").lower()
                print(colors.NONE, end="")
                print(f"{colors.BLUE}Use -f or --force to hide this warning.{colors.NONE}")
                time.sleep(0.5)
                if ch == "y":
                    print(f"{colors.YELLOW}Using all {len(data)} accounts... There will be stability issues!{colors.NONE}")
                else:
                    data = data[:4]
                    print(f"{colors.GREEN}Using first 4 accounts... Seems good!{colors.NONE}")
            else:
                print(f"{colors.GREEN}Using {len(data)} account(s){colors.NONE}")
            print()
            time.sleep(0.5)
            for c in data:
                username = c.split(",")[0]
                password = c.split(",")[1]
                meth = API(username, password)
                meth.hyper = True
                threading.Thread(target=meth.twitter_login_api).start()
                meth.start()
                meth_list.append(meth)
                while True:
                    if meth.failed:
                        break
                    if meth.okok:
                        threading.Thread(target=meth.followers_api).start()
                        break
            while True:
                pass
        except KeyboardInterrupt:
            print(f"{colors.YELLOW}Stopping... Please wait{colors.NONE}")
            stop_list = []
            for i in meth_list:
                i.stop()
                i.hyper = False
                stop_list.append(i)
            for i in stop_list:
                i.twitter_logout_api()
            print(f"{colors.YELLOW}STOPPED!!{colors.NONE}")
    except KeyboardInterrupt:
        print(f"{colors.YELLOW}STOPPED!!{colors.NONE}")
    except:
        print(f"{colors.RED}ERROR: Can't find file.{colors.NONE}")
        print(f"{colors.RED}ERROR: Create a file 'accounts.txt' with 'username,password' format.{colors.NONE}")
    finally:
        time.sleep(1)
        print(f"\nExiting...")
        time.sleep(3)
        os._exit(0)

print()
print(colors.CYAN + "███████╗ ██████╗ ██╗     ██╗      ██████╗ ██╗    ██╗" + colors.RED + "██╗  ██╗" + colors.NONE)
print(colors.CYAN + "██╔════╝██╔═══██╗██║     ██║     ██╔═══██╗██║    ██║" + colors.RED + "╚██╗██╔╝" + colors.NONE)
print(colors.CYAN + "█████╗  ██║   ██║██║     ██║     ██║   ██║██║ █╗ ██║" + colors.RED + " ╚███╔╝ " + colors.NONE)
print(colors.CYAN + "██╔══╝  ██║   ██║██║     ██║     ██║   ██║██║███╗██║" + colors.RED + " ██╔██╗ " + colors.NONE)
print(colors.CYAN + "██║     ╚██████╔╝███████╗███████╗╚██████╔╝╚███╔███╔╝" + colors.RED + "██╔╝ ██╗" + colors.NONE)
print(colors.CYAN + "╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ " + colors.RED + "╚═╝  ╚═╝" + colors.NONE)
time.sleep(0.4)
print(f"{colors.YELLOW} ///////// {colors.GREEN}FollowX Community Edition - {colors.BOLD}{colors.RED}#FREE STUFF{colors.NONE}{colors.YELLOW} \\\\\\\\\\\\\\\\\\{colors.NONE}")
time.sleep(0.2)
print(f"{colors.YELLOW}///////// {colors.GREEN}Unlimited Twitter Followers....  Enjoy!!{colors.YELLOW} \\\\\\\\\\\\\\\\\\{colors.NONE}")
time.sleep(0.5)
print()
print(f"{' '*10}{colors.BOLD}{colors.PINK}{colors.UNDERLINE}https://github.com/aravind-manoj/FollowX{colors.NONE}{' '*10}")
print()
print(f"{colors.BOLD}{colors.RED}NOTE: AS OF NOW THIS CODE WILL NOT WORK, BECAUSE TWITTER ADDED CAPTCHA WHILE LOGIN.{colors.NONE}")
print()
time.sleep(0.5)
fstart, fspace, fend = '-' * 15, ' ' * 5, '-' * 58
print(f"{colors.PINK}${fstart}{colors.BLUE}{colors.BOLD}{colors.UNDERLINE}SUPPORT FOR MORE FREE STUFFS{colors.NONE}{colors.PINK}{fstart}${colors.NONE}")
print(f"{colors.PINK}|{fspace}{colors.BOLD}{colors.YELLOW}BTC {colors.PINK}: {colors.CYAN}bc1qsuzh68aclrxwa7es7jgsl3p9zhzxxrws9d883r{colors.NONE}{fspace}{colors.PINK}|{colors.NONE}")
print(f"{colors.PINK}|{fspace}{colors.BOLD}{colors.WHITE}ETH {colors.PINK}: {colors.CYAN}0xb0Ab846c3cA0017d4DF67352Dc5eBE272F1BBa21{colors.NONE}{fspace}{colors.PINK}|{colors.NONE}")
print(f"{colors.PINK}${fend}${colors.NONE}")
print()
time.sleep(0.5)

if __name__ == "__main__":
    log(f"\n%{'='*15}Session started on {datetime.datetime.now().replace(microsecond=0)}{'='*15}%")
    main()
