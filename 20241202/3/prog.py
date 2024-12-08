from sys import stdin

s = b''.join(stdin.buffer.readlines())

if len(s) >= 44 and s[0:4] == b"RIFF" and s[8:12] == b"WAVE" and s[36:40] == b"data":
    print(
        f"Size={int.from_bytes(s[4:8], 'little')}, "
        f"Type={int.from_bytes(s[20:22], 'little')}, "
        f"Channels={int.from_bytes(s[22:24], 'little')}, "
        f"Rate={int.from_bytes(s[24:28], 'little')}, "
        f"Bits={int.from_bytes(s[34:36], 'little')}, "
        f"Data size={int.from_bytes(s[40:44], 'little')}"
    )
else:
    print("NO")
