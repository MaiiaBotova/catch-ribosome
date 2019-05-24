# buttons functions

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def new_game():
    filewin = Toplevel(root)
    button = Button(filewin, text="Start new game")
    button.pack()

def load_game():
    filewin = Toplevel(root)
    button = Button(filewin, text="Load game")
    button.pack()

def save():
    filewin = Toplevel(root)
    button = Button(filewin, text="Save progress")
    button.pack()

def close_window():
    filewin = Toplevel(root)
    button = Button(filewin, text="Close window")
    button.pack()






# Helper functions
# def create_block():
#     """ Creates an apple to be eaten """
#     global BLOCK
#     posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
#     posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
#     BLOCK = c.create_oval(posx, posy,
#                           posx + SEG_SIZE, posy + SEG_SIZE,
#                           fill="red")


# def main(IN_GAME):
#     """ Handles game process """
#     # global IN_GAME
#     if IN_GAME:
#         s.move()
#         head_coords = c.coords(s.segments[-1].instance)
#         x1, y1, x2, y2 = head_coords
#         # Check for collision with gamefield edges
#         if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
#             IN_GAME = False
#         # Eating apples
#         elif head_coords == c.coords(BLOCK):
#             s.add_segment()
#             c.delete(BLOCK)
#             create_block()
#         # Self-eating
#         else:
#             for index in range(len(s.segments) - 1):
#                 if head_coords == c.coords(s.segments[index].instance):
#                     IN_GAME = False
#         root.after(100, main)
#     # Not IN_GAME -> stop game and print message
#     else:
#         c.create_text(WIDTH / 2, HEIGHT / 2,
#                       text="GAME OVER!",
#                       font="Arial 20",
#                       fill="red")