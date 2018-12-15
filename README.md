# newsapi-scraper
A Python client for the [News API](https://newsapi.org/docs/)

Built for development of [Event Logger](https://github.com/KirtusJ/Event-Logger)

# pip install newsapi-scraper

from scrapenewsapi import News

news = News(api_key=api_key)

# Endpoints

Endpoints return JSON Object based on the input you give them

## query_top

	"top" : "https://newsapi.org/v2/top-headlines"

### options

query, sources, language, country, page_size, page_count
  
## query_everything

    "everything" : "https://newsapi.org/v2/everything"

### options

query, sources, language, domains, exclude_domains, from_date, to_date, sort, page_size, page_count
 
## query_sources:

	 "sources" : "https://newsapi.org/v2/sources"
   
### options

category, country, language
   

# Input
  
### countries:

      'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr','hk',
      'hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph','pl',
      'pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us','ve','za'
             
### languages:
           
      'ar','en','cn','de','es','fr','he','it','nl','no','pt','ru','sv','ud'
      
### categories:

    'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'}

### sort_method :
  
    'relevancy','popularity','publishedAt'

### Input types

      "query" : str
      "sources" : str
      "language" : str
      "country" : str
      "page_size" : int
      "page_count" : int
      "domains" : str
      "date" : str
      "sort" : str
      "category" : str
 
