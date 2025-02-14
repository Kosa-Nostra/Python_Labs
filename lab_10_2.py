import re
email_shablon = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
text = """
muzhdabaev.a.i.23@gmail.com
muzdabaev252@gmail.com
aider2307@gmail.com
testuser@testdomen.com
"""
emails = email_shablon.findall(text)
print(emails)
