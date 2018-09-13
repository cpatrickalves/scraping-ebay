# -*- coding: utf-8 -*-
import scrapy


class EbaySpider(scrapy.Spider):
	name = 'ebay'
	allowed_domains = ['ebay.com']
	start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=%22nintendo+switch+console%22&rt=nc&_ipg=200']

	def parse(self, response):
		results = response.xpath('//li[@class="s-item "]')

		for product in results:
			name = product.xpath('.//*[@class="s-item__title"]/text()').extract_first()
			price = product.xpath('.//*[@class="s-item__price"]/text()').extract_first()
			status = product.xpath('.//*[@class="SECONDARY_INFO"]/text()').extract_first()
			seller_level = product.xpath('.//*[@class="s-item__etrs-text"]/text()').extract_first()
			location = product.xpath('.//*[@class="s-item__location s-item__itemLocation"]/text()').extract_first()

			stars = -1
			ratings = 0

			stars_text = product.xpath('.//*[@class="clipped"]/text()').extract_first()
			if stars_text: stars = stars_text[:3]
			ratings_text = product.xpath('.//*[@aria-hidden="true"]/text()').extract_first()
			if ratings_text: ratings = ratings_text.split(' ')[0]

			yield{
			"Name":name,
			"Status":status,
			"Seller_Level":seller_level,
			"Location":location,
			"Price":price,
			"Stars":stars,
			"Ratings":ratings
			}

		#https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=%22nintendo+switch+console%22&rt=nc&_pgn=2
		next_page_url = response.xpath('//*[@class="x-pagination__control"][2]/@href').extract_first()
		yield scrapy.Request(next_page_url)       	


