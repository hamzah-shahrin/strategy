from . import tile


class Water(tile.Tile):
    def __init__(self, pos, callback=None):
        super(Water, self).__init__(pos, color=[32, 32, 38], callback=callback)
        self.name = "Water Tile"
