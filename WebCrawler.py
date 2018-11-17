from bs4 import BeautifulSoup

myHtml=''''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>This is Crawler</title>
</head>
<body>
<h1>It's good a drink?</h1>
<h1>你喝喝看就知道了!</h1>
<h2>Who care?</h2>
<p>This is Joe, I'm 9527</p>
</body>
</html>'''

soup=BeautifulSoup(myHtml,'html.parser')

#myH1=soup.find('h1')
myH1=soup.findAll('h1')

for i in myH1:
    if '你喝' in i.string:
        print(i.string)
#print(myH1)
#print(myH1.string)