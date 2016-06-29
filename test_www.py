# -*- coding: utf-8 -*-
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = os.environ.get("URL", "https://www.lamutuellegenerale.fr/")

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)


class Suite(unittest.TestCase):
    """Test du site 'La Mutuelle Generale'"""

    def test_01_openpage(self):
        """Ouverture de la page"""
        driver.get(base_url)
        self.assertIn(u"Devis et tarif Mutuelle santé - Assurance prévoyance", driver.title)

    def test_02_devisdeuxminutes(self):
        """Click sur le bouton 'Devis en deux minutes'"""
        driver.find_element_by_link_text(u"VOTRE DEVIS EN DEUX MINUTES").click()
        self.assertIn(u"Devis gratuit | La Mutuelle Générale", driver.title)

    def test_03_devissante(self):
        """Click sur le devis santé"""
        driver.find_element_by_link_text(u"cliquez ici !").click()
        driver.find_element_by_class_name("popinSimulateur")

    def test_04_fermeturedevis(self):
        """Fermeture du popin"""
        driver.find_element_by_css_selector("#layerGeneriqueContent .popinSimulateur .close").click()
        driver.find_element_by_link_text(u"cliquez ici !")

    def test_05_espaceadherent(self):
        """Click sur 'Espace Adhérent'"""
        driver.find_element_by_id("lienEspaceAdherent").click()
        self.assertIn(u"Identification", driver.title)
        driver.find_element_by_id("NumeroContrat")

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
