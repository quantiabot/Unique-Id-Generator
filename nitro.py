import requests,random,string,time
def generate(length=16):
    characters=string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
while True:
        code=generate(16)
        base=f"https://discord.com/api/v9/entitlements/gift-codes/{code}"
        try:
            result=requests.get(base,timeout=5)
            if result.status_code==404:
                print(f"{code} Invalid")
            elif result.status_code==429:
                print(f"{code} Timeout")
                time.sleep(5)       
            elif result.status_code==200:
                print(f"discord.gg/gift/{code}")
                break
        except:
              print("")
