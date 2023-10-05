import unittest
import HtmlTestRunner

from tema.tema9.teste_2 import clasa_de_Test
from tema.tema9.verificatori import Intrare



class TestSuita(unittest.TestCase):

		def test_suite(self):
				teste_de_rulat = unittest.TestSuite()
				teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Intrare),
										 unittest.defaultTestLoader.loadTestsFromTestCase(clasa_de_Test)])

				runner = HtmlTestRunner.HTMLTestRunner(

						combine_reports=True,
						report_title = "Test Execution Report",
						report_name = "Test Results"
				)

				runner.run(teste_de_rulat)