def on_overlap_tile(sprite, location):
    if True:
        info.change_score_by(1)
        tiles.set_tile_at(location, sprites.castle.tile_grass1)
    else:
        game.splash("Incorrect!")
        info.change_score_by(-1)
        tiles.set_tile_at(location, sprites.castle.tile_grass1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile15
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
    """),
    on_overlap_tile2)

scene.set_background_color(7)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
Connor = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f e f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Connor, 100, 100)
tiles.place_on_random_tile(Connor, assets.tile("""
    myTile3
"""))
scene.camera_follow_sprite(Connor)
info.set_score(0)