from .setup import const_type

class Const():
	def __init__(self,urls,countries,languages,categories,sort_method):
		self.urls = urls
		self.countries = countries
		self.languages = languages
		self.categories = categories
		self.sort_method = sort_method

	def get_sort_methods(self):
		return self.sort_method
	def get_top(self):
		return self.urls["top"]
	def get_everything(self):
		return self.urls["everything"]
	def get_sources(self):
		return self.urls["sources"]
	def get_countries(self):
		return self.countries
	def get_languages(self):
		return self.languages
	def get_categories(self):
		return self.categories
	def get_sort(self):
		return self.sort_method
	def verify(var, const):
		if type(var) == const_type[const]:
			return True
		return False