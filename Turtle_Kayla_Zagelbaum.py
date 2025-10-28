import turtle as T
import random

CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40


SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}


THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}

# ---------- tiny turtle helpers (provided) ----------

def move_to(x,y):
    '''
    x - position on x coordinate axis
    y - position on y coordinate axis
    '''
    T.penup(); T.goto(x, y); T.pendown()


def draw_line(x1, y1, x2, y2):
    '''
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis
       
       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
       '''
    move_to(x1, y1); T.pendown()
    T.goto(x2, y2); T.penup()


def fill_rect_center(cx, cy, w, h, color):
    '''
    cx - center of rectangle x coordinate 
    cy - center of rectangle y coordinate 
    w - width of rectangle 
    h - height of rectangle 
    color - color of rectangle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w/2, cy + h/2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()


def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.
    
    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    
    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).
    
    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """

    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()
    

def fill_circle_center(cx, cy, r, color):
    '''
    a circle is defined by 
    cx - the center of your circle, x coordinate 
    cy - center of your circle, y coordinate 
    r - radius 
    color - color of circle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()
    

# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
     allowed_set = set(allowed)

     # validates that the integer is one of the choices, reprompts if not
     while True:
        try:
            choice = int(input(prompt))
            if choice in allowed_set:
                return choice
            else:
                print("please enter a valid option")
        except ValueError:
             print("please enter a valid option")
             
         
def ask_choice_str(prompt, allowed):
    allowed_lower = [a.lower() for a in allowed]   # converting to lower case all in allowed list
    allowed_set = set(allowed)

    # validates that the word is one of the choices, reprompts if not
    while True:
        try:
            choice = str(input(prompt).strip().lower())
            if choice in allowed_set:
                return choice
            else:
                print("please enter a valid option")
        except ValueError:
            print("please enter a valid option")
            

# ---------- TODO: draw_roads ----------            
"""
Draw roads: This function will:
    1) define function
    2) define constants
    3) set pencolor and pensize
    4) draw horizontal lines for each row based on user input using a for loop
    5) draw verticle lines for each column based on user input using a for loop

"""

def draw_roads(cols, rows, cell_w, cell_h):


    # constants
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2

    # set pencolor and pensize
    T.pencolor("black")
    T.pensize(5)

    # draw horizontal line for each row, based on user input
    for r in range(1, rows):
        y =  CANVAS_H/2 - TOP_MARGIN - r * cell_h
        draw_line(left_x, y , right_x, y)

    # draw verticle lines for each column, based on user input
    for c in range(1, cols):
        draw_line(left_x + c * cell_w, top_y, left_x + c * cell_w, bot_y)
  


# ---------- TODO: draw_house_centered ----------
"""
Draw house: This function will:
    1) define function
    2) draw body = rectangle centered in cell
    3) draw roof = if triangle, draw trinagle; otherwise draw thin flat rectangle
    4) draw door = small rectangle centered on x = cx
"""


def draw_house_centered(cx, cy, size_key, theme_key, roof_style):

    
    w,h = SIZES[size_key]
    colors = THEMES[theme_key]

    # draw the body of the house
    body_c = colors["body"]                       
    fill_rect_center(cx, cy, w, h, body_c)
    
    # draw the roof of the house
    # if the user selects triangle:
    if roof_style == "triangle":
        roof_c = colors["roof"]
        p1 = cx - w/2, cy + h/2
        p2 = cx, cy + h
        p3 = cx + w/2, cy + h/2
        fill_triangle(p1, p2, p3, roof_c)

    # if the user selects flat:
    else:
        roof_c = colors["roof"]
        fill_rect_center(cx, cy + (h/3), w, h/3, roof_c)


    # draw a door
    door_c = colors["door"]
    fill_rect_center(cx, cy - (h * 0.25) , w/4, h/2, door_c )
    


# ---------- TODO: draw_tree_near ----------

"""
Draw tree: This function will:
    1) define draw_tree_near
    2) set w and h
    3) set trunk size ratios
    4) randomize which side the tree goes on
    5) draw trunk using fill_rect_center
    6) draw canopy using fill_circle_center

"""

def draw_tree_near(cx, cy, size_key):

    
    # constants
    w, h = SIZES[size_key]
    tw, th = w*0.10, h*0.40    # trunk size ratios
    side = random.choice([-1, 1])     # place to left or right of the house randomly
    tx = cx + side * (w+0.45)
    ty = cy - h*0.5 + th/2

    # draws the tree
    fill_rect_center(tx, ty, tw, th, "brown")   # draws the trunk
    fill_circle_center(tx, ty + 40, th/1.5, "green")    # draws the canopy



# ---------- TODO: draw_village (orchestration) ----------
"""
draw village: this function will:
    1) define draw village
    2) set constants
    3) call draw roads
    4) use a nested loop "for r: for c:" to:
        A) compute center of the cell
        B) call draw house
        C) call draw tree
    5) ask for sun [y/n]
        A) draw sun if answer is yes using fill_circle_center
"""

def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):


    # constants
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2

    # call draw roads
    draw_roads(cols, rows, cell_w, cell_h)


    # draws a house and tree in each cell
    for r in range(rows):
        for c in range(cols):
            # compute the center of the cell
            cx = left_x + (c + 0.5) * cell_w
            cy = top_y - (r + 0.5) * cell_h
            # draw the house and tree
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            draw_tree_near(cx, cy, size_key)
    
    # if the user chooses to have a sun, draw sun
    if sun_flag == 'y':
        r = 35
        cx = CANVAS_W/2 - r - 20
        cy = CANVAS_H/2 - r - 20
        fill_circle_center(cx, cy, r, "yellow")


# ---------- main ----------
"""
Main: This function will:
    1) print welcome message
    2) ask for:
        columns
        rows
        house size
        color theme
        roof style
        sun y/n
    3) set up window
    4) call draw village with inputs
    5) finalize
    6) call main
"""

def main():


    # collect user input for columns, rows, size, color theme, roof style, and sun
    print("Welcome to Turtle Village — Lite!")
    cols = ask_choice_int("How many houses per row?[2, 3]", [2, 3])
    rows = ask_choice_int("How many rows?[2]", [2])  # you may change to [2, 3]
    size_key = ask_choice_str("House size: [S, M, L]", ["s","m","l"]).strip().lower()
    theme_key = ask_choice_str("Color theme[pastel, primary]", ["pastel","primary"])
    roof_style = ask_choice_str("Roof type[triangle, flat]", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun[y / n]?", ["y","n"]).lower()

    
    # window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    # defines cell width and cell height given the user input
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # call draw village with arguments
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)

  
    # finalize
    T.tracer(True); T.hideturtle(); T.done()

    
# calls completed function
if __name__ == "__main__":
    main()

        
         

    

    

    
















































    
