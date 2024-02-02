import requests
import json

def fetchpublicationid(api_url, headers,host_name):
    #---------------getting publication id -------------------
    query = """
    query Publication(
    $host: String
    ) {
    publication(
        host: $host
    ) {
        id
        title
        displayTitle
        descriptionSEO
        }
    }
    """

    input_host = {
        "host": host_name
    }

    # Send the request
    first_response = requests.post(api_url, json={"query": query, "variables": input_host}, headers=headers)
    # Parse the response
    new_result = json.loads(first_response.text)
    # Access the data from the result
    data = new_result.get('data', {})
    publication_id_fetch = data.get('publication', {}).get('id')
    return publication_id_fetch

