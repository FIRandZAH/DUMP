import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
tokene = []
id = []
ses = requests.Session()
h = '\x1b[1;92m'  # Hijau
xxx = '\33[m'
def cokzar():
    try:
        os.system('clear')
        banlog()
        cok = {'cookie': input('ENTER COOKIE : ')}
        link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
        gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
        get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
        tok = re.search('accessToken="(.*?)"',str(get)).group(1)
        open(".tokzar.txt", "w").write(tok)
        open(".cokzar.txt", "w").write(cok['cookie'])
        print('\nToken : {}'.format(tok))
        exit()
    except(Exception) as e:
        print('Cookies Mokad') ; time.sleep(3)
        print(e)
        log_zar()
def log_zar():
    try:
        token = open('.tokzar.txt','r').read()
        cok = open('.cokzar.txt','r').read()
        tokene.append(token)
        try:
            gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokene[0], cookies={'cookie':cok})
            nteng = json.loads(gerap.text)['id']
            zara(nteng)
        except KeyError:
            cokzar()
        except requests.exceptions.ConnectionError:
            exit()
    except IOError:
        cokzar()
def zahra_animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.05)
def zahra_animasi2(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
def zahra_animasi3(berjalan):
    for gas in str(berjalan) + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.01)
def banzar():
    zahra_animasi3(f'''\x1b[1;91m
888888ba                                
88    `8b                               
88     88 dP    dP 88d8b.d8b.  88d888b. 
88     88 88    88 88'`88'`88  88'  `88 
88    .8P 88.  .88 88  88  88  88.  .88 
8888888P  `88888P' dP  dP  dP  88Y888P' 
\x1b[0;34moooooooooooooooooooooooooooooo~\x1b[1;91m88\x1b[0;34m~oooooo
                     \x1b[1;91m          dP       
                               ''')

def banlog():
    print('''\x1b[1;92m
         _____   ______ _____ __   _     
 |      |     | |  ____   |   | \  |     
\33[m |_____ |_____| |_____| __|__ |  \_| 
''')

def zara(id):
    try:
        cok = open('.cokzar.txt','r').read()
    except IOError:
        cokzar()
    os.system('clear')
    banzar()
    print(f'{xxx} 1. crack')
    print(f'{xxx} 2. lapor bug ({h}WhatsApp{xxx})')
    zahra = input(f'\n input: ')
    if zahra == '1':
        asi()
    elif zahra == '2':
        os.system("xdg-open https://wa.me/+6289673673476?text=halo+kak")
        log_zar()
    else:
        log_zar()
def asi():
    try:
        print(f'')
        print(f'{xxx} 1. DUMP ID{h} 61.10009.10008')
        print(f'{xxx} 2. DUMP SEMUA ID{xxx}')
        zahraa = input(f'{xxx}>> : ')
        if zahraa == '1':
            print(f'{xxx}')
            uid = input('  ENTER ID: ').split(',')
            for x in uid:
                nge_krek(x, '')
        elif zahraa == '2':
            print(f'{xxx}')
        uid = input('  ENTER ID: ').split(',')
        for x in uid:
            nge_krek1(x , '')
        else:
            asi()
    except Exception as e:
        print(f'Error: {e}')
        

def nge_krek(uidz, after):
    try:
        tok = open('.tokzar.txt', 'r').read()
        cok = {'cookie': open('.cokzar.txt', 'r').read()}
    except IOError:
        exit()
    
    try:
        if len(id) == 0:
            params = {
                'access_token': tok,
                'fields': 'friends'
            }
        else:
            params = {
                'access_token': tok,
                'fields': 'friends.after({})'.format(after)
            }
        
        po = ses.get('https://graph.facebook.com/{}'.format(uidz), params=params, cookies=cok).json()
        
        for x in po['friends']['data']:
            id_prefix = x.get('id')[:2]
            id_prefix5 = x.get('id')[:5]
            if id_prefix == '61' or id_prefix5 in ('10009', '10008'):
                id.append(x.get('id') + '|' + x.get('name'))
                print("  TOTAL ID: " + str(len(id)), end='\r')
        
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz, afr)
    except KeyError:
        pass
    
    simpan()

def nge_krek1(uidz , after):
    try:
        tok = open('.tokzar.txt','r').read()
        cok = {'cookie':open('.cokzar.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print("  TOTAL ID : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz , afr)
    except(KeyError) as e:
        pass
    simpan()
def simpan():
    while True:
        zahra_animasi(f'\n{xxx}   ({h}Mau disimpan di repositori mana?{xxx})')
        zahra_animasi(f'{xxx}   ({h}CONTOH: {xxx}/storage/emulated/0/Download/{xxx})')
        zahra_animasi(f'{xxx}   ({h}atau Ketik "{xxx}y{h}" untuk simpan otomatis{xxx})')
        zahra_animasi(f'{xxx}   ({h}DI: {xxx}/storage/emulated/0/ZAHRA-DUMP/{xxx})')
        repo_dir = input(' Input: ')
        
        if repo_dir.lower() == 'y':
            repo_dir = '/storage/emulated/0/ZAHRA-DUMP/'
            if not os.path.isdir(repo_dir):
                os.mkdir(repo_dir)
            break
        elif not os.path.isdir(repo_dir):
            print('Direktori repositori tidak valid. Silakan coba lagi.')
        else:
            break

    zahra_animasi(f'\n{xxx}   ({h}Nama file contoh sayang.txt{xxx})')
    file_name = input(' Input: ')

    file_path = os.path.join(repo_dir, file_name)

    with open(file_path, 'w') as file:
        for uid in id:
            file.write(uid + '\n')

    zahra_animasi(f' disimpan di repositori {h}{file_path}')
    exit()
    
if __name__=="__main__":
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
        os.system('git pull')
        zahra_animasi2(f'\n{xxx}   ({h}SEMOGA{xxx} FIRMAN{h} DAN SEKELUARGA SEHAT SELALU AMIN{xxx})')
        zahra_animasi2(f'{xxx}   ({h}DAN BANYAK REZEKINYA AMINN{xxx})')
        waktu(3)
        log_zar() 
	