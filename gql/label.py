class Label:
    def __init__(self, json):
        self.name = json['name']

    def __str__(self):
        return self.name
