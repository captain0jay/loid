import requests
import json
from tabulate import tabulate

def listonlinedrafts(api_url,headers):
# Define your GraphQL query
  query = """
  query Me {
      me {
        username
        name
        profilePicture
        publications(first: 50) {
          edges {
            node {
              drafts(first: 10) {
                edges {
                  node {
                    id
                    slug
                    title
                  }
                }
              }
            }
          }
        }
      }
    }
  """

  # Send the GraphQL request
  response = requests.post(api_url, json={'query': query}, headers=headers)

  # Check for errors
  if response.status_code != 200:
      print(f"Error {response.status_code}: {response.text}")
  else:
      print("Hashnode Request Successful")

  # Parse the response
  result = json.loads(response.text)
  # Access the data from the result
  data = result.get('data', {})

  table_data = []
  drafts = data.get('me', {}).get('publications', {}).get('edges', [])[0].get('node', {}).get('drafts', {}).get('edges', [])
  for draft in drafts:
    draftid = draft.get('node', {}).get('id')
    title = draft.get('node', {}).get('title')
    slug = draft.get('node', {}).get('slug')

    table_data.append([draftid, title, slug])

  headers = ["id", "title", "slug"]
  print(tabulate(table_data, headers=headers, tablefmt="grid"))
