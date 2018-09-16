# -*- coding: utf-8 -*-
import scrapy


class EbaySpider(scrapy.Spider):
	
	name = "ebay"
	allowed_domains = ["ebay.com"]
	start_urls = ["http://www.ebay.com"]

	# Allow a custom parameter (-a flag in the scrapy command)
	def __init__(self, search="nintendo switch console"):
		self.search_string = search

	def parse(self, response):
		# Extrach the trksid to build a search request	
		trksid = response.css("input[type='hidden'][name='_trksid']").xpath("@value").extract()[0]       
		
		yield scrapy.Request("http://www.ebay.com/sch/i.html?_from=R40&_trksid=" + trksid +
							 "&_nkw=" + self.search_string.replace(' ','+'), 
							 callback=self.parse_link)

	# Parse the search results
	def parse_link(self, response):
		scrapy.utils.response.open_in_browser(response)

		results = response.xpath('//li[@class="s-item "]')

		# Extract info for each product
		for product in results:
			name = product.xpath('.//*[@class="s-item__title"]/text()').extract_first()
			price = product.xpath('.//*[@class="s-item__price"]/text()').extract_first()
			status = product.xpath('.//*[@class="SECONDARY_INFO"]/text()').extract_first()
			seller_level = product.xpath('.//*[@class="s-item__etrs-text"]/text()').extract_first()
			location = product.xpath('.//*[@class="s-item__location s-item__itemLocation"]/text()').extract_first()

			# Set default values
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
		
		next_page_url = response.xpath('//*[@class="x-pagination__control"][2]/@href').extract_first()
		yield scrapy.Request(next_page_url)       	


