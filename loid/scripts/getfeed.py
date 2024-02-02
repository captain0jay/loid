import requests
import json
from tabulate import tabulate
from loid.scripts.showtabledata import print_tablemain
def getfeed(api_url, headers,numofposts):
      #-----------------publish draft-------------------------------

  mutation = """
  query Feed(
    $first: Int!
  ) {
    feed(
      first: $first
    ) {
      edges {
      node {
          id
          title
          url
          author{
            id
          }
          views
          publication{
            id
          }
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

  input_data = {
      "first": numofposts
  }

  # Send the request
  first_response = requests.post(api_url, json={"query": mutation, "variables": input_data}, headers=headers)

  # Parse the response
  new_result = json.loads(first_response.text)
  # Access the data from the result
  data = new_result.get('data', {})
  feedposts = data.get('feed', {}).get('edges', [])
  table_data = []
  for feedpost in feedposts:
    feedpostid = feedpost.get('node', {}).get('id')
    feedposttitle = feedpost.get('node', {}).get('title')
    feedpostviews = feedpost.get('node', {}).get('views')

    table_data.append([feedpostid, feedposttitle, feedpostviews])

  headers = ["id", "title", "views"]
  print(tabulate(table_data, headers=headers, tablefmt="grid"))
  print_tablemain(table_data)
