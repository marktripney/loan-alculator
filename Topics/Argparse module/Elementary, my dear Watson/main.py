import argparse


def decode_caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


parser = argparse.ArgumentParser()
parser.add_argument('--word')
parser.add_argument('--offset')

args = parser.parse_args()

s, n = [args.word, args.offset]
n = -abs(int(n))

decode_caesar_cipher(s, n)
