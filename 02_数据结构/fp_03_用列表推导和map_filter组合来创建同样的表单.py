symbols = '$¢£¥€¤₽'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
