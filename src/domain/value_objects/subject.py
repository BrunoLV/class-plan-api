class Subject:

    def __init__(self, code, name):
        self.code = code
        self.name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):

        if value is None or type(value) is not str or value == '':
            raise ValueError('Code must be a non Blank string.')

        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if value is None or type(value) is not str:
            raise ValueError('Name must be a non Blank string.')

        self._name = value
