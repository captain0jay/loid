import argparse
import os
import sys
from getpass import getpass

import keyring
from rich.console import Console

from loid import __version__
from loid.constants.informations import APPLICATION_DESCRIPTION
from loid.constants.informations import EPILOG_DESCRIPTION
from loid.constants.informations import INSTALLATION_GUIDE
from loid.constants.informations import VERSION_INFO
from loid.scripts.listdrafts import list_drafts
from loid.scripts.createfile import create_md_file
from loid.scripts.texteditor import openeditor
from loid.middlewares.hashnode import publishdraftmain
from loid.middlewares.hashnode import getpublicationposts
from loid.middlewares.hashnode import publishonlinedraftmain
from loid.middlewares.hashnode import listonlinedraftsmain
from loid.middlewares.hashnode import readdraft
from loid.middlewares.hashnode import readpost
from loid.middlewares.hashnode import copydraftmain
from loid.middlewares.hashnode import feedmain
from loid.constants.services import KEYRING_SERVICE_NAME
from loid.exceptions.system import KeyringIssue
from loid.exceptions.system import BrokenCredentials
from loid.constants.system import BLOG_DOMAIN

parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION + '\n\r\n\r' + INSTALLATION_GUIDE,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog='loid',
)

parser.add_argument(
    'command',
    nargs=1,
    choices=['get','open','publish','create','publication','publishonlinedraft','readDraft','readPost','copydraft'],  # Specify valid choices for the 'command'
    help='Special commands',
)

parser.add_argument(
    '--version',
    action='version',
    version=VERSION_INFO.format(__version__),
)

parser.add_argument(
    '--auth',
    action='store_true',
    help='Set your Personal Auth Token',
)

parser.add_argument(
    '--drafts',
    action='store_true',
    help='Get your drafts',
)

parser.add_argument(
    '--feed',
    action='store_true',
    help='Your hashnode feed',
)

parser.add_argument(
    '--listonlinedrafts',
    action='store_true',
    help='Online drafts list',
)

parser.add_argument(
    'filename',
    nargs='?',  # Make the filename optional
    help='Argument to be passed after command',
)

def main():
    args = parser.parse_args()
    console = Console()

    if args.auth:
        blog_domain = os.environ.get('BLOG_DOMAIN')
        auth_token = getpass(f'Personal Access Token: ')
        try:
            keyring.set_password(
                service_name=KEYRING_SERVICE_NAME.lower(),
                username=blog_domain,
                password=auth_token,
            )
        except Exception as _:
            raise KeyringIssue(
                'There is something wrong with your OS keyring system. Make sure you have right access to run loid '
                'on your system. '
            )
        console.print(f'Personal Access Token set successfully!')

    credentials = keyring.get_credential(
        service_name=KEYRING_SERVICE_NAME.lower(),
        username = os.environ.get('BLOG_DOMAIN')
    )

    if not credentials:
        raise BrokenCredentials(
            f'Make sure you have set your {BLOG_DOMAIN} and Personal Access Token via --auth.'
        )
    
    if args.command:
        # Handle 'show' command
        command = args.command[0]
        if command == 'get':
            print('Fetching...')
        elif command == 'open':
            if args.filename:
                openeditor(args.filename)
            else:
                print('Error: Missing filename for the "open" command.')
        
        elif command == 'create':
            if args.filename:
                create_md_file(args.filename)
            else:
                print('Error: Missing filename for the "create" command.')

        elif command == 'publish':
            if args.filename:
                publishdraftmain(args.filename)
            else:
                print('Error: Missing filename for the "publish" command.')

        elif command == 'publication':
            if args.filename:
                getpublicationposts(args.filename)
            else:
                print('Error: Missing publication url for the "publication" command.')

        elif command == 'publishonlinedraft':
            if args.filename:
                publishonlinedraftmain(args.filename)
            else:
                print('Error: Missing draftid for the "publishonlinedraft" command.')

        elif command == 'readDraft':
            if args.filename:
                readdraft(args.filename)
            else:
                print('Error: Missing draftid for the "readDraft" command.')

        elif command == 'readPost':
            if args.filename:
                readpost(args.filename)
            else:
                print('Error: Missing postid for the "readPost" command.')

        elif command == 'copydraft':
            if args.filename:
                copydraftmain(args.filename)
            else:
                print('Error: Missing draftid for the "copydraft" command.')

        else:
            print(f"{args.command[0]} command is not in the directory please try another command!")

    if args.drafts:
        list_drafts()
        
    if args.feed:
        feedmain()

    if args.listonlinedrafts:
        listonlinedraftsmain()


    return 0

if __name__ == "__main__":
    sys.exit(main())