from flask import Flask, jsonify
from business.web_scrapy_manager import WebScraper
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import crochet
from scrapy import signals
import requests
import json

crochet.setup()

app = Flask(__name__)


output_data = []


crawl_runner = CrawlerRunner()


@app.route("/scrape")
def scrape():
    scrape_with_crochet()
    return jsonify(output_data)
    
@app.route('/api/requests/<string:term>')
def search_term(term):
    url = 'https://ikman.lk/data/serp'
    params = {
            "top_ads": 1,
            "spotlights": 5,
            "sort": "relevance",
            "buy_now": 0,
            "urgent": 0,
            "categorySlug": "van",
            "locationSlug": "colombo",
            "category": 391,
            "query": term,
            "page": 1             
        }
    result = requests.get(url, params)
    return result.json()


@crochet.wait_for(timeout=10.0)
def scrape_with_crochet():
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(WebScraper)
    return eventual


def _crawler_result(item, response, spider):
    output_data.append(dict(item))


app.run(port=5000)