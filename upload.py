import requests

url=""

#headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary5tBS5SLzak42PAxi'}

with open('testone.php','rb') as f:
    files={'file':f} #check the params first
    r=requests.post(url, files=files)

print(r.text)
