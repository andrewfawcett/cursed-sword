import curses

# https://gist.github.com/claymcleod/b670285f334acd56ad1c

ENTER = 10
ESCAPE = 27

def main():
    curses.wrapper(draw_title)
    curses.wrapper(draw_map)

def draw_menu(stdscr):
    menu_window = curses.newwin(10, 10, 0, 70)
    
    menu = ['Battle', 'Item', 'Save', 'Quit']
    option = 0

    k = 0
    while (k != ENTER):
        menu_window.clear()
        menu_window.border()
        # Dynamically draw menu items
        for num, item in enumerate(menu, start=1):
                        menu_window.addstr(num, 2, item)
        
        # Move cursor
        if k == curses.KEY_DOWN:
            option = option + 1
        elif k == curses.KEY_UP:
            option = option - 1
        option = option % len(menu)

        menu_window.addch(option + 1, 1, '>')
        
        # Draw window and get key
        menu_window.refresh()
        k = stdscr.getch()
    
    if option == 0:
        battle(stdscr)
    elif option == 3:
        return False


def battle(stdscr):
    battle_window = curses.newwin(24, 48)
    
    k = 0
    while (k != ESCAPE):
        battle_window.clear()
        battle_window.border()
        battle_window.refresh()
        k = stdscr.getch()

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
        curses.curs_set(0) # Disable cursor

        stdscr.clear()
        stdscr.refresh()
        
        PLAY=True
        while (PLAY):
            stdscr.clear()
            stdscr.border()
            height, width = stdscr.getmaxyx()

            if k == curses.KEY_DOWN:
                cursor_y = cursor_y + 1
            elif k == curses.KEY_UP:
                cursor_y = cursor_y - 1
            elif k == curses.KEY_RIGHT:
                cursor_x = cursor_x + 1
            elif k == curses.KEY_LEFT:
                cursor_x = cursor_x - 1
            elif k == ENTER:
                PLAY == draw_menu(stdscr)
            
            if ((cursor_y + cursor_x) % 2 == 0):
                charcter = '<>'
            else:
                charcter = '><'
            stdscr.addstr(cursor_y, cursor_x, charcter)


            #DEBUG
            # stdscr.addstr(80, 0, str(PLAY))
            stdscr.refresh()
            k = stdscr.getch()


    

def draw_title(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.clear()
    stdscr.refresh()

    while (k != ENTER):
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