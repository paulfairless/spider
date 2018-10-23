# -*- coding: utf-8 -*-
import scrapy
from re import sub
from decimal import Decimal


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
            { 'url': '/dresses/', 'type': 'dresses', 'department':'women' },
            { 'url': '/denim/', 'type': 'denim', 'department':'women' },
            { 'url': '/tops-and-t-shirts/', 'type': 'tops', 'department':'women' },
            { 'url': '/shirts-and-blouses/', 'type': 'shirts', 'department':'women' },
            { 'url': '/knitwear/', 'type': 'knitwear', 'department':'women' },
            { 'url': '/skirts/', 'type': 'skirts', 'department':'women' },
            { 'url': '/trousers/', 'type': 'trousers', 'department':'women' },
            { 'url': '/shorts/', 'type': 'shorts', 'department':'women' },
            { 'url': '/sweatshirts/', 'type': 'sweatshirts', 'department':'women' },
            { 'url': '/lingerie/', 'type': 'lingerie', 'department':'women' },
            { 'url': '/swimwear/', 'type': 'swimwear', 'department':'women' },
            { 'url': '/shoes/', 'type': 'shoes', 'department':'women' },
            { 'url': '/bags/', 'type': 'bags', 'department':'women' },
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
        if sku is not None: sku=sku.strip().lower()
        title = response.css("meta[itemprop='name']::attr(content)").extract_first()
        if title is not None: title=title.strip()
        color = response.css("ul.swatches li.selected a::text").extract_first()
        if color is not None: color=color.strip().lower()
        images = response.css(".imagecarousel img::attr(src)").extract()
        price = response.css(".product-price .price-sales::text").extract_first()
        if price is not None: price=float(sub(r'[^\d.]', '', price))
        rrp = response.css(".product-price .price-standard::text").extract_first()
        if rrp is not None: 
            rrp=float(sub(r'[^\d.]', '', rrp))
        else:
            rrp = price
        
        sale = False
        if rrp > price:
            sale = True

        yield {
            'brand': 'ganni',
            'store': 'ganni',
            'type': response.meta['type'],
            'department': response.meta['department'],
            'productUrl': response.meta['url'],
            'sku': sku,
            'title': title,
            'color': color,
            'price': price,
            'rrp': rrp,
            'sale': sale,
            'image_urls': images
        }
