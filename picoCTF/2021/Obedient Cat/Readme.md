# [Obedient Cat](https://play.picoctf.org/practice/challenge/147?originalEvent=34&page=1)
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category: General Skills</div>

#### AUTHOR: SYREAL

### Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag).


##### Code

```shell
wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag

cat flag
```
##### output
```

┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/Obedient Cat]
└─$ wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
--2021-04-21 21:33:17--  https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142, 205.251.196.165, 205.251.199.165, ...
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: ‘flag’

flag
100%[=====================================================================>]      34  --.-KB/s    in 0s       

2021-04-21 21:33:18 (14.7 MB/s) - ‘flag’ saved [34/34]


┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/Obedient Cat]
└─$ cat flag
picoCTF{s4n1ty_v3r1f13d_2fd6ed29}

```



### Flags


#### ***** picoCTF{s4n1ty_v3r1f13d_2fd6ed29} ****