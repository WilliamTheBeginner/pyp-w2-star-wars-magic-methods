class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        if self.name != type(str):
        	raise TypeError()

    def __str__(self):
    	return self.name

    def __call__(self):
    	return 'Help me {}, you\'re my only hope.'.format(self.name)

    def __div__(self, other):
    	if self or other is type(object):

    		return '{} throws a lightsaber at {}.'.format(self.name, other.name)
    	else:
    		raise TypeError()

    def __mul__(self, other):
    	pass