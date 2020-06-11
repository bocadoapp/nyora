import scrapy
import json

class RecetasGratis(scrapy.Spider):
  name = 'RecetasGratis'
  allowed_domains = ['recetasgratis.net']
  custom_settings = {
    'FEED_EXPORT_ENCODING': 'utf-8'
  }

  def start_requests(self):
    return [scrapy.Request(
      'https://www.recetasgratis.net/recetas-japonesas',
      callback=self.get_links_from_category
    )]

  def get_links_from_category(self, response):
    yield from response.follow_all(css='div.resultado a', callback=self.parse)
  
  def parse(self, response):
    try:
      site_categories = response.css('ul.breadcrumb li::text').extract_all()
      for annonce in response.css('.list_item'):
          yield{
              'link':annonce.css('::attr(href)').extract_first(),
              'title':annonce.css('.item_title::text').extract_first().strip(),
              }      
    except:
      site_categories = []
    print(site_categories)
    yield {
      'title': response.css('h1::text').extract_first(),
      'site_categories': 
    }