class People(object):
    def __init__(self, name, dark_side=False, light_side=True):
        self.name = name

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
    	if self and other is type(object):

    		return '{} throws a terminal detonator at {}!'.format(self.name, other.name)

    def __rshift__(self, other):
    	return '{} uses the force to push {} away form them'.format(self.name, other.name)

    def __lshift__(self, other):
    	return '{} uses the force to push {} towards them'.format(self.name, other.name)

    def __neg__(self):
    	return dark_side=True
    	return light_side=False

    def __pos__(self):
    	return light_side=True
    	return dark_side=False

    def __invert__(self):
    	if light_side = True and dark_side = False:
    		return light_side = False and dark_side = True
    	if light_side = False and dark_side = True:
    		return light_side = True and dark_side = False

    def __xor__(self, other):
    	return '{} force chokes {}'.format(self.name, other.name)

    def 

    	