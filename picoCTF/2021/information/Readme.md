# [information]()
<div style="background-image: linear-gradient(to bottom left,#fd5d93,#ec250d,#fd5d93);margin-right:75%; padding-left:2%;border-radius: .4285rem; color:white">Category: Forensics</div>

#### AUTHOR: SUSIE

### Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)



##### Code

```shell
picoCTF{the_m3tadata_1s_modified}

```
##### output
```

┌──(callummason㉿MARVIN)-[/mnt/…/CTF/picoCTF/2021/information]
└─$ exiftool cat.jpg                       
ExifTool Version Number         : 12.16
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 18:24:46+00:00
File Access Date/Time           : 2021:04:21 22:10:47+01:00
File Inode Change Date/Time     : 2021:04:21 22:06:30+01:00
File Permissions                : rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1


```

We are looking at the License part, this is a base64 so we will need to decode it using cyber chef again

![Cyber chef Base64](https://raw.githubusercontent.com/Callum-Mason/CTF/master/picoCTF/2021/information/assets/cyber%20chef%20base64.png "Cyber chef Base64")



### Flags


#### ***** picoCTF{the_m3tadata_1s_modified} ****