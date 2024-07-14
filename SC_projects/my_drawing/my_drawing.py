"""
File: my_drawing.py
Name: Vicky
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My favorite animation
    Totoro is a main character of the famous movie.
    He let us gain the courage and hope to face the difficulty.
    """
    window = GWindow(width=650, height=560, title='my_drawing')
    body = GOval(300, 410, x=200, y=150)
    body.filled = True
    body.fill_color = 'gray'
    body.color = 'gray'
    window.add(body)
    eye_l = GOval(30, 30, x=280, y=200)
    eye_l.filled = True
    eye_l.fill_color = 'white'
    window.add(eye_l)
    eye_l_point = GOval(10, 10, x=285, y=210)
    eye_l_point.filled = True
    window.add(eye_l_point)
    eye_r = GOval(30, 30, x=390, y=200)
    eye_r.filled = True
    eye_r.fill_color = 'white'
    window.add(eye_r)
    eye_r_point = GOval(10, 10, x=395, y=210)
    eye_r_point.filled = True
    window.add(eye_r_point)
    nose = GOval(25, 8, x=340, y=230)
    nose.filled = True
    window.add(nose)
    abdomen = GOval(270, 268, x=215, y=280)
    abdomen.filled = True
    abdomen.fill_color = 'white'
    window.add(abdomen)
    beard_l_1 = GLine(160, 250, 250, 260)
    window.add(beard_l_1)
    beard_l_2 = GLine(130, 265, 250, 270)
    window.add(beard_l_2)
    beard_l_3 = GLine(160, 285, 250, 280)
    window.add(beard_l_3)
    beard_r_1 = GLine(440, 260, 540, 250)
    window.add(beard_r_1)
    beard_r_2 = GLine(440, 270, 570, 265)
    window.add(beard_r_2)
    beard_r_3 = GLine(440, 280, 540, 285)
    window.add(beard_r_3)
    mouse = GOval(10, 3, x=347, y=260)
    mouse.filled = True
    window.add(mouse)
    ear_r = GOval(40, 120)
    ear_r.filled = True
    ear_r.fill_color = 'gray'
    ear_r.color = 'gray'
    window.add(ear_r, x=250, y=90)
    ear_l = GOval(40, 110)
    ear_l.filled = True
    ear_l.fill_color = 'gray'
    ear_l.color = 'gray'
    window.add(ear_l, x=400, y=90)
    fur_1 = GPolygon()
    fur_1.add_vertex((50, 80))
    fur_1.add_vertex((75, 50))
    fur_1.add_vertex((100, 80))
    fur_1.add_vertex((75, 65))
    fur_1.filled = True
    window.add(fur_1, x=200, y=280)
    fur_2 = GPolygon()
    fur_2.add_vertex((50, 80))
    fur_2.add_vertex((75, 50))
    fur_2.add_vertex((100, 80))
    fur_2.add_vertex((75, 65))
    fur_2.filled = True
    window.add(fur_2, x=280, y=280)
    fur_3 = GPolygon()
    fur_3.add_vertex((50, 80))
    fur_3.add_vertex((75, 50))
    fur_3.add_vertex((100, 80))
    fur_3.add_vertex((75, 65))
    fur_3.filled = True
    window.add(fur_3, x=350, y=280)
    fur_4 = GPolygon()
    fur_4.add_vertex((50, 80))
    fur_4.add_vertex((75, 50))
    fur_4.add_vertex((100, 80))
    fur_4.add_vertex((75, 65))
    fur_4.filled = True
    window.add(fur_4, x=180, y=320)
    fur_5 = GPolygon()
    fur_5.add_vertex((50, 80))
    fur_5.add_vertex((75, 50))
    fur_5.add_vertex((100, 80))
    fur_5.add_vertex((75, 65))
    fur_5.filled = True
    window.add(fur_5, x=240, y=320)
    fur_6 = GPolygon()
    fur_6.add_vertex((50, 80))
    fur_6.add_vertex((75, 50))
    fur_6.add_vertex((100, 80))
    fur_6.add_vertex((75, 65))
    fur_6.filled = True
    window.add(fur_6, x=310, y=320)
    fur_7 = GPolygon()
    fur_7.add_vertex((50, 80))
    fur_7.add_vertex((75, 50))
    fur_7.add_vertex((100, 80))
    fur_7.add_vertex((75, 65))
    fur_7.filled = True
    window.add(fur_7, x=380, y=320)

    station_1 = GOval(100, 100, x=20, y=200)
    station_1.filled = True
    station_1.fill_color = 'darksage'
    window.add(station_1)
    station_2 = GRect(10, 250, x=65, y=300)
    station_2.filled = True
    station_2.fill_color = 'gray'
    window.add(station_2)
    station_3 = GRect(80, 35, x=30, y=525)
    station_3.filled = True
    window.add(station_3)
    label = GLabel('Python', x=35, y=265)
    label.font = '-20'
    label.color = 'gold'
    window.add(label)


if __name__ == '__main__':
    main()
