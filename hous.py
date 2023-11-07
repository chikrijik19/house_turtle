import turtle

def draw_house(
        x=0,
        y=0, 
        base_w=100, 
        base_h=10, 
        base_color='grey', 
        walls_w=90, 
        walls_h=90, 
        walls_color='red', 
        roof_w=100,
        roof_h=50,
        roof_color='brown',
):
    draw_base(x, y, base_w, base_h, base_color)
    draw_walls()
    draw_roof()



def draw_base(x, y, base_w, base_h, base_color):
    print('рисуем икс в',{x}, 'игрик в ', {y},'цвет в', {base_color})
    draw_rectangle(x, y, base_w, base_h, base_color)



def draw_walls():
    print('рисуем стены')



def draw_roof():
    print('рисоем крышу')



def draw_rectangle(x, y, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.end_fill()


draw_house()
turtle.done()