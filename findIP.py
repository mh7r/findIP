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
            ["City:", data["city"]],
            ["Country:", data["country"]],
            ["Region:", data["region"]]]
    print(colored(tabulate(table), "blue"))
except:
    print(colored("---------------------------", "cyan"))
    print(colored("Check your network", "red"))
    print(colored("---------------------------", "cyan"))   
