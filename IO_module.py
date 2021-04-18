import argparse
import cipher_module
import decipher_module


def read_data(file):
    with open(file, 'r') as content:
        text = content.read()
    return text


def write_data(data, file):
    with open(file, 'w') as content:
        content.write(data)


def encode(args):
    try:
        if args.cipher == "vernam":
            text = read_data(args.input)
            cipher_instance = cipher_module.Vernam(args.key)
            write_data(cipher_instance.encode(text), args.output)
        elif args.cipher == "caesar":
            text = read_data(args.input)
            key = int(args.key)
            cipher_instance = cipher_module.Caesar(key)
            write_data(cipher_instance.encode(text), args.output)
        else:
            text = read_data(args.input)
            cipher_instance = cipher_module.Vigenere(args.key)
            write_data(cipher_instance.encode(text), args.output)
    except args.input.isempty():
        print("You must provide a correct (non-empty) input")


def decode(args):
    try:
        if args.cipher == "vernam":
            text = read_data(args.input)
            cipher_instance = cipher_module.Vernam(args.key)
            write_data(cipher_instance.decode(text), args.output)
        elif args.cipher == "caesar":
            text = read_data(args.input)
            key = int(args.key)
            cipher_instance = cipher_module.Caesar(key)
            write_data(cipher_instance.decode(text), args.output)
        else:
            text = read_data(args.input)
            cipher_instance = cipher_module.Vigenere(args.key)
            write_data(cipher_instance.decode(text), args.output)
    except args.input.isempty():
        print("You must provide a correct (non-empty) input")


def attack(args):
    try:
        text = read_data(args.input)
        write_data(decipher_module.deciphering(text, args.n), args.output)
    except args.input.isempty():
        print("You must provide a correct (non-empty) input")


def get_arguments():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers()

    # Encoding
    encode_parser = subs.add_parser("encode")
    encode_parser.set_defaults(action="encode", func=encode)
    encode_parser.add_argument("-c", "--cipher", type=str, help="Available options: caesar, vigenere, vernam",
                               required=True, choices=["caesar", "vigenere", "vernam"])
    encode_parser.add_argument("-k", "--key", type=str, help="Must be a word (or an integer in case of Caesar cipher",
                               required=True)
    encode_parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
    encode_parser.add_argument("-o", "--output", type=str, help="Output file path", required=True)

    # Decoding
    decode_parser = subs.add_parser("decode")
    decode_parser.set_defaults(action="decode", func=decode)
    decode_parser.add_argument("-c", "--cipher", type=str, help="Available options: caesar, vigenere, vernam",
                               required=True, choices=["caesar", "vigenere", "vernam"])
    decode_parser.add_argument("-k", "--key", type=str, help="Must be a word (or an integer in case of Caesar cipher",
                               required=True)
    decode_parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
    decode_parser.add_argument("-o", "--output", type=str, help="Output file path", required=True)

    # Attacking
    attack_parser = subs.add_parser("attack")
    attack_parser.set_defaults(action="attack", func=attack)
    attack_parser.add_argument("-n", type=int, help="A positive integer parameter for frequence analysis"
                                                    " choosing N-grams to analyse", required=True)
    attack_parser.add_argument("-i", "--input", type=str, help="input file path", required=True)
    attack_parser.add_argument("-o", "--output", type=str, help="output file path", required=True)

    return parser.parse_args()
