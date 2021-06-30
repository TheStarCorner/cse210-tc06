class Guess:

    def __init__(self, guess):
        self._guess = guess
    def get_guess(self):
        return self._guess
    def set_guess(self, guess):
        self._guess = guess
    ''' 
        guess will get_guess and set_guess

    sterotype: info holder



    '''
    
    def __init__(self,guess):
    
        self.guess = guess


    def get_guess(self):
    
        return self.guess

    def set_guess(self,new_guess):
        
        self.guess = new_guess



