import arcade
from config import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, CHARACTER_SCALING, TILE_SCALING

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

    def setup(self):
        # create Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        
        # Player sprites
        image_source = ':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png'
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Wall sprites
        for x in range(0, SCREEN_WIDTH+64, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            self.wall_list.append(wall)
            wall.center_y = 32

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)


    def on_draw(self):
        self.clear()

        self.player_list.draw()
        self.wall_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()