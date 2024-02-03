import curses
from tabulate import tabulate
from loid.scripts.getpost import getpost
from loid.constants.services import KEYRING_SERVICE_NAME
import keyring
import os

credentials = keyring.get_credential(
    service_name=KEYRING_SERVICE_NAME.lower(),
    username=os.environ.get('BLOG_DOMAIN')
)

if credentials is None:
    print("Credential not found.")
else:
    api_url = ' https://gql.hashnode.com'  # Replace with the actual API endpoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': credentials.password,  # Include authorization if required
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
        curses.curs_set(0)  # Hide the cursor
        stdscr.clear()
        stdscr.refresh()

        # Get the updated terminal size after entering curses mode
        num_lines, num_cols = stdscr.getmaxyx()

        if num_lines < 13 or num_cols < 30:  # Check if terminal size is sufficient
            stdscr.clear()
            stdscr.addstr(0, 0, "To choose and read posts Please resize your terminal! (to at least 13 lines and 30 columns). \n To exit this message presss 'Q'")
            stdscr.refresh()
            stdscr.getch()
            return

        selected_index = 2  # Start from the second row to select the title
        start_row = 0

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
                if selected_index > start_row + num_lines - 3:
                    start_row += 1

        selected_id = table_data[selected_index - 2][0]
        getpost(api_url, headers, selected_id)
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting

        return selected_id

    wrapper_result = curses.wrapper(main)
    return wrapper_result

# Example usage
# print_tablemain(...)  # Provide the appropriate table_data when calling the function
