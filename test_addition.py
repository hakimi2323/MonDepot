import unittest
def addition (a,b):
    return a+b
# TDD : developpment dirige par les test 
# Ecrivez une methode de etst pour la fonction
def test_addition():
    # appeler le fonction a tester
    result = addition(3,5)
    # Assertion pour verifier si le resutat est au resultat attendu
    assert result == 8 , f"le resultat attendu est 8 , mais le resulat obtenu est {result}"
    result = addition(3,9)
    assert result == 12 , f"le resultat attendu est 12 , mais le resulat obtenu est {result}"
# Creez une suite de tests et executez-les
test_addition()
print("Test termine ...")