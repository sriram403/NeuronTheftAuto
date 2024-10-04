import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

# Add left shift as a separate key
left_shift_key = 0xA0  # Virtual key code for left shift

def key_check():
    keys = []
    for key in keyList:
        # Handle left shift separately
        if key == " " and wapi.GetKeyState(left_shift_key) < 0:
            keys.append("Lshift")
        # For other keys, use GetAsyncKeyState
        elif wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys