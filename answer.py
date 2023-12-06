arr = "abcdefghijklmnopqrstuvwxyz0123456789_"
pico = ""
text = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]
for i in range(0,len(text)):
    try:
        #print(str(arr[int(text[i]) % 37]),end="")
        pico = pico + arr[text[i] % 37]
    except IndexError:
        print("Index out of range")
    
    
print(pico)
