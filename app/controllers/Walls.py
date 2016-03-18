from system.core.controller import *

class Walls(Controller):
    def __init__(self, action):
        super(Walls, self).__init__(action)

        self.load_module('Wall')
        self.load_module('Dashboard')
        self.load_module('Dashboards')

    def wall(self, id):
        print " loading The Wall "*20
        # messages = self.models['Wall'].get_messages_by_wall(id)
        return self.load_view('walls/wall.html', messages=messages, id=id)
