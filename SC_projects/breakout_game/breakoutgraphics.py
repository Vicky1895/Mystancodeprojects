"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
switch = False
paddle_count = 0
score = 0
score_label = GLabel('Score=>'+str(score))


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width - ball_radius * 2) / 2,
                          y=(self.window.height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)
        score_label.font = '-20'
        self.window.add(score_label, x=0, y=window_height - score_label.height)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                if i < 2:
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 2 <= i <= 3:
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 4 <= i <= 5:
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 6 <= i <= 7:
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif 8 <= i <= 9:
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.bricks = self.window.add(self.brick, x=brick_spacing * j + brick_width * j,
                                              y=brick_offset + brick_spacing * i + brick_height * i)
        self.bricks_num = brick_rows * brick_cols
        self.r = ball_radius

    def paddle_move(self, event):  # 板子移動
        if event.x - self.paddle.width / 2 >= 0 and event.x + self.paddle.width / 2 <= self.window.width:
            self.paddle.x = event.x - self.paddle.width / 2

    def set_ball_velocity(self, event):  # 設定球速度
        global switch
        if not switch:
            switch = True
            if switch:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def get_vx(self):  # 取得x方向移動速度
        return self.__dx

    def get_vy(self):  # 取得y方向移動速度
        return self.__dy

    def set_new_vx(self, new_vx):  # 設定新的x方向移動速度
        self.__dx = new_vx

    def set_new_vy(self, new_vy):  # 設定新的y方向移動速度
        self.__dy = new_vy

    def reset_ball(self):  # 讓球回到起始位置
        global switch
        self.ball = GOval(self.r * 2, self.r * 2, x=(self.window.width - self.r * 2) / 2,
                          y=(self.window.height - self.r * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)
        switch = False
        self.__dx = 0
        self.__dy = 0

    def check_ball(self):  # 判斷球是否有碰到磚塊或是板子
        global paddle_count, score
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x + 2 * self.r, self.ball.y)
        obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.r)
        obj_4 = self.window.get_object_at(self.ball.x + 2 * self.r, self.ball.y + 2 * self.r)
        if obj_1 is not None and obj_1 is not score_label:
            if obj_1 is self.paddle:  # 判斷球是否有碰到板子
                self.__dy = -self.__dy
                paddle_count += 1
            else:  # 判斷球不是碰到板子，那就是碰到磚塊(self.brick只會最後一個brick)
                self.window.remove(obj_1)
                self.bricks_num -= 1
                score += 1
                self.__dy = -self.__dy
        elif obj_2 is not None and obj_2 is not score_label:
            if obj_2 is self.paddle:
                self.__dy = -self.__dy
                paddle_count += 1
            else:
                self.window.remove(obj_2)
                self.bricks_num -= 1
                score += 1
                self.__dy = -self.__dy
        elif obj_3 is not None and obj_3 is not score_label:
            if obj_3 is self.paddle:
                self.__dy = -self.__dy
                paddle_count += 1
            else:
                self.window.remove(obj_3)
                self.bricks_num -= 1
                score += 1
                self.__dy = -self.__dy
        elif obj_4 is not None and obj_4 is not score_label:
            if obj_4 is self.paddle:
                self.__dy = -self.__dy
                paddle_count += 1
            else:
                self.window.remove(obj_4)
                self.bricks_num -= 1
                score += 1
                self.__dy = -self.__dy
        if paddle_count >= 1:  # 球碰到板子時，將球移到板子上方反彈，避免反彈後球仍落在板子內
            self.ball.move(0, self.paddle.y-self.ball.y-self.ball.height)
            paddle_count = 0
        score_label.text = 'Score=>' + str(score)



