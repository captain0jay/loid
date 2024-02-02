import requests
import json
from loid.scripts.draftpostviewer import openviewer
def getdraft(api_url, headers,draftid):
#-----------------publish draft-------------------------------
  mutation = """
  query Draft($id: ObjectId!) {
    draft(id: $id) {
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
      "id": draftid
  }

  # Send the request
  first_response = requests.post(api_url, json={"query": mutation, "variables": input_data}, headers=headers)

  # Parse the response
  new_result = json.loads(first_response.text)
  # Access the data from the result
  data = new_result.get('data', {})

  postid = data.get('draft', {}).get('id')
  posttitle = data.get('draft', {}).get('title')
  postslug = data.get('draft', {}).get('slug')
  postsubtitle = data.get('draft', {}).get('subtitle')
  postcontent = data.get('draft', {}).get('content')

  formatted_string = f"""
    id: {postid}
    title: {posttitle}
    subtitle: {postsubtitle}
    slug: {postslug}
    info:  Press 'Ctrl + q' to exit


    {postcontent}
  """
  openviewer(formatted_string)