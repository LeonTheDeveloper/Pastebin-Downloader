import requests

print("Welcome to Pastebin downloader! Made by Azure#0263 / Lee Everrett")
print("No more copy and pasting into a text file manually!")
print("To start, please enter the url to a pastebin or the id. \n")

pastebin_raw_url = input("URL / ID: ")
filename = input("Name of text file (e.g Downloaded pastebin): ")
pastebin_id = pastebin_raw_url.split("/")[-1]

if len(pastebin_raw_url.split("/")) == 1:
  pastebin_raw_url = 'https://pastebin.com/raw/{}'.format(pastebin_id)
elif pastebin_raw_url.split("/")[-2] != "raw":
  pastebin_raw_url = 'https://pastebin.com/raw/{}'.format(pastebin_id)

r = requests.get(pastebin_raw_url)
f = open(f'{filename}.txt', 'a+')
f.write(r.text)
print(f"Text file {filename}.txt has been made!")