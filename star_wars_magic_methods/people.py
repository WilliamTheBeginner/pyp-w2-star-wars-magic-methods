class People(object):
    def __init__(self, name, dark_side=False, light_side=True):
        self.name = name
        self.dark_side = dark_side
        self.light_side = light_side
        if self.dark_side == True:
            self.light_side = False
        if self.light_side == True:
            self.dark_side = False
    def __str__(self):
    	return self.name

    def __call__(self):
    	return 'Help me {}, you\'re my only hope.'.format(self.name)

    def __div__(self, other):
    	if isinstance(self, People) and isinstance(other, People):

    		return '{} swings a lightsaber at {}.'.format(self.name, other.name)
    	else:
    		raise TypeError()

    def __mul__(self, other):
    	if isinstance(self, People) and isinstance(other, People):

    		return '{} throws a thermal detonator at {}!'.format(self.name, other.name)
    		
    	else:
    	    raise TypeError()

    def __rshift__(self, other):
        if isinstance(self, People) and isinstance(other, People):
            
    	    return '{} uses the force to push {} away from them.'.format(self.name, other.name)

        else:
            raise TypeError()
            
    def __lshift__(self, other):
    	if isinstance(self, People) and isinstance(other, People):
    	
    	    return '{} uses the force to pull {} towards them.'.format(self.name, other.name)

        else: 
            raise TypeError()
    def __neg__(self):
    	self.dark_side=True
    	self.light_side=False

    def __pos__(self):
    	if self.dark_side == True:
    	    self.light_side=True
    	    self.dark_side=False
    	

    def __invert__(self):
    	self.light_side = not self.light_side

    def __xor__(self, other):
    	return '{} force chokes {}.'.format(self.name, other.name)
    
    def __eq__(self, other):
        if other.name == 'Han Solo':
            return 'Han Solo shoots {}. BECAUSE HAN SHOOTS FIRST.'.format(self.name)
        
        return '{} shoots {}.'.format(self.name, other.name)
        
        
            
            
            
        
    	