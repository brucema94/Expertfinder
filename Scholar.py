from serpapi import GoogleSearch
params = {
  "engine": "google_scholar",
  "q": "biology",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results['organic_results']