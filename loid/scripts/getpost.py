import requests
import json
from loid.scripts.draftpostviewer import openviewer

def getpost(api_url, headers, postid):
#-----------------publish draft-------------------------------

  mutation = """
  query Post($id: ID!) {
    post(id: $id) {
      id
      slug
      title
      subtitle
      tags {
        id
        name
        slug
        logo
        tagline
      }
      content {
        markdown
        html
        text
      }
    }
  }
  """

  input_data = {
      "id": postid
  }

  # Send the request
  first_response = requests.post(api_url, json={"query": mutation, "variables": input_data}, headers=headers)

  # Parse the response
  new_result = json.loads(first_response.text)
  # Access the data from the result
  data = new_result.get('data', {})
  postid = data.get('post', {}).get('id')
  posttitle = data.get('post', {}).get('title')
  postslug = data.get('post', {}).get('slug')
  postsubtitle = data.get('post', {}).get('subtitle')
  postcontent = data.get('post', {}).get('content',{}).get('markdown')

  formatted_string = f"""
    id: {postid}
    title: {posttitle}
    subtitle: {postsubtitle}
    slug: {postslug}
    info:  Press 'q' to exit


    {postcontent}
  """
  openviewer(formatted_string)