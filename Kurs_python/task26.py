import requests
#with open('dataset_3378_3 (1).txt') as input:
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
b = r.text
print(b)
url = 'https://stepic.org/media/attachments/course67/3.6.3/' + b
c = requests.get(url)
print(c.text)
#r = requests.get(url))
#print(r.text)
#while r.text.startswith("We") == False: