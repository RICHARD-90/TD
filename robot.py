# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:02:49 2020

@author: Junio
"""
class Robot():
    
    '''
    modeliser l'etat et le comportement d'un robot
    '''
    (x,y) = (0,0)
    direct = 'Est'
    
    def __init__(self):
        self.nom = 'robot'
    
    def position(self):
        couple = self.avance()
        self.x = couple[0]
        self.y = couple[1]
        return (self.x,self.y)
    
    def direction(self):
        self.direct = self.orienter()
        return self.direct
    
    '''
    dans ce programme, demander au robot d'avancer veut dire deplace toi d'un pas
    '''
    
    def avance(self,p=0):
        if p == 0: pass
        elif  p==1:
            if self.direction() == 'Est':
                self.x += 1
            elif self.direction() =='Nord':
                self.y += 1
            else: print('je ne peux pas me deplacer')
        return (self.x,self.y)
    
    
    def orienter(self,a=0):
        orientation = ['Sud','Ouest','Nord','Est']
        valeur = self.direct
        if a ==0: return valeur
        elif a == 1 :
            for k in range(len(orientation)):
                if  valeur == orientation[k]:
                    if k != 3:
                        self.direct = orientation[k+1]
                    else: self.direct = orientation[0]
            valeur = self.direct
            return self.direct
    
    
    def info(self):
        return (self.nom,self.position(),self.direction())
