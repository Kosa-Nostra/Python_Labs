import re
phone_shablon = re.compile(r'\+?7[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}|8[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}')
text = """
+7 912 345-67-89
8(495)123-45-67
+79123456789
8 800 555 35 35
0 922 15 32 32
"""
phones = phone_shablon.findall(text)
print(phones)
