import unittest

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
		
		# setUp method is called before each test in this class
		# This way each test starts with a clean account object

		def setUp(self):
			self.account = BankAccount(balance=1000)

		def test_deposit(self):
				self.assertEqual(self.account.deposit(100), 1100)

		def test_withdraw(self):
				self.assertEqual(self.account.withdraw(50), 950)

		def test_get_balance(self):
				self.assertEqual(self.account.get_balance(), 1000)
				