from flask import Flask, jsonify
from flask_cors import cross_origin
from business.riyasewana_spider import RiyasewanaSpider
from business.patpat_spider import PatPatSpider
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from flaskext.mysql import MySQL
import crochet
from scrapy import signals
import requests
import json
import random

crochet.setup()

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'drowssap'
app.config['MYSQL_DATABASE_DB'] = 'glb_search_eng'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


output_data = []


crawl_runner = CrawlerRunner()


@app.route("/scrape/<string:term>")
@cross_origin()
def scrape(term):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    ikman_ret = scrape_with_ikman(term)

    stcructs = structuredata(output_data, ikman_ret)
    return jsonify(stcructs)


@app.route("/api/requests/<string:term>")
def scrape_with_ikman(term):
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


@app.route("/api/searchTerm/<string:term>")
@cross_origin()
def postSearchTerm(term):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    ikman_ret = scrape_with_ikman(term)

    stcructs = structuredata(output_data, ikman_ret)
    return jsonify(stcructs)


@app.route("/api/siteVisit/<string:website>")
@cross_origin()
def postSiteVisit(website):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    ikman_ret = scrape_with_ikman(term)

    stcructs = structuredata(output_data, ikman_ret)
    return jsonify(stcructs)


@app.route("/api/chart/mostSearch")
@cross_origin()
def getMostSearchedChatData(term):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    ikman_ret = scrape_with_ikman(term)

    stcructs = structuredata(output_data, ikman_ret)
    return jsonify(stcructs)


@app.route("/api/chart/mostVisit")
@cross_origin()
def getMostVisitedChatData(term):
    output_data.clear()
    scrape_with_crochet(term)
    scrape_with_patpat(term)
    ikman_ret = scrape_with_ikman(term)

    stcructs = structuredata(output_data, ikman_ret)
    return jsonify(stcructs)


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

def structuredata(scrape, ikman):
    finalArr = []
    ikmanAds = []
    for ads in ikman['ads']:
        tmpArr = {}
        tmpArr = {
            'image' : ads['imgUrl'],
            'link' : 'https://ikman.lk/en/ad/' + ads['slug'],
            'name' : ads['title'],
            'price': "Not Mentioned" if 'price' not in ads else ads['price'].replace("Rs", "Rs.").strip(),
            'label': "Ikman"
        }
        ikmanAds.append(tmpArr)
    
    firstIkman = ikmanAds[:10]
    del ikmanAds[:10]
    adsCount = len(ikmanAds)

    for ads in scrape:
        tmpArr = {}
        tmpArr = {
            'image' : ads['image'],
            'link' : ads['link'],
            'name' : ads['name'],
            'price': ads['price'].replace("LKR", "Rs.").strip(),
            'label': ads['label']
        }
        ikmanAds.append(tmpArr)

    firstRiyasewana = ikmanAds[adsCount:adsCount+10]
    del ikmanAds[adsCount:adsCount:adsCount+10]

    totalFirst = [];

    for first in firstIkman:
        totalFirst.append(first)

    for first in firstRiyasewana:
        totalFirst.append(first)

    random.shuffle(totalFirst)

    totArray = []

    for first in totalFirst:
        totArray.append(first)

    for last in ikmanAds:
        totArray.append(last)

    return totArray


app.run(port=5000)