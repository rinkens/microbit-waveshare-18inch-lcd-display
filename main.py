def on_button_pressed_a():
    global colorIndex
    colorIndex += 1
    if colorIndex >= len(color):
        colorIndex = 0
    basic.show_number(colorIndex)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global xpos, ypos
    LCD1IN8.LCD_Clear()
    xpos = 80
    ypos = 64
input.on_button_pressed(Button.AB, on_button_pressed_ab)

colorIndex = 0
ypos = 0
xpos = 0
color: List[number] = []
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
basic.show_icon(IconNames.SQUARE)
color = [LCD1IN8.Get_Color(LCD_COLOR.RED),
    LCD1IN8.Get_Color(LCD_COLOR.MAGENTA),
    LCD1IN8.Get_Color(LCD_COLOR.YELLOW),
    LCD1IN8.Get_Color(LCD_COLOR.GREEN),
    LCD1IN8.Get_Color(LCD_COLOR.BLUE),
    LCD1IN8.Get_Color(LCD_COLOR.CYAN),
    LCD1IN8.Get_Color(LCD_COLOR.BLACK)]
xpos = 80
ypos = 64

def on_forever():
    global xpos, ypos
    LCD1IN8.draw_point(xpos, ypos, color[colorIndex], DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.LCD_DisplayWindows(xpos - 3, ypos - 3, xpos + 3, ypos + 3)
    if input.acceleration(Dimension.X) >= -70 and input.acceleration(Dimension.X) <= 70 and (input.acceleration(Dimension.Y) >= -70 and input.acceleration(Dimension.Y) <= 70):
        pass
    else:
        if input.acceleration(Dimension.X) < -70 and xpos > 0:
            xpos += -1
        if input.acceleration(Dimension.X) > 70 and xpos < 159:
            xpos += 1
        if input.acceleration(Dimension.Y) < -70 and ypos > 0:
            ypos += -1
        if input.acceleration(Dimension.Y) > 70 and xpos < 127:
            ypos += 1
basic.forever(on_forever)
