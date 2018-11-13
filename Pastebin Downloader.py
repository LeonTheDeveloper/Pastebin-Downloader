import requests

print("Welcome to Pastebin downloader! Made by Azure#0263 / Lee Everrett")
print("No more copy and pasting into a text file manually!")
print("To start, please enter the url to a pastebin (raw)")
print("")
pastebin_url = input("Url: ")
filename = input("Name of text file (e.g Downloaded pastebin): ")

r = requests.get(pastebin_url)
f = open(f'{filename}.txt', 'a+')
f.write(r.text)
print(f"Text file {filename}.txt has been made!")
