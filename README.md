[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![badge](https://img.shields.io/badge/For-CTF%20players-red.svg)](https://shields.io/)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
<br>
All shells accept a GET parameter, cmd, to execute commands. 
<br>
<h2>What is upload.py?</h2>
upload.py - script to automatically upload a webshell. i like automation eh. look at the code, you will understand from the comments what to do. if you feel like uploading another file, just type "upload it [path ot the file]" and this will upload that other file. You can use it to upload any file basically.
<br>
<h2>What is gifwebshell.php?</h2>
<br>
gifwebshell.php - GIF webshell type 1, where the server only checks whether or not the magic GIF [GIF89a] bytes are present in the file. here i took a random gif, added php code inside it and added __halt_compiler() to make things simpler in the end. This repo is to just make my life easier kek. It's for those CTFs/Pentests where you are checking if you can upload a php file with GIF magic bytes and get it executed.
