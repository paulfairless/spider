# -*- coding: utf-8 -*-
import scrapy


class GanniComSpider(scrapy.Spider):
    name = 'ganni.com'
    allowed_domains = ['ganni.com']
    start_urls = ['http://ganni.com/e']
    base_url = "https://www.ganni.com"

    def parse(self, response):
        pass

    def start_requests(self):
        baseAjaxUrl = 'https://www.ganni.com/en'
        entries = [
            { 'url': '/coats-and-jackets/', 'type': 'coats-and-jackets', 'department':'women' },
        ]
        for entry in entries:
            url = baseAjaxUrl + entry['url']
            yield self.buildRequest(url, entry['type'], entry['department'])

    def buildRequest(self, url, type, department):
        request = scrapy.Request(url=url, callback=self.parse)
        request.meta['url'] = url
        request.meta['type'] = type
        request.meta['department'] = department

        return request

    def buildItemRequest(self, url, type, department):
        request = scrapy.Request(url=url, callback=self.parseProduct)
        request.meta['url'] = url
        request.meta['type'] = type
        request.meta['department'] = department

        return request

    def cleanUrl(self, url):
        if url.startswith('/'):
            url = self.base_url + url
        return scrapy.utils.url.canonicalize_url(url)

    def parse(self, response):
        #  process html products
        products = response.css(".product-tile a")
        for product in products:
            url = self.cleanUrl(product.css("a::attr(href)").extract_first())
            yield self.buildItemRequest(url, response.meta['type'], response.meta['department'])

    
    def parseProduct(self, response):
        sku = response.css("input[id='pid']::attr(value)").extract_first()
        title = response.css("meta[itemprop='name']::attr(content)").extract_first()
        color = response.css("ul.swatches li.selected a::text").extract_first()
        images = response.css(".imagecarousel img::attr(src)").extract()

        yield {
            'brand': 'ganni',
            'store': 'ganni',
            'type': response.meta['type'],
            'department': response.meta['department'],
            'productUrl': response.meta['url'],
            'sku': sku,
            'title': title,
            'color': color,
            'images': images
        }
