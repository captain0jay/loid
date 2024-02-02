#!/bin/python3
import curses
import sys
import os

def main(stdscr,filename):
    s = curses.initscr()
    s.nodelay(1)
    curses.noecho()
    curses.raw()
    s.keypad(1)

    b = []

    md_filename = filename + ".md"


    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)

    # Specify the relative path for the drafts folder
    drafts_folder = os.path.join(current_dir, "../drafts")

    # Create the drafts folder if it doesn't exist
    if not os.path.exists(drafts_folder):
        os.makedirs(drafts_folder)

    # Construct the full path for the Markdown file
    md_filepath = os.path.join(drafts_folder, md_filename)
    
    src = md_filepath

    R, C = s.getmaxyx()
    x, y, r, c = [0] * 4

    if len(sys.argv) == 2:
        src = sys.argv[1]

    try:
        # Read the initial content from a file
        with open(src) as f:
            cont = f.read().split('\n')
            cont = cont[:-1] if len(cont) > 1 else cont
            for rw in cont:
                b.append([ord(c) for c in rw])
    except FileNotFoundError:
        # Use default initial content if the file is not found
        b.append([])

    while True:
        s.move(0, 0)

        if r < y:
            y = r
        if r >= y + R:
            y = r - R + 1
        if c < x:
            x = c
        if c >= x + C:
            x = c - C + 1

        for rw in range(R):
            brw = rw + y
            for cl in range(C):
                bcl = cl + x
                try:
                    s.addch(rw, cl, b[brw][bcl])
                except:
                    pass
            s.clrtoeol()
            try:
                s.addch('\n')
            except:
                pass

        curses.curs_set(0)
        s.move(r - y, c - x)
        curses.curs_set(1)
        s.refresh()
        ch = -1
        while ch == -1:
            ch = s.getch()

        if ch != ((ch) & 0x1f) and ch < 128:
            b[r].insert(c, ch)
            c += 1
        elif chr(ch) in '\n\r':
            l = b[r][c:]
            b[r] = b[r][:c]
            r += 1
            c = 0
            b.insert(r, [] + l)
        elif ch in [8, 263]:
            if c:
                c -= 1
                del b[r][c]
            elif r:
                l = b[r][c:]
                del b[r]
                r -= 1
                c = len(b[r])
                b[r] += l
        elif ch == curses.KEY_LEFT:
            if c != 0:
                c -= 1
            elif r > 0:
                r -= 1
                c = len(b[r])
        elif ch == curses.KEY_RIGHT:
            if c < len(b[r]):
                c += 1
            elif r < len(b) - 1:
                r += 1
                c = 0
        elif ch == curses.KEY_UP and r != 0:
            r -= 1
        elif ch == curses.KEY_DOWN and r < len(b) - 1:
            r += 1

        rw = b[r] if r < len(b) else None
        rwlen = len(rw) if rw is not None else 0
        if c > rwlen:
            c = rwlen

        if ch == (ord('q') & 0x1f):
            sys.exit()
        elif ch == (ord('s') & 0x1f):
            cont = ''
            for l in b:
                cont += ''.join([chr(c) for c in l]) + '\n'
            with open(src, 'w') as f:
                f.write(cont)

def openeditor(filename):
    curses.wrapper(lambda stdscr: main(stdscr, filename))
