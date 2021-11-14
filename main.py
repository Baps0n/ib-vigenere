def encode_by_key(msg, key):
    res = ''
    key_i = 0
    for i in range(len(msg)):
        if msg[i] == '_':
            res += msg[i]
        else:
            msg_chr_num = ord(msg[i]) - 97
            key_chr_num = ord(key[key_i % len(key)]) - 97
            res_chr_num = (msg_chr_num + key_chr_num) % 26
            res += chr(res_chr_num + 97)
            key_i += 1
    return res


def decode_by_key(enc_msg, key):
    dec_msg = ''
    key_i = 0
    for i in range(len(enc_msg)):
        if enc_msg[i] == '_':
            dec_msg += enc_msg[i]
        else:
            msg_chr_num = ord(enc_msg[i]) - 97
            key_chr_num = ord(key[key_i % len(key)]) - 97
            dec_msg_chr_num = (msg_chr_num - key_chr_num) % 26
            dec_msg += chr(dec_msg_chr_num + 97)
            key_i += 1
    return dec_msg


def encode_by_msg(msg, k):
    enc_msg = ''
    key_i = 0
    key = k + msg.replace('_', '')[:-1]
    for i in range(len(msg)):
        if msg[i] == '_':
            enc_msg += '_'
        else:
            msg_chr_num = ord(msg[i]) - 97
            key_chr_num = ord(key[key_i]) - 97
            enc_msg_chr_num = (msg_chr_num + key_chr_num) % 26
            enc_msg += chr(enc_msg_chr_num + 97)
            key_i += 1
    return enc_msg


def decode_by_msg(enc_msg, k):
    dec_msg = ''
    for i in range(len(enc_msg)):
        if enc_msg[i] == '_':
            dec_msg += '_'
        else:
            enc_msg_chr_num = ord(enc_msg[i]) - 97
            key_chr_num = ord(k) - 97
            dec_msg_chr_num = (enc_msg_chr_num - key_chr_num) % 26
            dec_msg += chr(dec_msg_chr_num + 97)
            k = dec_msg[-1]
    return dec_msg


def encode_by_enc_msg(msg, k):
    enc_msg = ''
    for i in range(len(msg)):
        if msg[i] == '_':
            enc_msg += '_'
        else:
            msg_chr_num = ord(msg[i]) - 97
            key_chr_num = ord(k) - 97
            enc_msg_chr_num = (msg_chr_num + key_chr_num) % 26
            enc_msg += chr(enc_msg_chr_num + 97)
            k = enc_msg[-1]
    return enc_msg


def decode_by_enc_msg(enc_msg, k):
    dec_msg = ''
    key_i = 0
    key = k + enc_msg.replace('_', '')[:-1]
    for i in range(len(enc_msg)):
        if enc_msg[i] == '_':
            dec_msg += enc_msg[i]
        else:
            msg_chr_num = ord(enc_msg[i]) - 97
            key_chr_num = ord(key[key_i % len(key)]) - 97
            dec_msg_chr_num = (msg_chr_num - key_chr_num) % 26
            dec_msg += chr(dec_msg_chr_num + 97)
            key_i += 1
    return dec_msg


def text_edit(text):
    text = text.lower()
    text = text.replace(" ", "_")
    for i in ['.', ',', '!', '?', '«', '»', '—', '-', ':', ';', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9']:
        text = text.replace(i, '')
    return text


def main():
    print("Выберите способ выработки гаммы, введя его номер:\n"
          "1. Повторение короткого лозунга\n"
          "2. Самоключ Виженера по открытому тексту\n"
          "3. самоключ Виженера по шифртексту")

    gamma_type = input()
    while '1' not in gamma_type and '2' not in gamma_type and '3' not in gamma_type:
        print("Ввод некорректен. Введите номер способа")
        gamma_type = input()
    print("Выберите тип операции, введя её номер:\n"
          "1. Шифрование\n"
          "2. Расшифрование")

    operation = input()
    while '1' not in operation and '2' not in operation:
        print("Ввод некорректен. Введите номер типа операции")
        operation = input()
    if '1' in operation:
        print("Введите открытый текст")
    if '2' in operation:
        print("Введите шифртекст")

    inp_text = text_edit(input())

    while False in [97 <= ord(i) <= 122 for i in inp_text.replace("_", "")]:
        print("Ввод некорректен. Текст должен состоять из латинских букв")
        inp_text = text_edit(input())
    print("Введите ключ шифра")

    inp_key = input()
    if '1' in gamma_type:
        while False in [97 <= ord(i) <= 122 for i in inp_key] or len(inp_key) >= len(inp_text) or len(inp_key) < 3:
            print("Ввод некорректен. Ключ должен состоять из строчных латинских букв и быть короче шифртекста, "
                  "но не короче 3 символов")
            inp_key = input()
    if '2' in gamma_type or '3' in gamma_type:
        while len(inp_key) != 1 or not 97 <= ord(inp_key) <= 122:
            print("Ввод некорректен. Ключ должен состоять из одной латинской буквы")
            inp_key = input()

    print("Результат операции:")
    if '1' in operation:
        if '1' in gamma_type:
            print(encode_by_key(inp_text, inp_key))
        if '2' in gamma_type:
            print(encode_by_msg(inp_text, inp_key))
        if '3' in gamma_type:
            print(encode_by_enc_msg(inp_text, inp_key))
    if '2' in operation:
        if '1' in gamma_type:
            print(decode_by_key(inp_text, inp_key))
        if '2' in gamma_type:
            print(decode_by_msg(inp_text, inp_key))
        if '3' in gamma_type:
            print(decode_by_enc_msg(inp_text, inp_key))


if __name__ == "__main__":
    main()
