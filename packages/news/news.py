import json
from urllib import request

async def main(args):
    url = 'http://eventregistry.org/api/v1/event/getBreakingEvents'
    headers = {'Content-Type': 'application/json'}
    data = {
        "eventImageCount": 3,
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

    data = json.dumps(data).encode('utf-8')

    req = request.Request(url, data=data, headers=headers)

    try:
        with request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            return {
                'body': json.loads(result)
            }
    except request.URLError as e:
        return f"Error: {e}"