# Multiple line strings
comment = """
askjfjlkfjsdaljfd
asjf;lsdjafkjlkjsad
dsafjksdjlk;jfa
sdffjdskj;kjlds
fsdiofoadsifjsadf
rpoweiugfnlkjaf
fdasnsadoijlfsalkj
"""
# Something like placeholders
print(comment)
name = "Kyle"
email ="""
 Hello {},
 how are you? 
 It was nice meeting you
 """
print(email.format(name))
# You can also do it like this;
name1 = "Joe"
email =f"""
 Hello {name1},
 how are you? 
 It was nice meeting you
 """
print(email)
