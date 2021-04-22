from flask import Flask, jsonify
from flask_cors import cross_origin
from business.riyasewana_spider import RiyasewanaSpider
from business.patpat_spider import PatPatSpider
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


@app.route("/scrape/<string:term>")
@cross_origin()
def scrape(term):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    retVal2 = search_term(term)

    stcructs = structuredata(output_data, retVal2)
    return jsonify(stcructs)


@app.route("/api/requests/<string:term>")
def search_term(term):
    url = "https://ikman.lk/data/serp"
    term = term.replace("-", "")
    params = {
        "top_ads": 1,
        "spotlights": 5,
        "sort": "relevance",
        "buy_now": 0,
        "urgent": 0,
        "categorySlug": "vehicles",
        "locationSlug": "sri-lanka",
        "category": 391,
        "query": term,
        "page": 1,
    }
    result = requests.get(url, params)
    return result.json()


@crochet.wait_for(timeout=10.0)
def scrape_with_crochet(search):
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    xa = {RiyasewanaSpider}
    riya_sewana = []
    for x in xa:
        # riya_sewana = crawl_runner.crawl(x, category="es-8")
        riya_sewana = crawl_runner.crawl(x, category=search)
        # print (riya_sewana)
        return riya_sewana

@crochet.wait_for(timeout=10.0)
def scrape_with_patpat(search):
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    xa = {PatPatSpider}
    patpat = []
    search = search.replace("-", "")
    for x in xa:
        # patpat = crawl_runner.crawl(x, category="es-8")
        patpat = crawl_runner.crawl(x, category=search)
        # print (patpat)
        return patpat


def _crawler_result(item, response, spider):
    output_data.append(dict(item))

def structuredata(riyasewana, ikman):

    ikmanAds = []
    for ads in ikman['ads']:
        tmpArr = {}
        tmpArr = {
            'image' : ads['imgUrl'],
            'link' : 'https://ikman.lk/en/ad/' + ads['slug'],
            'name' : ads['title'],
            'price': "Not Mentioned" if 'price' not in ads else ads['price'],
        }
        ikmanAds.append(tmpArr)
    
    for ads in riyasewana:
        tmpArr = {}
        tmpArr = {
            'image' : ads['image'],
            'link' : ads['link'],
            'name' : ads['name'],
            'price': ads['price'],
        }
        ikmanAds.append(tmpArr)

    return ikmanAds

app.run(port=5000)