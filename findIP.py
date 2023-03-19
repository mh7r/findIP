import json
from urllib.request import urlopen
from tabulate import tabulate
from termcolor import colored
try:
    url = "https://ipinfo.io/json"
    response = urlopen(url)
    data = json.load((response))
    table = [["IP:", data["ip"]],
            ["Server:", data["org"]],
            ["Sehir:", data["city"]],
            ["Ulke:", data["country"]],
            ["Bolge:", data["region"]]]
    print(colored(tabulate(table), "blue"))
except:
    print(colored("---------------------------", "cyan"))
    print(colored("Baglantinizi kontrol ediniz", "red"))
    print(colored("---------------------------", "cyan"))   
