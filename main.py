import os,time,sys.shutil

class Main:

      def __init__(self):
              self.detekos()

      def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;    ███╗   ██╗████████╗████████╗████████╗  ;
        ;    ████╗  ██║╚══██╔══╝╚══██╔══╝╚══██╔══╝  ;
        ;    ██╔██╗ ██║   ██║      ██║      ██║     ;
        ;    ██║╚██╗██║   ██║      ██║      ██║     ;
        ;    ██║ ╚████║   ██║      ██║      ██║     ;
        ;    ╚═╝  ╚═══╝   ╚═╝      ╚═╝      ╚═╝     ;                  
		;--------------------------------------------
		;             TOOL BY KAR13MA09             ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    NOTE: Công cụ này chỉ dùng được cho số điện thoại Việt Nam hoặc Indonesia 

1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
6. OTP momo.vn
7. OTP f88.vn		
8. OTP vietteltelecom.vn	
""")
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))    