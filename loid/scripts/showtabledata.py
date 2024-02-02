import curses
from tabulate import tabulate
from loid.scripts.getpost import getpost
from loid.constants.services import KEYRING_SERVICE_NAME
import keyring
import os

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

def print_tablemain(table_data):
    def print_table(stdscr, table, selected_index, start_row):
        stdscr.clear()
        stdscr.addstr(0, 0, "Use arrow keys to navigate. Press Enter to select.")

        max_rows = min(curses.LINES - 3, len(table))
        for i, row in enumerate(table[start_row:start_row + max_rows], start=2):
            x = 4
            y = i
            if i == selected_index:
                stdscr.addstr(y, x, f"-> {row[1]}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"   {row[1]}")

        stdscr.addstr(10, 0, tabulate(table[start_row:start_row + max_rows],
                                      headers=["ID", "Title", "Views"], tablefmt="grid"))
        stdscr.refresh()

    def main(stdscr):
        selected_index = 2  # Start from the second row to select the title
        start_row = 0

        curses.curs_set(0)  # Hide the cursor
        stdscr.clear()
        stdscr.refresh()

        key = 0
        while key != ord('\n'):  # Enter key
            print_table(stdscr, table_data, selected_index, start_row)
            key = stdscr.getch()

            if key == curses.KEY_UP and selected_index > 2:
                selected_index -= 1
                if start_row > 0 and selected_index < start_row + 2:
                    start_row -= 1
            elif key == curses.KEY_DOWN and selected_index < len(table_data) + 1:
                selected_index += 1
                if selected_index > start_row + curses.LINES - 3:
                    start_row += 1

        selected_id = table_data[selected_index - 2][0]
        getpost(api_url, headers,selected_id)
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting

        return selected_id

    return curses.wrapper(main)

