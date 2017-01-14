# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:52:46 2016

@author: Xiiime
Credits for prime numbers generator
Les recettes de Tyrtamos
http://python.jpvweb.com/mesrecettespython/doku.php?id=liste_des_nombres_premiers
"""

class Ut:
    """
    Ut contient:
    tree = un arbre de nombres premiers jusque n
    manifold = l'ensemble des éléments connectés à cet arbre
    """
    def __init__(self, *size):
        self.tree = list()
        self.manifold = dict()            
        # tree est la liste de premiers qui sert de base       
    def __repr__(self):        
        return 'Ut: {} => {}'.format(self.tree, self.manifold.keys())
    def __len__(self):
        return len(self.tree)
    def __call__(self):
        return self.tree
    def size(self):
        return len(self.manifold)
    def sizecheck(self, param):
        if not self.tree or param > self.tree[-1]:
            self.treeme(param)
    def premiers(self, n, p=[2,3,5]):      
        k = p[-1]+2
        if n < k:
            return [x for x in p if x<=n]
        while k <= n:
            i = 0
            while i < len(p):
                if p[i]*p[i] > k:
                    p.append(k)
                    break
                if (k % p[i]) == 0:
                    break
                i += 1
            k += 2
        return p
    def treeme(self, n):
        if not self.tree or len(self.tree) == 0:
            self.tree = self.premiers(n)
        elif n > self.tree[-1]:
            self.tree = self.premiers(n,self.tree)
    def grow(self):
        """
        Ajoute un élément à tree
        ATTENTION ! L'algo Premiers trouvé suppose trois éléments de base.
        (premiers jusque 5)A prendre en compte lors du mapping !
        """
        if len(self.tree) == 0:
            self.treeme(5)
        else:
            into = len(self.tree)
            n=1
            while len(self.tree) == into:
                self.treeme(self.tree[-1]+n)
                n+=1
            
            
    def checktree(self,Hz):
        return [x for x in self.tree if not bool(x==Hz) or not bool(x>Hz)]
    def windtree(self,Hz):
        self.sizecheck(Hz)
        return [x for x in self.tree if Hz%x == 0]