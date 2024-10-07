def toggle_string(s: str) -> str:
    return_s = ''
    for c in s:
        return_s += chr(ord(c)^0x20)
    #next c
    return return_s
#end function

print(toggle_string('SomeFunnyCHarters'))

