from data.most_visited_repository import MostVisitedRepository
from data.search_term_repository import SearchTermRepository

mostVisitedRepo = MostVisitedRepository()
searchTermRepo = SearchTermRepository()

class Charts:

    def __init__(self):
        pass

    def getMostSearchData(self):
        return searchTermRepo.getData

    def getMostVisitedSiteData(self):
        return mostVisitedRepo.getData

    def saveSearchKeyword(self,term):
        try:
            conn=mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO analytics_search_keyword VALUES")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()