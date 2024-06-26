class City:
    def __init__(self, postcode, name):
        self.postcode = postcode
        self._name = name

    @property
    def postcode(self):
        return self._postcode
    @property
    def name(self):
        return self._name

    @postcode.setter
    def postcode(self, postcode):
        self._postcode = postcode

    @name.setter
    def name(self, name):
        self._name = name