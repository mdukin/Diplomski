import sys
import math
from hooke_jeeves import hooke_jeeves

class ogr_nejednakosti:
    def __init__(self,ogranicenja) -> None:
        self.ogranicenja = ogranicenja
    
    def zadovoljava(self, X):
        for ogranicenje in self.ogranicenja:
            if ogranicenje(X) < 0:
                return False
        return True
    def mjesovito(self, X):
        if self.ogranicenja == None: return 0
        f = lambda X: sum( -math.log(g(X) ) if g(X) > 0 else sys.float_info.max
                          for g in self.ogranicenja)
        return f(X)
    
    def vrati_tocku_koja_zad_ogr(self,X0):
        f = lambda X: sum( -g(X)  if g(X) < 0 else 0 for g in self.ogranicenja)
        return hooke_jeeves(X0,f)

class ogr_ekspl:
    def __init__(self, Xd, Xg) -> None:
        self.Xd = Xd
        self.Xg = Xg
    def zadovoljava(self, X):
        for xi, xid, xig in zip(X, self.Xd, self.Xg):
            if not (xid <= xi <= xig):
                return False
        return True

class ogr_jednakosti:
    def __init__(self,ogranicenja) -> None:
        self.ogranicenja = ogranicenja
    
    def zadovoljava(self, X):
        for ogranicenje in self.ogranicenja:
            if ogranicenje(X) != 0:
                return False
        return True
    def mjesovito(self, X):
        if self.ogranicenja == None: return 0
        f = lambda x: sum(func(x)**2 for func in self.ogranicenja)
        return f(X)