import arcade
from config import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMARANTH)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()