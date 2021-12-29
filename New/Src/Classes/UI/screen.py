from Utils.loadmap import load_map, transcribe_map, render_map, get_tiles

class Screen:
    def __init__(self, value, objects, map_path):
        self.value = value
        self.objects = objects
        self.map = load_map(map_path)
        self.tmap = transcribe_map(self.map)
        self.tiles = get_tiles(self.map)
    def update(self, keys, mouse_pos, camera):
        if self.objects['player']: self.objects['player'].update(keys, self.tiles)
        if self.objects['gun']: self.objects['gun'].update(self.objects['player'], mouse_pos)
        camera.update(self.objects['player'])
    def render(self, display, assets, camera):
        render_map(display, self.tmap, assets, camera)
        for value in self.objects.values():
            value.render(display, camera)