import itertools
from collections import Counter
from enchant.checker import SpellChecker
from main import decode_by_key


def frequency_score(text):
    text_freq = Counter(text.replace('_', ''))
    score = 0
    eng_most_freq = {'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r'}
    eng_least_freq = {'j', 'x', 'q', 'z'}
    for i in eng_most_freq:
        if i in [i[0] for i in text_freq.most_common(9)]:
            score += 1
    for i in eng_least_freq:
        if i in [i[0] for i in text_freq.most_common()[:-4-1:-1]]:
            score += 1
    return score


def text_switch_back(text, switch_num):
    res = ''
    for i in text:
        if i == '_':
            res += i
        else:
            res += chr(((ord(i) - switch_num - 97) % 26) + 97)
    return res


def find_best_switch(text):
    switches = {}
    for i in range(0, 26):
        switches[chr(i + 97)] = frequency_score(text_switch_back(text, i))
    return {k: v for k, v in sorted(switches.items(), key=lambda item: item[1], reverse=True)}


def find_key_chrs(text, key_len):
    key_chrs = []
    for i in range(key_len):
        key_chrs.append([])
        best_chrs = find_best_switch(text.replace('_', '')[i::key_len])
        max_score = list(best_chrs.values())[0]
        for j in best_chrs:
            if best_chrs[j] > max_score - 2:
                key_chrs[i].append(j)
    return key_chrs


def find_possible_keys(key_chrs):
    possible_keys = list(itertools.product(*key_chrs))
    for i in range(len(possible_keys)):
        possible_keys[i] = ''.join(possible_keys[i])
    return possible_keys


def try_keys(enc_text, pos_keys):
    res_print = f'Возможные ключи длины {len(pos_keys[0])}:\n'
    enc_texts = {}
    for i in pos_keys:
        decoded = decode_by_key(enc_text, i)
        d = SpellChecker(lang='en')
        d.set_text(decoded.replace('_', ' '))
        prob = float("%.2f" % ((1 - len([i.word for i in d]) / len(enc_text.split('_'))) * 100))
        enc_texts[decoded] = [prob, i]

    enc_texts = {k: v for k, v in sorted(enc_texts.items(), key=lambda item: item[1], reverse=True)}
    for i in enc_texts:
        res_print += f'{enc_texts.get(i)[1]}, вероятность верности ключа: {enc_texts.get(i)[0]}%, полученный текст: ' \
                     f'{i}\n'
    return [res_print, max(enc_texts.items())[0]]


def find_key_len(enc_text):
    enc_text = enc_text.replace('_', '')
    substrings = [
        enc_text[i:i + j]
        for i in range(0, len(enc_text) - 3 + 1)
        for j in range(3, len(enc_text) - i - 1)
    ]
    most_repeated = Counter(substrings).most_common(1)[0][0]
    spaces = []
    for i in enc_text.split(most_repeated):
        spaces.append(len(i) + len(most_repeated))

    spaces_divisors = []
    for i in spaces:
        for j in range(3, i//2):
            if i % j == 0:
                spaces_divisors.append(j)

    return [i[0] for i in Counter(spaces_divisors).most_common(3)]


def main():
    print("Введите шифртекст")
    inp_enc = input()
    key_lens = []
    for i in find_key_len(inp_enc):
        key_lens.append(try_keys(inp_enc, find_possible_keys(find_key_chrs(inp_enc, i))))
    for i in sorted(key_lens, reverse=True):
        print(i[0])


if __name__ == "__main__":
    main()
