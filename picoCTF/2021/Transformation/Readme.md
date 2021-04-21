# [Transformation](https://play.picoctf.org/practice/challenge/104?originalEvent=34&page=1)
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category: Reverse Engineering</div>

#### AUTHOR: MADSTACKS

### Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) ``''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])``

### Method

We can see that the enc file was decoded using that python line in the description so we will need to create a decoder using the reverse if what was used to encode the flag. Once it has been decoded it will then output the glag. 


##### Code

```python

encoded_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
for i in range(len(encoded_flag)):
    print(chr(ord(encoded_flag[i]) >> 8), end='')
    print(chr((ord(encoded_flag[i])) -
              ((ord(encoded_flag[i]) >> 8) << 8)), end='')

```

### Flags


#### ***** picoCTF{16_bits_inst34d_of_8_d52c6b93} ****