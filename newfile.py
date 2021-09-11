import codecs


st = r"I'm \nBangladesh"
st1 = codecs.decode(st,'unicode_escape')
print(st1)
