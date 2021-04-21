# [Python Wrangling](https://play.picoctf.org/practice/challenge/166?originalEvent=34&page=1)
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category:  General Skills</div>

#### AUTHOR: SYREAL

### Description

Python scripts are invoked kind of like programs in the Terminal... Can you run this [Python](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py) script using [this password](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/pw.txt) to get [the flag](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/flag.txt.en)?


##### Code

```shell
python3 ./ende.py -d ./flag.txt.en

```
##### output
```

┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/Python Wrangling]
└─$ python3 ende.py -d flag.txt.en                            130 ⨯ 
Please enter the password:ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}

```



### Flags


#### ***** picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff} ****