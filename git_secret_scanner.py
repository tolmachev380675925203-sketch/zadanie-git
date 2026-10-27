import subprocess
import re
import math
def entropia(s):
    if not s:
        return 0
    e=0
    for x in set(s):
        p=s.count(x) / len(s)
        e-=p* math.log2(p)
    return e
def skanuj():
    p=subprocess.run("git log -p", capture_output=True, text=True, shell=True)
    dane=p.stdout
    reguly=[
        r"password\s*=\s*['\"].*?['\"]",
        r"api_key\s*=\s*['\"].*?['\"]",
        r"token\s*=\s*['\"].*?['\"]",
        r"secret\s*=\s*['\"].*?['\"]"
    ]
    print("start skanowania...")
    for reg in reguly:
        wyniki=re.findall(reg,dane,re.IGNORECASE)
        for w in wyniki:
            print("znaleziono haslo:",w)
    slowa=dane.split()
    for slowo in slowa:
        if len(slowo) >12 and entropia(slowo)>4.2:
            print("podejrzany ciag (wysoka entropia):",slowo)
skanuj()