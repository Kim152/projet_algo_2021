#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Ce module contient les classes et fonctions de bases qui vous seront nÃ©cessaires
lors de la rÃ©alisation projet du cours d'algorithmique.
En particulier, ce module dÃ©clare:
  * La classe abstraite `ArbreBinaire` que vous devez complÃ©ter.
  * La fonction `creer_arbre(forme_parenthesee)` que vous devez implementer.
'''

class ArbreBinaire:
    '''
    Ce prototype de classe (Ã  modifier par vous) est une version simplifiÃ©e de 
    la classe qui vous a Ã©tÃ© prÃ©sentÃ© lors du cours sur l'implÃ©mentation des 
    arbres binaires.

    .. important::
       Le nom de la methode `simplifier` ainsi que sa signature vous
       sont imposÃ©s. Si vous modifiez un de ces Ã©lÃ©ments, votre code ne pourra
       pas Ãªtre validÃ©.
    '''

    def __init__(self, elem=None, left=None, right=None):
        '''
        :pre: -
        :post: initialize a new Binary Tree with "elem" stored at the root node,
               when "elem" is None, this is interpreted as an empty BinaryTree.
        '''
        self.root_elem  = elem  # An element at the root
        self.left_tree  = None
        self.right_tree = None
    
    def est_une_feuille(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© est une feuille.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi ce (sous-)arbre est une feuille.
        '''
        if self.right_tree == None and self.left_tree == None:
            return True
        return False


    def a_un_enfant_gauche(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© possÃ¨de un 
        sous-arbre Ã  gauche.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi le sous arbre gauche de cet arbre existe
        '''
        if self.left_tree != None:
            return True
        return False

    def a_un_enfant_droit(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© possÃ¨de un 
        sous-arbre Ã  droite.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi le sous arbre droit de cet arbre existe
        '''
        if self.right_tree != None:
            return True
        return False

    
    def hauteur(self):
        '''
        Renvoie le nombre de niveaux maximum en dessous du noeud courant. 
        (Note: pour une feuille, ca sera toujours 0).

        Suggestion, afin de rendre votre implÃ©mentation plus efficace, vous 
        pourriez vouloir stocker le rÃ©sultat de cette methode dans un attribut
        privÃ© de votre classe et le renvoyer chaque fois que cette mÃ©thode est
        appelÃ©e. Quel impact cela a-t-il sur la complexitÃ© spatiale de votre 
        algorithme ? Et sur la complexitÃ© temporelle ? 
        (A discuter avec l'assistant lors de la sÃ©ance de follow-up)

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie Renvoie le nombre de niveaux maximum en dessous du noeud 
                courant. 
        '''
        if self.est_une_feuille():
            return 0
        return 1+ max(self.right_tree.hauteur(), self.left_tree.hauteur())


    def simplifier(self, i):
        '''
        Renvoie un dÃ©coupage de la phrase correspondant au `i`eme niveau de 
        l'arbre d'analyse.

        :pre:    L'arbre est valide (il a pu Ãªtre interprÃ©tÃ© correctement)
        :post:   Renvoie une chaine de caractere reprÃ©sentant le dÃ©coupage de
                 l'arbre selon son `i` eme niveau. 
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
        if self.left_tree == None and self.right_tree ==None:
            return self.root_elem
        if i > 0 :
            return f"{ self.left_tree.simplifier(i-1)}| {self.right_tree.simplifier(i-1)}"
        else :
            if i == 0:
                return f"{self.left_tree.simplifier(0)}{self.right_tree.simplifier(0)}"

def creer_arbre(forme_parenthesee):
    '''
     Cette fonction permet de crÃ©er une instance d'ArbreBinaire correspondant Ã  
     l'arbre encodÃ©e dans la chaine de caractÃ¨res en forme parenthÃ©sÃ©e.

     :pre:  Le paramÃ¨tre forme_parenthesee est une chaine de caractÃ¨res qui 
            encode un arbre d'analyse valide.
     :post: Renvoie une instance de la classe ArbreBinaire ci-dessus.
            L'instance retournee correspond Ã  ce qui est encodÃ© dans forme_parenthesee.

     :exc:  Si la prÃ©condition devait Ãªtre violÃ©e lors de l'appel Ã  cette fonction,
            vous Ãªtes autorisÃ©s Ã  lever une exception de type ValueError qui est une
            exception standard du langage Python3.
    '''
    # TODO: A vous d'implÃ©menter cette fonction
    #
    #       Note:
    #         Vous n'Ãªtes pas *formellement* obligÃ©s de dÃ©finir des fonctions
    #         et classes utilitaires pour parser la forme parenthÃ©sÃ©e; en
    #         thÃ©orie il est possible de tout faire dans la fonction
    #         `creer_arbre`. Cependant, nous vous dÃ©conseillons fortement cette
    #         approche et vous encourageons Ã  modulariser votre code.
    #         Ce faisant, vous rendrez votre solution plus Ã©lÃ©gante (pour vous
    #         comme pour nous), plus simple et probablement beaucoup plus courte
    #         (ce qui demandera donc moins d'effort de votre part).
    pass

# TODO: Donnez ici l'implÃ©mÃ©ntation des fonctions et classes utilitaires que
#       vous utilisez pour parser (interprÃ©ter) une chaine de caractÃ¨res en
#       forme parenthÃ©sÃ©e.
#
#       Note:
#         Vous n'Ãªtes pas *formellement* obligÃ©s de dÃ©finir des fonctions
#         et classes utilitaires pour parser la forme parenthÃ©sÃ©e; en thÃ©orie
#         il est toujours possible de tout faire dans la fonction `creer_arbre`
#         ci-dessus. Cependant, nous vous dÃ©conseillons fortement cette approche
#         et vous encourageons Ã  modulariser votre code. Ce faisant, vous
#         rendrez votre solution plus Ã©lÃ©gante (pour vous comme pour nous), plus
#         simple et probablement beaucoup plus courte.


if __name__ == '__main__':
    '''
     Ce simple test a pour but de vous permettre de valider plus facilement le rÃ©sultat de votre
     travail. Ce point d'entrÃ©e **ne sera en aucun cas appelÃ©e** lors de l'Ã©valuation de votre
     travail sur INGInious. Il est donc nÃ©cessaire que vous Ã©criviez votre code en respectant les
     instructions qui vous sont donnÃ©es ci-dessus.

     Pour aller plus loin (Optionnel):
     ---------------------------------
     Ceux qui veulent effectuer une vÃ©rification plus robuste de leur solution sont invitÃ©s Ã 
     Ã©crire une suite de tests avec le module `unittest` (ou `nose`) de python. Celle-ci vous
     permettra de valider le comportement des/de l' implÃ©mentation(s) de la classe `ArbreBinaire`
     que vous avez rÃ©alisÃ© ainsi que celui de la mÃ©thode 'creer_arbre()' dÃ©finie ci-dessus.
    '''
    # Une phrase d'exemple
    exemple = '''
              ((((2 An) ((4 engaging) (2 overview))) ((2 of) (((2 Johnson) (2 's)) ((2 eccentric) (3 career))))) (2 .))
              '''

    # CrÃ©ation d'un arbre d'analyse correspondant Ã  l'exemple donnÃ© ci-dessus.
    arbre = creer_arbre(exemple)
    # Calcul du dÃ©coupage de l'arbre selon le niveau 1
    calcule=arbre.simplifier(1)
    attendu="An engaging overview of Johnson 's eccentric career|."

    # TODO: A vous de jouer.
    #       Cet exemple de programme imprime le decoupage pour l'exemple donnÃ© dans
    #       les instructions du projet. Vous Ãªtes encouragÃ©s Ã  dÃ©finir de nouveaux
    #       tests par vous mÃªme ou adapter cet exemple de programme.
    print("Le decoupage calculÃ© est '{}'.".format(calcule))
    print("Le decoupage attendu est '{}'.".format(attendu))