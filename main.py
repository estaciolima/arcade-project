import arcade
from config import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, CHARACTER_SCALING, TILE_SCALING, PLAYER_MOVEMENT_SPEED

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        # create Scene
        self.scene = arcade.Scene()

        # create Sprite lists
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)
        
        # Player sprites
        image_source = ':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png'
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite('Player', self.player_sprite)

        # Wall sprites
        for x in range(0, SCREEN_WIDTH+64, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite('Walls', wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite('Walls', wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.scene.get_sprite_list('Walls'))


    def on_draw(self):
        self.clear()

        self.scene.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.scene.get_sprite_list('Player').move(0.0, PLAYER_MOVEMENT_SPEED)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.scene.get_sprite_list('Player').move(0.0, -PLAYER_MOVEMENT_SPEED)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.scene.get_sprite_list('Player').move(PLAYER_MOVEMENT_SPEED, 0.0)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.scene.get_sprite_list('Player').move(-PLAYER_MOVEMENT_SPEED, 0.0)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.scene.get_sprite_list('Player').move(0.0, 0.0)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.scene.get_sprite_list('Player').move(0.0, 0.0)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.scene.get_sprite_list('Player').move(0.0, 0.0)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.scene.get_sprite_list('Player').move(0.0, 0.0)

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()