import requests
import json

def fetchtagid(api_url, headers):
    #--------------------tag fetch-------------------------

    tag_query = """
    query Tag($slug: String!) {
    tag(slug: $slug) {
        id
        name
        slug
    }
    }"""

    tag_input_host = {
        "slug": "coding"
    }

    # Send the request
    tag_response = requests.post(api_url, json={"query": tag_query, "variables": tag_input_host}, headers=headers)
    # Parse the response
    tag_result = json.loads(tag_response.text)
    # Access the data from the result
    data = tag_result.get('data', {})
    tag_fetch = data.get('tag', {}).get('id')
    return tag_fetch
