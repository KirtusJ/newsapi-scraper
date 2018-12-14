from config import setup 
from config.constants import Const
import requests

const = Const(
	setup.urls, setup.countries, setup.languages, setup.categories, setup.sort_method
)

class Query():
	def connect(url,auth,timeout,params):
		req = requests.get(url, auth=auth, timeout=timeout, params=params)
		if req.status_code != requests.codes.ok:
			raise Exception(f"{requests.status_codes._codes[req.status_code]}")
		return req.json()
	def get_query(query,package):
		if query is not None:
			if Const.verify(query, "query"):
				package["q"] = query
			else:
				raise TypeError("Query must be type: {}".format(str(setup.const_type.get("query").__name__)))
	def get_sources(sources,package):
		if sources is not None:
			if Const.verify(sources, "sources"):
				package["sources"] = sources
			else:
				raise TypeError("Sources must be type: {}".format(str(setup.const_type.get("sources").__name__)))
	def get_language(language,package):
		if language is not None:
			if Const.verify(language, "language"):
				if language in const.get_languages():
					package["language"] = language
				else:
					raise ValueError("Language not found")
			else:
				raise Exception("Language must be type: {}".format(str(setup.const_type.get("language").__name__)))
	def get_country(country,package):
		if country is not None:
			if Const.verify(country, "country"):
				if country in const.get_countries():
					package["country"] = country
				else:
					raise ValueError("Country not found")
			else:
				raise TypeError("Country must be type: {}".format(str(setup.const_type.get("country").__name__)))
	def get_page_size(page_size,package):
		if page_size is not None:
			if Const.verify(page_size, "page_size"):
				if not page_size > 0:
					package["page_size"] = 1
				elif page_size <= 100:
					package["pageSize"] = page_size
			else:
				raise TypeError("Page size must be type: {}".format(str(setup.const_type.get("page_size").__name__)))
	def get_page_count(page_count,package):
		if page_count is not None:
			if Const.verify(page_count, "page_count"):
				if not page_count > 0:
					package["page_count"] = 1
				elif page_count <= 100:
					package["page_count"] = page_count
				else:
					package["page"] = 100
			else:
				raise TypeError("Page count must be type: {}".format(str(setup.const_type.get("page_count").__name__)))
	def get_domains(domains,package,verse):
		if domains is not None:
   			if Const.verify(domains, "domains"):
   			    package[verse] = domains
   			else:
   			    raise TypeError("Domains must be type: {}".format(str(setup.const_type.get("domains").__name__)))
	def get_date(date,package,verse):
 		if date is not None:
 			if Const.verify(date, "date"):
 				if (len(date)) >= 10:
 					for i in range(len(date)):
 						if (i == 4 and date[i] != '-') or (i == 7 and date[i] != '-'):
 							raise ValueError("Date must be type: YYYY-MM-DD")
 						else:
 							package[verse] = date
 				else:
 					raise ValueError("Date must be type: YYYy-MM-DD")
 			else:
 				raise TypeError("Date must be type: {}".format(str(setup.const_type.get("date").__name__)))
	def get_sort(sort,package):
 		if sort is not None:
 			if Const.verify(sort, "sort"):
 				if sort in const.get_sort():
 					package["sortBy"] = sort
 				else:
 					raise ValueError("Sort type not found")
 			else:
 				raise TypeError("Sort must be type: {}".format(str(setup.const_type.get("sort").__name__)))
	def get_category(category,package):
		if category is not None:
			if Const.verify(category, "category"):
				if category in const.get_categories():
					package["category"] = category
				else:
					raise ValueError("Category not found")
			else:
				raise TypeError("Category must be type: {}".format(str(setup.const_type.get("category").__name__)))