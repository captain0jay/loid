import requests
import json
from loid.scripts.fetchpublicationid import fetchpublicationid
from tabulate import tabulate
from loid.scripts.showtabledata import print_tablemain

def getpublication(api_url,headers,host_name):
  #-----------------publish draft-------------------------------

  mutation = """
  query SearchPostsOfPublication(
    $first: Int!,
    $filter: SearchPostsOfPublicationFilter!
  ) {
    searchPostsOfPublication(
      first: $first,
      filter: $filter
    ) {
      edges {
      node {
          id
          slug
          title
          tags{
            id
            name
          }
          url
          author{
            id
          }
          coAuthors{
            id
          }
          views
          publication{
            id
          }
          brief
        }
        cursor
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
  """

  publication_id_fetch = fetchpublicationid(api_url, headers,host_name);

  input_data = {
      "first": 5,
      "filter": {
          "query": "How",
          "publicationId": publication_id_fetch
      }
  }

  # Send the request
  first_response = requests.post(api_url, json={"query": mutation, "variables": input_data}, headers=headers)

  # Parse the response
  table_data = []
  new_result = json.loads(first_response.text)
  # Access the data from the result
  data = new_result.get('data', {})
  feedposts = data.get('searchPostsOfPublication', {}).get('edges', [])
  table_data = []
  for feedpost in feedposts:
    feedpostid = feedpost.get('node', {}).get('id')
    feedposttitle = feedpost.get('node', {}).get('title')
    feedpostviews = feedpost.get('node', {}).get('views')

    table_data.append([feedpostid, feedposttitle, feedpostviews])

  headers = ["id", "title", "views"]
  print(tabulate(table_data, headers=headers, tablefmt="grid"))
  print_tablemain(table_data)