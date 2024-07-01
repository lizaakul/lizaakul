def is_palindrome(words: str) -> bool:
    """Ищет палиндромы"""

    words: str = words.lower()
    first,last = 0, len(words) - 1

    while first < last:
        if not words[first].isalpha():
            first += 1
        if not words[last].isalpha():
            last -= 1
        if words[first] != words[last]:
            return False

        first += 1
        last -= 1

    return True


print(is_palindrome("r o r o r"))