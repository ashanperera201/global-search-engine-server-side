import pymysql
import requests
import json
from main import app
from database_config import mysql
from flask import jsonify
from flask import flash, request
from flask_cors import cross_origin

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
