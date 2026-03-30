s = "A man, a plan, a canal: Panama"
cleaned = "".join(c.lower() for c in s if c.isalnum())
is_palin = cleaned == cleaned[::-1]
print("Palindrome" if is_palin else "Not a palindrome")
