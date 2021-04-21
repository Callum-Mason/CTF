# [Title]()
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category: General Skills</div>

#### AUTHOR: SYREAL

### Description

There is a nice program that you can talk to by using this command in a shell: `` $ nc mercury.picoctf.net 21135``, but it doesn't speak English...

### Method 

When you run that command, it will give you a list of random numbers.

```

112 
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
97
102
100
53
102
100
97
52
125
10
```

But if we put that output into cyberchef, and put an a 'From Decimal' operation on it and say that the Life feed is the delimiter, it will give us our flag

![Cyber chef netcat](https://raw.githubusercontent.com/Callum-Mason/CTF/master/picoCTF/2021/Nice%20netcat/assets/cyberchefnetcat.png "Cyber chef netcat")



### Flags


#### ***** picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4} ****