class hamming:

    def distance(self,x,y):
        if len(x) != len(y):
            raise ValueError('Strands must be of equal length.')
        if len(x)==0 and len(y)==0:
            return 0

        return sum([1 for i in range(len(x)) if x[i] != y[i]])
        
    
    