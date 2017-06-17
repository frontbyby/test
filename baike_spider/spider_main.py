# -*- coding:utf-8 -*- 
import html_downloader
import html_output
import html_parser
import url_manager
import urllib.parse
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPaser()
        self.outputer = html_output.HtmlOutputer()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, urllib.parse.unquote(new_url)))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 5:
                    break
                count = count + 1
            except:
                print('craw faild')
        
        self.outputer.output_html()
        
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"# 入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)#启动爬虫
