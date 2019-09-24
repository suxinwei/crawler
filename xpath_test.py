from lxml import etree

html = etree.parse('./xpath_test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
