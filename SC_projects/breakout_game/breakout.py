"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        # update
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            elif lives < 0:
                score_label = GLabel('Game over')
                score_label.font = '-40'
                score_label.color = 'Red'
                graphics.window.add(score_label, x=(graphics.window.width-score_label.width)/2,
                                    y=(graphics.window.height/2))
                break
        if graphics.bricks_num == 0:
            score_label = GLabel('Congratulation!')
            score_label.font = '-40'
            score_label.color = 'Blue'
            graphics.window.add(score_label, x=(graphics.window.width - score_label.width) / 2,
                                y=(graphics.window.height / 2))
            graphics.window.remove(graphics.ball)
            break

        # check
        while graphics.ball.y < graphics.window.height:
            graphics.ball.move(graphics.get_vx(), graphics.get_vy())
            graphics.check_ball()
            # 判斷球是否超過window左邊或右邊
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -graphics.get_vx()
                graphics.set_new_vx(vx)
            # 判斷球是否超過window上方
            if graphics.ball.y <= 0:
                vy = -graphics.get_vy()
                graphics.set_new_vy(vy)
            # pause
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
