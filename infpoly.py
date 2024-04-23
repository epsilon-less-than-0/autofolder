class infpolyinfo:
    def __init__(self, info):
        self.info = info
        self.number_of_polygons = len(info)

    def list_info(self):
        return self.