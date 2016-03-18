from system.core.model import Model

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()

    def get_messages_by_wall(self, userid):
