from string import ascii_letters

class Caesar:
    step = int()
    alphabet_size = 26

    def __init__(self, key):
        self.step = key

    def encode(self, message):
        result = str()
        for char in message:
            if char not in ascii_letters:
                result += char
            else:
                current_index = ascii_letters.index(char)
                new_index = (current_index + self.step) % self.alphabet_size
                result += ascii_letters[new_index]
        return result

    def decode(self, message):
        result = str()
        for char in message:
            if char not in ascii_letters:
                result += char
            else:
                current_index = ascii_letters.index(char)
                new_index = (current_index - self.step) % self.alphabet_size
                result += ascii_letters[new_index]
        return result


class Vigenere:
    key = str()
    alphabet_size = 26

    def __init__(self, key):
        self.key = key

    def encode(self, message):
        result = str()
        current_pos_in_key = 0
        for char in message:
            if char not in ascii_letters:
                result += char
            else:
                current_index = ascii_letters.index(char)
                new_index = (current_index + ascii_letters.index(self.key[current_pos_in_key])) % self.alphabet_size
                current_pos_in_key = (current_pos_in_key + 1) % len(self.key)
                result += ascii_letters[new_index]
        return result

    def decode(self, message):
        result = str()
        current_pos_in_key = 0
        for char in message:
            if char not in ascii_letters:
                result += char
            else:
                current_index = ascii_letters.index(char)
                new_index = (current_index - ascii_letters.index(self.key[current_pos_in_key])) % self.alphabet_size
                current_pos_in_key = (current_pos_in_key + 1) % len(self.key)
                result += ascii_letters[new_index]
        return result


class Vernam:
    key = str()
    alphabet = ascii_letters

    def __init__(self, key):
        self.key = key

    def encode(self, message):
        result = str()
        current_key_pos = 0
        for char in message:
            key_binary_representation = bin(ord(self.key[current_key_pos]))[2:].zfill(8)
            binary_representation = bin(ord(char))[2:].zfill(8)
            encoded_char = int(binary_representation, 2) ^ int(key_binary_representation, 2)
            result += str().join(chr(encoded_char))
            current_key_pos = (current_key_pos + 1) % len(self.key)
        return result

    def decode(self, message):
        # Thanks to XOR properties, encoding already encoded message with the same key gives us initial message.
        return self.encode(message)
