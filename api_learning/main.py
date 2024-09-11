import requests

responde = requests.get("https://www.youtube.com/watch?v=hpc5jyVpUpw")

print(responde.text)