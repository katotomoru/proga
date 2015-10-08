import re
a = re.compile('<title>(.*?)</title>')
b = re.compile('\[\[(.*?)\]\]')
c = re.compile('<text>(.*?)([.\n])*</text>')

all_titles = []
references = []
wu = []


f = open('xhwiktionary-20151002-pages-articles-multistream.xml', 'r', encoding='utf-8')
for i in f.readlines():
    articles = re.findall(a, i)
    for ii in articles:
        all_titles.append(ii)
    links = re.findall(b, i)
    for l in links:
        references.append(len(l))

for i in f.read():
    text = re.findall(c, i)
    for words in text:
        wu.append(words)

f.close()

print (len(references))
print (all_titles)
print (wu)

f1 = open('Dumps sqwiki.csv', 'w', encoding='utf-8')
f1.write('Title;References;Word usage')

for n in range(len(all_titles)):
     f1.write(all_titles[n] + ';' + links[n] + ';' + wu[n] + '/n')

f1.close()
