import requests
import json
from loid.scripts.fetchpublicationid import fetchpublicationid
from loid.scripts.fetchtagid import fetchtagid
from tabulate import tabulate

def publishdraft(api_url, headers, file_contents,host_name,maintitle,mainslug,posttag,postnewslug):
  publication_id_fetch = fetchpublicationid(api_url, headers,host_name);
  tag_fetch = fetchtagid(api_url, headers);
    #--------------------publish-------------------------
  # Define your GraphQL query
  mutation = """
  mutation PublishPost($input: PublishPostInput!) {
      publishPost(input: $input) {
        post {
          id
          slug
          title
          subtitle
        }
      }
    }
  """

  input_data = {
      "input": {
          "title": maintitle,
          "publicationId": publication_id_fetch,
          "contentMarkdown": file_contents,
          "slug": mainslug,
          "tags": {"id": tag_fetch, "name": posttag, "slug": postnewslug},
      }
  }

  # Send the request
  response = requests.post(api_url, json={"query": mutation, "variables": input_data}, headers=headers)

  # Check for errors
  if response.status_code != 200:
      print(f"Error {response.status_code}: {response.text}")
  else:
      print("Draft Published")

  # Parse the response
  result = json.loads(response.text)
  # Access the data from the result
  data = result.get('data', {})
  table_data = []
# Define headers for the table
  postid = data.get('publishPost', {}).get('post', {}).get('id')
  posttitle = data.get('publishPost', {}).get('post', {}).get('title')
  postslug = data.get('publishPost', {}).get('post', {}).get('slug')
  postsubtitle = data.get('publishPost', {}).get('post', {}).get('subtitle')
  table_data.append([postid, posttitle, postslug, postsubtitle])

  headers = ["id", "title", "slug", "subtitle"]
  # Display the table
  print(tabulate(table_data, headers=headers, tablefmt="grid"))
 
