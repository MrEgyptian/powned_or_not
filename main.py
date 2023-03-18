#!/bin/env python3
# Ver: 0.1
# By : @MrEgyptian
# GitHub :Github.com/MrEgyptian
# Website : https://www.MrEgyptian.codes
# Contact : Me@MrEgyptian.com
import requests,json
import cloudscraper

def search(q):
 q=requests.utils.quote(q)
 scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 
 r = scraper.get(f"https://haveibeenpwned.com/unifiedsearch/{q}")
 if(r.content!=b''):
  return r.json()
 else:
  return 'NOTPOWNED'
def save_json(file_name,content):
 f=open(file_name,'w')
 f.write(json.dumps(content,indent=4))
 f.close()
if __name__=='__main__':
 R = '\033[31m' # red
 G = '\033[32m' # green
 C = '\033[36m' # cyan
 W = '\033[0m'  # white
 Y = '\033[33m' # yellow
 print('''
 _______________
< Powned or not >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||

 ''')
 q=input(f'{G}[+]' + C + ' Enter Phone/Email to start : ' + W)
 res=search(q)
 #print(res)
 if(type(res)==dict):
  breaches=res['Breaches']
  print(f"Found {len(breaches)}:")
  for item in breaches:
   print(f'\n' \
   f'{G}[+] {C}Breach      : {W}{str(item["Title"])} \n' \
   f'{G}[+] {C}Domain      : {W}{str(item["Domain"])} \n' \
   f'{G}[+] {C}Date        : {W}{str(item["BreachDate"])} \n' \
   f'{G}[+] {C}BreachedInfo: {W}{str(item["DataClasses"])} \n' \
   f'{G}[+] {C}Fabricated  : {W}{str(item["IsFabricated"])} \n' \
   f'{G}[+] {C}Verified    : {W}{str(item["IsVerified"])} \n' \
   f'{G}[+] {C}Retired     : {W}{str(item["IsRetired"])} \n' \
   f'{G}[+] {C}Spam        : {W}{str(item["IsSpamList"])}'
   )
   print('_'*50)
  save=input(f'{G}[+]' + C + 'Wanna save results to JSON file [Yn]' + W)
  if(save.lower!='n'):
   save_json(q+'.json',res)
   print(f'{G}[+]' + C + 'Data saved into '+Y +q+'.json'+ W)
 else:
  print(f'{G} Not Powned ...')
 # print()
 print(f'{G} GoodBye ...')
