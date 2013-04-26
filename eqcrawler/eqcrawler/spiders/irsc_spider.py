from scrapy.http import FormRequest
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from eqcrawler.items import EarthquakeItem


class IRSCSpider(BaseSpider):

    name = 'irsc.ut.ac.ir'
    allowed_domains = ['irsc.ut.ac.ir']
    start_urls = ['http://irsc.ut.ac.ir/currentearthq.php']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        eqs = hxs.select("//tr[contains(@class,'DataRow')]")

        for eq in eqs:
            earthquake = EarthquakeItem()
            earthquake['date'] = eq.select('td/span/a/text()').extract()[0]
            earthquake['lattitude'] = eq.select('td[3]/text()').extract()[0]
            earthquake['longitude'] = eq.select('td[4]/text()').extract()[0]
            earthquake['depth'] = eq.select('td[5]/text()').extract()[0]
            earthquake['magnitude'] = eq.select('td[6]/text()').extract()[0]
            earthquake['region'] = eq.select('td[7]/text()').extract()[0]
            yield earthquake


class IRSCSearchSpider(BaseSpider):
    name = 'search.irsc.ut.ac.ir'
    allowed_domains = ['irsc.ut.ac.ir']
    start_urls = ['http://irsc.ut.ac.ir/bulletin.php']

    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'start_Y': '2006',
                              'start_M': '01',
                              'start_D': '01',
                              'start_H': '00',
                              'end_Y': '2014',
                              'min_mag': '4',
                              'max_mag': '10',
                              'action': 'Search'},
                    callback=self.after_search)]

    def after_search(self, response):
        hxs = HtmlXPathSelector(response)

        eqs = hxs.select("//tr[contains(@class,'DataRow')]")

        for eq in eqs:
            earthquake = EarthquakeItem()
            earthquake['id'] = eq.select('td[2]/text()').extract()[0]
            earthquake['date'] = eq.select('td/span/a/text()').extract()[0]
            earthquake['lattitude'] = eq.select('td[4]/text()').extract()[0]
            earthquake['longitude'] = eq.select('td[5]/text()').extract()[0]
            earthquake['depth'] = eq.select('td[6]/text()').extract()[0]
            earthquake['magnitude'] = eq.select('td[7]/text()').extract()[0]
            # earthquake['region'] = eq.select('td[7]/text()').extract()[0]
            yield earthquake
