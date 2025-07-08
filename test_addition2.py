import unittest

# Fonction à tester
def addition (a,b):
    return a+b
# Classe de test
class TestAddition (unittest.TestCase): # heritage de la classe TestCase de unittest
    #definition du code de la methode de test
    def test_addition(self):
        self.assertEqual(addition(2,3),5)
        self.assertEqual(addition(7,8),15)
        self.assertEqual(addition(9,3),12)
# definition d'un objet test
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition) # mettre comme argument le nom de classe definie pour le test
#Execution du test
unittest.TextTestRunner().run(test_addition)

# Code de la fonction à tester
def multiplication(a, b):  
    return a * b

# Classe de test
class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(-4, 3), -12)
        self.assertEqual(multiplication(-2, -2), 4)
        self.assertEqual(multiplication(1000, 0), 0)

# Exécution des tests 
suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)
unittest.TextTestRunner().run(suite)

# Code de la fonction à tester
def puissance(a, b):
    return a ** b

# Classe de test
class TestPuissance(unittest.TestCase):
    def test_puissance(self):
        self.assertEqual(puissance(2, 3), 8)      # 2^3 = 8
        self.assertEqual(puissance(5, 0), 1)      # 5^0 = 1
        self.assertEqual(puissance(0, 5), 0)      # 0^5 = 0
        self.assertEqual(puissance(2, -1), 0.5)   # 2^-1 = 0.5
        self.assertEqual(puissance(-3, 2), 9)     # (-3)^2 = 9
        self.assertEqual(puissance(-3, 3), -27)   # (-3)^3 = -27

# Exécution des tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)
unittest.TextTestRunner().run(suite)

# Code de la fonction à tester : pour calculer la somme des nombres inferieurs à n 
def somme_entiers_inferieurs(n):
    
    return sum(range(n))
class TestSommeEntiersInferieurs(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme_entiers_inferieurs(5), 10)   # 0+1+2+3+4 = 10
        self.assertEqual(somme_entiers_inferieurs(1), 0)    # aucun nombre < 1
        self.assertEqual(somme_entiers_inferieurs(0), 0)    # aucun nombre < 0
        self.assertEqual(somme_entiers_inferieurs(10), 45)  # 0+1+...+9 = 45

# Exécution 
suite = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)
unittest.TextTestRunner().run(suite)