from bs4 import BeautifulSoup

soup = BeautifulSoup(
    html_doc, #html 文档字符串
    'html.parser',# html解析器
    from_endcoding='utf8' #html文档的编码
)
#搜索节点(find_a,find)
soup.find_all('a')

soup.find_all(reg)
soup.find_all('div',class_='abc', string='Python')

#访问节点信息：<a href=''></a>

