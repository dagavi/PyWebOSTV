
class InputSource(object):
    def __init__(self, data):
        self.data = data
        self.label = data["label"]

    def __getitem__(self, val):
        return self.data[val]

    def __repr__(self):
        return "<InputSource '{}'>".format(self["label"])
