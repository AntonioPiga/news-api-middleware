import requests

def main(args):
    url = 'http://eventregistry.org/api/v1/event/getBreakingEvents'
    headers = {'Content-Type': 'application/json'}
    data = {
        "eventImageCount": 1,
        "breakingEventsCount": 1,
        "includeEventSummary": True,
        "includeEventLocation": False,
        "includeEventSocialScore": False,
        "includeEventArticleCounts": False,
        "includeEventConcepts": False,
        "includeEventCategories": False,
        "includeConceptLabel": False,
        "includeEventSentiment": False,
        "includeLocationGeoLocation": False,
        "apiKey": args.get('API_KEY')
    }

    response = requests.get(url, headers=headers, json=data)

    if response.status_code == 200:
        return {
            'body': response.json()
        }
    else:
        return f"Error: {response.status_code} - {response.text}"