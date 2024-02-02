import requests
import json
from tabulate import tabulate

def publishonlinedraft(api_url,headers,draftid):
  #-----------------publish draft-------------------------------
  mutation = """
  mutation PublishDraft($input: PublishDraftInput!) {
    publishDraft(input: $input) {
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
      "draftId": draftid
  }

  # Send the request
  first_response = requests.post(api_url, json={"query": mutation, "variables": {"input" : input_data}}, headers=headers)

  # Parse the response
  new_result = json.loads(first_response.text)
  # Access the data from the result
  data = new_result.get('data', {})
  table_data = []
# Define headers for the table
  postid = data.get('publishDraft', {}).get('post', {}).get('id')
  posttitle = data.get('publishDraft', {}).get('post', {}).get('title')
  postslug = data.get('publishDraft', {}).get('post', {}).get('slug')
  postsubtitle = data.get('publishDraft', {}).get('post', {}).get('subtitle')
  table_data.append([postid, posttitle, postslug, postsubtitle])

  headers = ["id", "title", "slug", "subtitle"]
  # Display the table
  print(tabulate(table_data, headers=headers, tablefmt="grid"))