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