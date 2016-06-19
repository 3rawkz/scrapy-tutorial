import scrapy

from tutorial.items import AdBlockItem

class AdblockSites(scrapy.Spider):
  name = "adblock"

  start_urls = [
    "http://www.bild.de/",
    "http://www.forbes.com/"
  ]

  def parse(self, response):
    item = AdBlockItem()

    item['html'] = response.xpath('//body').extract()
    item['js'] = response.xpath('//script').extract()

    yield item
