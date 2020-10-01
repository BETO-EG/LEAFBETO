import sys
import requests
import os
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import time as timer
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

Done = 0
Failed = 0

logo = '''
.______    _______ .___________.  ______        ______ .______  
|   _  \  |   ____||           | /  __  \      /      ||   _  \ 
|  |_)  | |  |__   `---|  |----`|  |  |  |    |  ,----'|  |_)  |
|   _  <  |   __|      |  |     |  |  |  |    |  |     |   ___/ 
|  |_)  | |  |____     |  |     |  `--'  |    |  `----.|  |     
|______/  |_______|    |__|      \______/      \______|| _|     
                                                                

'''

print logo
LFBETO = raw_input(' [+] CPANEL PATH [+]   ')
BETOTHRE = int(raw_input(' [+] ThreadPool NUM [+]   '))

def LFCHEK(leafBETO):
	global Done, Failed
	try :
			
			req = requests.session()
			try :
				login = req.get(leafBETO,timeout=15)
			except:
				login = req.get(leafBETO,verify=False, timeout=15)
			if '[-randomstring-] : ' and 'Leaf PHPMailer' in login.content :
				print ' {}[+] WORKING-leafmailer'.format(fg)
				Done += 1
				os.system("title " + "[+] Leaf PHPMailer CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
				print '{}'.format(leafBETO)
				open('WORKING-leafmailer.txt', 'a').write('{}\n'.format(leafBETO))
			else:
				print ' {} {} [-] Login failed'.format(fr, leafBETO)
				Failed += 1
				os.system("title " + "[+] Leaf PHPMailer CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
	except:
		print ' {} {} [-] Login failed'.format(fr, leafBETO)
		Failed += 1
		os.system("title " + "[+] Leaf PHPMailer CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
if __name__ == "__main__":
	LFBETO = open(LFBETO, 'r').read().split('\n')
	pool = ThreadPool(BETOTHRE)
	for _ in pool.imap_unordered(LFCHEK, LFBETO):
		pass
		