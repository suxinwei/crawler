from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello<P>', 'lxml')
print(soup.p.string)
