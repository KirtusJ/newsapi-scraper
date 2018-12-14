from config import setup
from config.auth import Authenticate
from .queries import Query as queries

class News(object):
	def __init__(self, api_key):
		self.auth = Authenticate(api_key=api_key)
		self.package = setup.package

	def query_top(self,query=None,sources=None,language=None,country=None,page_size=None,page_count=None):
		queries.get_query(query, self.package)
		queries.get_sources(sources, self.package)
		queries.get_language(language, self.package)
		queries.get_country(country, self.package)
		queries.get_page_size(page_size, self.package)
		queries.get_page_count(page_count, self.package)
		return queries.connect(setup.urls.get("top"), self.auth, 30, self.package)

	def query_everything(self,query=None,sources=None,domains=None,exclude_domains=None,from_date=None,to_date=None,language=None,sort=None,page_count=None,page_size=None):
		queries.get_query(query, self.package)
		queries.get_sources(sources, self.package)
		queries.get_language(language, self.package)
		queries.get_domains(domains, self.package, "domain")
		queries.get_domains(exclude_domains, self.package, "exclude_domains")
		queries.get_date(from_date, self.package, "from")
		queries.get_date(to_date, self.package, "to")
		queries.get_sort(sort, self.package)
		queries.get_page_size(page_size, self.package)
		queries.get_page_count(page_count, self.package)
		return queries.connect(setup.urls.get("everything"), self.auth, 30, self.package)

	def query_sources(self,category=None,language=None,country=None):
		queries.get_category(category, self.package)
		queries.get_country(country, self.package)
		queries.get_language(language, self.package)
		return queries.connect(setup.urls.get("sources"), self.auth, 30, self.package)

