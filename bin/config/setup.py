# Constants
package={}

logging_file = "console.log"

urls = {
	"top" : "https://newsapi.org/v2/top-headlines",
	"everything" : "https://newsapi.org/v2/everything",
	"sources" : "https://newsapi.org/v2/sources"
}
countries = {'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr','hk',
             'hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph','pl',
             'pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us','ve','za'}
             
languages = {'ar','en','cn','de','es','fr','he','it','nl','no','pt','ru','sv','ud'}
categories = {'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'}
sort_method = {'relevancy','popularity','publishedAt'}

const_type = {
	"query" : str,
	"sources" : str,
	"language" : str,
	"country" : str,
	"page_size" : int,
	"page_count" : int,
	"domains" : str,
	"date" : str,
	"sort" : str,
	"category" : str
}

