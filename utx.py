# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:36:46 2016

@author: Xiiime     


MEMO
stream = streamer.Streamer(streamer.GephiWS())     
          
     node = graph.Node(hillx.tree.p[w], type="Premier")                            
     stream.add_node(node_p)
     
     edge_t = graph.Edge(source,key, type='Tige')
     stream.add_edge(edge_t)
                            
                            
"""
# Third Party
from gephistreamer import graph
from gephistreamer import streamer

#Python
import time

#Self-consistence
import Ut

class Utx:
    """
    Reprise de tree, hill et num sur une base propre
    Génère l'arbre Phi qu'il construit immédiatement dans gephi
    """
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = list()
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected. \
            Ajoutez un referent dans gephi avant d'ajouter des points \
            Gardez ce référent à portée avant d'ajouter des points \
            Connectez-vous en master")
        except :
            print('Impossible de se connecter au gephistreamer.')
            
        if type(seed) == Ut.Ut():
            self.sow(seed.manifold)
            
            
        # tree est la liste de premiers qui sert de base       
    def __repr__(self):        
        return 'Utx : {} => {}'.format(self.tree, self.manifold.keys()) 
    def out(self, elements=None):
        """
        stream out l'élément ajouté (node, edge) ou décortique la liste 
        d'éléments ajoutés
        """
        if not elements or elements == None:
            return 'nothing to add'
        elif type(elements) == graph.Node:
            self.stream.add_node(elements)
        elif type(elements) == graph.Edge:
            self.stream.add_edge(elements)
        elif isinstance(elements, list) == True:
            n=0
            while n<len(elements):
                if type(elements[n]) == graph.Edge or type(elements[n]) == graph.Node: 
                    self.out(elements[n])
                n+=1
        elif isinstance(elements, int)==True or isinstance(elements, str)==True:
            return 'Objet non graphable immediatement'
        elif type(elements) == dict():
            for key in elements.keys():
                self.out(elements[key])

        else:
            return elements

    def clearnodes(self):
        for key,values in self.manifold.items():
            p = self.manifold[key]
            i=0            
            while i<len(p):
                if type(p[i]) == graph.Node:
                    self.stream.delete_node(p[i])
                elif type(p[i]) == graph.Edge:
                    self.stream.delete_edge(p[i])
                i+=1
            del self.manifold[key]

    def connect(self, n):
        """
        Conncete un nombre à ses facteurs
        """
        toout=list()
        if not self.ut.tree:
            self.ut.treeme(n)
        if self.ut.checktree(n) == False:
            node = graph.Node(n, type='Factor')
            toout.append(node)
        else:
            node=graph.Node(n, type='Prime')
            toout.append(node)
        w=0
        while w < len(self.ut.tree):
            if n % self.ut.tree[w] == 0 and n/self.ut.tree[w] != 1:
                premierfac = graph.Node(self.ut.tree[w], type="Prime")
                toout.append(premierfac)
                premierResultat = graph.Node(n/self.ut.tree[w], type="Factor")
                self.lone.append(n/self.ut.tree[w])
                toout.append(premierResultat)
                lienfact = graph.Edge(premierfac, node, type="Product")
                toout.append(lienfact)
                lienfac2 = graph.Edge(premierfac, premierResultat, type="Product")
                toout.append(lienfac2)
            elif n%self.ut.tree[w] == 0 and n/self.ut.tree[w] == 1 and n != 1:
                premierfac = graph.Node(n/self.ut.tree[w], type="Prime")
                toout.append(premierfac)
                premierprecedent = graph.Node(self.ut.tree[w-1], type="Prime")
                toout.append(premierprecedent)
                arbre = graph.Edge(premierfac,premierprecedent, type='PrimeLine')
                toout.append(arbre)
            w+=1
        if len(toout) != 0:
            #self.ut.tree[n] = toout
            self.out(toout)



    def split(self):
        if not self.lone:
            return 'Rien a ajouter'
        key=0    
        while key < len(self.lone):
            if self.ut.checktree(self.lone[key])==True:
                del self.lone[key]
            try:   
                self.connect(self.lone[key])
            except IndexError:
                message = 'Terminé'                
                del self.lone
                return message
            key+=1
            
        self.lone=list()
    def sow(self, element):
        """
        Connecte les éléments d'une série présentée par l'argument element
        """
        if isinstance(element, int):
            self.connect(element)
        elif isinstance(element, list) or isinstance(element, tuple):
            keyn=0
            while keyn < len(element):
                self.connect(element[keyn])
                keyn+=1
        elif isinstance(element, dict):
            for key in element.keys():
                self.connect(key)
        elif isinstance(element, str):
            print ('Pas de dictionnaire pour les mots actuallement')
        else:
            try:
                key=0
                while key < len(element):
                    self.connect(element[key])
                    key+=1
            except:
                print('Objet non reconnu et non utilisable')
    def flow(self, timer=None):
        if timer == None:
            timer=0
        t=str()
        flux=2      
        while t != 'q':
            t=raw_input('Entrez q pour arrêter le flux...')
            print ('Ajout de {}...'.format(flux))            
            while flux > 0:
                self.connect(flux)
                time.sleep(timer)
                flux+=1
                
            
            
    def spread(self, timer=None):
        """
       ....
        """
        timing = time.time()
        if timer != None and isinstance(timer, int)==True:
            timeout = timing + timer*self.ut.tree[-1]
            print ('Attention, l\'opération prendra {} secondes.'.format(timeout-timing))
            follow = raw_input('Entrez oui pour continuer')
        else:
            follow = 'oui'
        
        if follow == 'oui':
            itmax = self.ut.tree[-1]
            while itmax >= 2:
#                try:
                    self.connect(itmax)
#                except : 
#                    return 'Erreur valeur{} '.format(itmax)
                if isinstance(timer,int):
                    time.sleep(timer)
                itmax-=1