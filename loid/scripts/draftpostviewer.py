import curses

def main(stdscr, content):
    curses.curs_set(0)
    stdscr.clear()

    R, C = stdscr.getmaxyx()
    start_row = 0

    while True:
        stdscr.clear()

        lines = content.split('\n')
        for i, line in enumerate(lines[start_row:start_row + R]):
            stdscr.addstr(i, 0, line[:C-1])

        stdscr.refresh()

        ch = stdscr.getch()
        if ch == ord('q') or ch == curses.KEY_EXIT:  # Check for 'q' or exit key
            break
        elif ch == curses.KEY_UP and start_row > 0:
            start_row -= 1
        elif ch == curses.KEY_DOWN and start_row < len(lines) - R:
            start_row += 1


# Example usage
def openviewer(content_to_view):
    curses.wrapper(lambda stdscr: main(stdscr, content_to_view))