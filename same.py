class same:
  def __init__(self,a):
    self.a = a
    
  def __pow__(self,other,a):
    return pow(self,other,a)

    def __mod__(self, other):
        return self in other
