scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile15`, function (sprite, location) {
    game.splash("this statement is type")
    if (true) {
        info.changeScoreBy(1)
        tiles.setTileAt(location, sprites.castle.tileGrass1)
    } else {
        game.splash("Incorrect!")
        info.changeScoreBy(-1)
        tiles.setTileAt(location, sprites.castle.tileGrass1)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile12`, function (sprite2, location2) {
    game.over(true)
})
scene.setBackgroundColor(7)
tiles.setCurrentTilemap(tilemap`level2`)
let Connor = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Connor, 100, 100)
tiles.placeOnRandomTile(Connor, assets.tile`myTile3`)
scene.cameraFollowSprite(Connor)
info.setScore(0)
