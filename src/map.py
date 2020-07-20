import noise


class Map:
    def __init__(self, path, size):
        self.width, self.height = size
        self.x, self.y = self.width//8, self.height//8
        try:
            with open(path, 'r') as file:
                self._map_data = file.read().split('\n')
                self._map_data = [list(map(int, list(i))) for i in self._map_data]
        except FileNotFoundError:
            self._map_data = [([0]*self.x) for _ in range(self.y)]
            for x in range(self.y):
                f = noise.pnoise1(x / 1000, octaves=3, lacunarity=10, persistence=0.6, base=1200)
                y = round((f * self.x) + (self.x//2))
                for index, _ in enumerate(self._map_data[x]):
                    if index > y:
                        self._map_data[x][index] = 1
                # TODO: Repeat for trees/sand
            with open(path, 'w+') as file:
                final = ''
                for i in self._map_data:
                    final += ''.join([str(j) for j in i]) + '\n'
                file.write(final[:-1])

    def get_map(self):
        return self._map_data
