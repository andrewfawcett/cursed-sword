import curses

# https://gist.github.com/claymcleod/b670285f334acd56ad1c

ENTER = 10


def main():
    curses.wrapper(draw_title)
    curses.wrapper(draw_map)

def draw_map(stdscr):
        stdscr.clear()
        # height, width = stdscr.getmaxyx()
        # Forcing a fixed width game
        height = 80
        width = 24

        k = 0
        cursor_x = 1
        cursor_y = 1

        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        stdscr.clear()
        stdscr.refresh()

        option = 0
        menu = ['Battle', 'Item', 'Save', 'Quit']
        PLAY=True
        while (PLAY):
            while (k != ENTER):
                stdscr.clear()
                height, width = stdscr.getmaxyx()

                if k == curses.KEY_DOWN:
                    option = option + 1
                elif k == curses.KEY_UP:
                    option = option - 1

                option = option % len(menu)

                for num, item in enumerate(menu, start=0):
                    stdscr.addstr(num, 1, item)
                # stdscr.addstr(0, len(statusbar), " " * (width - len(statusbar) - 1))
                

                console = f'Key: {k} | Option: {option}'[:width-1]
                stdscr.addstr(height-1, 0, console)

                stdscr.move(option, 0)

                stdscr.refresh()
                k = stdscr.getch()
            if option == 3:
                PLAY = False


    

def draw_title(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.clear()
    stdscr.refresh()

    while (k != ord('q')):
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "Sword Adventure"[:width-1]
        subtitle = "Written by Andrew Fawcett"[:width-1]
        keystr = f"Last key pressed: {k}"[:width-1]
        statusbar = f"[Q]uit"
        if k == 0:
            keystr = "Start..."[:width-1]

        # Centering caclculation
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Redering status bar
        stdscr.addstr(height-1, 0, statusbar)
        stdscr.addstr(height-1, len(statusbar), " " * (width - len(statusbar) - 1))

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Print the rest of the text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)



        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
    

if __name__ == '__main__':
    main()