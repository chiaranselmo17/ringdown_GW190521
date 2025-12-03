import urllib.request
import json

repo = "chiaranselmo17/ringdown_GW190521"
api_url = f"https://api.github.com/repos/{repo}/releases/latest"

with urllib.request.urlopen(api_url) as f:
    content = json.loads(f.read().decode())

for asset in content['assets']:
    urlfile = asset['browser_download_url']
    filename = urlfile.split('/')[-1]

    if filename.endswith(".npy"):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(urlfile, filename)

print("All .npy files downloaded successfully.")
