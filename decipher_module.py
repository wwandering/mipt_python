# Deciphering Caesarus cipher through frequency analysis implementation
from cipher_module import Caesar


def get_similarity(message, data, n):
    similarity = 0
    current_pref = message[:n - 1]
    length = len(message)
    for i in range(n - 1, length):
        if current_pref in data and message[i] in data[current_pref]:
            similarity += data[current_pref][message[i]]
        current_pref = (current_pref + message[i])[1:]
    return similarity


def n_builder(message, n):
    n = max(1, n)
    result = dict()
    length = len(message)
    if length < n:
        return result
    current_pref = message[:n - 1]
    for i in range(n - 1, length):
        if current_pref in result:
            if message[i] not in result[current_pref]:
                result[current_pref][message[i]] = 1 / length
            else:
                result[current_pref][message[i]] += 1 / length
        else:
            result[current_pref] = dict()
            result[current_pref][message[i]] = 1 / length
        current_pref = (current_pref + message[i])[1:]
    return result


def deciphering(message, n):
    data = n_builder(message, n)
    tmp = message
    max_similarity = 0
    best = 0
    for key in range(1, 26):
        current_similarity = get_similarity(Caesar(key).decode(tmp), data, n)
        if max_similarity <= current_similarity:
            max_similarity = current_similarity
            best = key
    return Caesar(best).encode(message)
