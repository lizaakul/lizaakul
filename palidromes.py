def is_palindrome(words: str):
    """Ищет палиндромы"""

    words: str = words.lower()
    first,last = 0, len(words) - 1

    while first < last:
        while first < last and not words[first].isalpha():
            first += 1
        while first < last and not words[last].isalpha():
            last -= 1
        if words[first] != words[last]:
            return False
        else:
            first += 1
            last -= 1

    return True


print(is_palindrome("roror"))