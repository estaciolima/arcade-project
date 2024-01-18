import arcade
from config import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, CHARACTER_SCALING, TILE_SCALING, PLAYER_MOVEMENT_SPEED
import config

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        #scene
        self.scene = None
        
        # player sprite
        self.player_sprite = None
        
        # physics engine
        self.physics_engine = None
        
        # camera
        self.camera = None
        
        # sounds
        self.collect_coin_sound = None
        self.jump_sound = None

    def setup(self):
        # create Scene
        self.scene = arcade.Scene()

        # create Sprite lists
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)
        self.scene.add_sprite_list('Coins')
        
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

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             gravity_constant=config.GRAVITY,
                                                             walls=self.scene.get_sprite_list('Walls'))
        
        # create camera
        self.camera = arcade.Camera(self.width, self.height)

        # add coins
        for x in range(128, 1250, 256):
            coin_sprite = arcade.Sprite(':resources:images/items/coinGold.png', config.COIN_SCALING)
            coin_sprite.center_x = x
            coin_sprite.center_y = 96
            self.scene.add_sprite('Coins', coin_sprite)

        # load sounds
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin1.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/jump1.wav')

    def on_draw(self):
        self.clear()

        # draw our scene
        self.scene.draw()

        # activate ou camera
        self.camera.use()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - self.camera.viewport_width/2
        screen_center_y = self.player_sprite.center_y - self.camera.viewport_height/2

        screen_center_x = screen_center_x if screen_center_x > 0 else 0
        screen_center_y = screen_center_y if screen_center_y > 0 else 0

        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def collect_coins(self):
        coin_hitlist = arcade.check_for_collision_with_list(self.player_sprite, self.scene['Coins'])

        for coin in coin_hitlist:
            coin.remove_from_sprite_lists()

            arcade.play_sound(self.collect_coin_sound)

    def on_update(self, delta_time: float):
        # move the player with the physics engine
        self.physics_engine.update()

        # move camera
        self.center_camera_to_player()

        # check for collision with coin and then remove coin
        self.collect_coins()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.scene['Player'].move(0, config.PLAYER_JUMP_SPEED)
                arcade.play_sound(self.jump_sound)
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