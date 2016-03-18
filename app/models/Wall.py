from system.core.model import Model

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()

    def get_messages_by_wall(self, userid):
        print "retrieving messages method"
        messages_query = "SELECT * FROM messages WHERE wall_id = %s"
        messages_data = [userid]
        return self.db.query_db(messages_query, messages_data)
