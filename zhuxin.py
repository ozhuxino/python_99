class Route(object):
    def __init__(self):
        self.j = "qj"
    def __new__(cls, *args, **kwargs):
        super(Route, self).__new__()
    def __str__(self):
        return "这是一个神起"