from string import ascii_letters

class Caesar:
    step = int()
    alphabet_size = 26

    def __init__(self, key):
        """
        Initialize Caesar entity with given step
        :param key: step size
        """
        self.step = key

    def encode(self, message):
        """
        Encodes text with Caesar cipher and given step
        :param message: text content
        :return: encoded text
        """
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
        """
        Decodes text with Caesar cipher and given step
        :param message: text content
        :return: decoded text
        """
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
        """
        Initialize Vigenere entity with given key
        :param key: key
        """
        self.key = key

    def encode(self, message):
        """
        Encodes text with Vigenere cipher and given key
        :param message: text content
        :return: encoded text
        """
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
        """
        Decodes text with Vigenere cipher and given key
        :param message: text content
        :return: decoded text
        """
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
        """
        Initialize Vernam entity with given key
        :param key: key
        """
        self.key = key

    def encode(self, message):
        """
        Encodes text with Vernam cipher and given key
        :param message: text content
        :return: encoded text
        """
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
        """
        Decodes text with Vernam cipher and given key
        :param message: text content
        :return: decoded text
        """
        # Thanks to XOR properties, encoding already encoded message with the same key gives us initial message.
        return self.encode(message)
