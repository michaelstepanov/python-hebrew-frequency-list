import scrapy
from scrapy.selector import Selector
from hebrew_frequency_list.items import HebrewFrequencyListItem


class HebrewFrequencyListSpider(scrapy.Spider):
    name = 'hebrew_frequency_list'
    allowed_domains = ['teachmehebrew.com']
    start_urls = ['http://www.teachmehebrew.com/hebrew-frequency-list.html']

    def parse(self, response):
        selector = Selector(response)
        words = selector.xpath('//*[@id="wsite-content"]//tr[position()>1]')
        item = HebrewFrequencyListItem()
        for word in words:
            if not word.xpath('.//td[1]/text()').extract():
                item['rank'] = ''
            else:
                item['rank'] = str(word.xpath('.//td[1]/text()').extract()[0].strip().encode('utf8'))

            if not word.xpath('.//td[2]/text()').extract():
                item['english'] = ''
            else:
                item['english'] = str(word.xpath('.//td[2]/text()').extract()[0].strip().encode('utf8'))

            if not word.xpath('.//td[3]/text()').extract():
                item['transliteration'] = ''
            else:
                item['transliteration'] = str(word.xpath('.//td[3]/text()').extract()[0].strip().encode('utf8'))

            if not word.xpath('.//td[4]/text()').extract():
                item['hebrew'] = ''
            else:
                item['hebrew'] = str(word.xpath('.//td[4]/text()').extract()[0].strip().encode('utf8'))

            yield item
