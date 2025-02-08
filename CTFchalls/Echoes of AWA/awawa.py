flag = "?????????????????????"

awa_map = {
    '0': 'awa',
    '1': 'awawawa',
    '2': 'awawa',
    '3': 'wawawa',
}

def encrypt_with_msg2(flag, shift_value):
    shifted_flag = ''.join(chr((ord(char) + shift_value) % 128) for char in flag)

    encrypted = ""
    for char in shifted_flag:
        binary_char = format(ord(char), '08b')
        reversed_binary = binary_char[::-1]
        awa_encoded = ''.join(awa_map.get(bit, '') for bit in reversed_binary)
        encrypted += awa_encoded + " "
    
    encrypted_message = encrypted.strip()

    msg2 = "????????????????????????????????"
    
    msg2_encoded = msg2.encode('utf-8').hex()
    return f"{encrypted_message} {msg2_encoded}"

def extract_msg_msg2(encrypted_message_with_msg2):
    parts = encrypted_message_with_msg2.rsplit(' ', 1)
    encrypted_message = parts[0]
    msg2_encoded = parts[1]
    msg2 = bytes.fromhex(msg2_encoded).decode('utf-8')
    return encrypted_message, msg2

shift_value = "?????????????????????????????"

encrypted_flag_with_msg2 = encrypt_with_msg2(flag, shift_value)
print("Encoded flag", encrypted_flag_with_msg2)