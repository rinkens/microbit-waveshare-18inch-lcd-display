input.onButtonPressed(Button.A, function () {
    colorIndex += 1
    if (colorIndex >= color.length) {
        colorIndex = 0
    }
    basic.showNumber(colorIndex)
})
input.onButtonPressed(Button.AB, function () {
    LCD1IN8.LCD_Clear()
    xpos = 80
    ypos = 64
})
let colorIndex = 0
let ypos = 0
let xpos = 0
let color: number[] = []
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
basic.showIcon(IconNames.Square)
color = [
LCD1IN8.Get_Color(LCD_COLOR.RED),
LCD1IN8.Get_Color(LCD_COLOR.MAGENTA),
LCD1IN8.Get_Color(LCD_COLOR.YELLOW),
LCD1IN8.Get_Color(LCD_COLOR.GREEN),
LCD1IN8.Get_Color(LCD_COLOR.BLUE),
LCD1IN8.Get_Color(LCD_COLOR.CYAN),
LCD1IN8.Get_Color(LCD_COLOR.BLACK)
]
xpos = 80
ypos = 64
basic.forever(function () {
    LCD1IN8.DrawPoint(
    xpos,
    ypos,
    color[colorIndex],
    DOT_PIXEL.DOT_PIXEL_1
    )
    LCD1IN8.LCD_DisplayWindows(
    xpos - 3,
    ypos - 3,
    xpos + 3,
    ypos + 3
    )
    if (input.acceleration(Dimension.X) >= -70 && input.acceleration(Dimension.X) <= 70 && (input.acceleration(Dimension.Y) >= -70 && input.acceleration(Dimension.Y) <= 70)) {
    	
    } else {
        if (input.acceleration(Dimension.X) < -70 && xpos > 0) {
            xpos += -1
        }
        if (input.acceleration(Dimension.X) > 70 && xpos < 159) {
            xpos += 1
        }
        if (input.acceleration(Dimension.Y) < -70 && ypos > 0) {
            ypos += -1
        }
        if (input.acceleration(Dimension.Y) > 70 && xpos < 127) {
            ypos += 1
        }
    }
})
