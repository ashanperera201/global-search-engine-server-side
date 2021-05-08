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

    def saveSearchKeyword(self,term,mysql):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql = "INSERT INTO analytics_search_keyword (search_keyword) VALUES (%s)"
            val = (term)
            cursor.execute(sql, val)
            resp.status_code=200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()