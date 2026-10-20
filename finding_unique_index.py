s="abcabc"
unique_chars=""
for chars in s:
    if chars not in unique_chars:
        unique_chars+=chars
b=len(unique_chars)
print("there are ",b,"unique characters")