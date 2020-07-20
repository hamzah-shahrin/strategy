from . import tile


class Grass(tile.Tile):
    def __init__(self, pos, callback=None):
        super().__init__(pos, color=[40, 46, 40], callback=callback)
        self.name = "Grass Tile"
