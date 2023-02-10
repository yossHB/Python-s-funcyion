from itertools import count
import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) +1 # 0 is by default value in case there are an error
print(counts)