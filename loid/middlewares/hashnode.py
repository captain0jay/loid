import requests
import json
import os
from loid.scripts.publishdraft import publishdraft
from loid.scripts.getdraft import getdraft
from loid.scripts.getpost import getpost
from loid.scripts.getpublication import getpublication
from loid.scripts.listonlinedrafts import listonlinedrafts
from loid.scripts.publishonlinedrafts import publishonlinedraft
from loid.scripts.getfeed import getfeed
from loid.constants.services import KEYRING_SERVICE_NAME
import keyring

credentials = keyring.get_credential(
    service_name=KEYRING_SERVICE_NAME.lower(),
    username = os.environ.get('BLOG_DOMAIN')
)

if credentials is None:
    print("Credential not found.")
else:
    api_url = ' https://gql.hashnode.com'  # Replace with the actual API endpoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': credentials.password,# Include authorization if required
    }

    host_name = credentials.username

def convert_to_slug(title):
    slug = title.lower()
    slug = slug.replace(" ", "-")
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    return slug

def publishdraftmain(filename):
    print("Publishing...")
    # Get input from the user
    maintitle = input("Enter the title: ")
    mainslug = convert_to_slug(maintitle)
    posttag = input("Enter tag(single tag supported as of now): ")
    postslugnew = convert_to_slug(posttag)

    # Get the directory of the current script
    md_filename= filename + ".md"
    current_dir = os.path.dirname(__file__)
    drafts_folder = os.path.join(current_dir, "../drafts")
    if not os.path.exists(drafts_folder):
        os.makedirs(drafts_folder)
        
    file_path = os.path.join(drafts_folder, md_filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            file_contents = file.read()

        publishdraft(api_url, headers, file_contents, host_name, maintitle, mainslug,posttag,postslugnew)
    else:
        print(f"File '{file_path}' does not exist.")

def listonlinedraftsmain():
    listonlinedrafts(api_url,headers)

def readdraft(draftid):
    getdraft(api_url, headers,draftid)

def readpost(postid):
    getpost(api_url, headers,postid)

def copydraftmain(draftid):
    print("Publishing...")

def getpublicationposts(pub_host_name):
    getpublication(api_url,headers,pub_host_name)

def publishonlinedraftmain(draftid):
    publishonlinedraft(api_url,headers,draftid)

def feedmain():
    strnumofposts = input("How many posts do you want?: ")
    numofposts = int(strnumofposts)
    getfeed(api_url,headers,numofposts)

def commentonposts():
    print("Publishing...")

def getllmanswer():
    print("Publishing...")