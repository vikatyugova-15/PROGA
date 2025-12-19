# -*- coding: windows-1251 -*-
import unittest
from finance import Issuer, Release, Investor


class TestFinanceSystem(unittest.TestCase):

    #  Тест 1: добавление выпуска эмитенту
    def test_issuer_add_issue(self):
        issuer = Issuer("Газпром", "A+")
        release = Release("GAZ-2025")

        issuer.add_issue(release)

        self.assertEqual(issuer.get_issue_ids(), ["GAZ-2025"])
        self.assertEqual(release.issuer, issuer)

    #  Тест 2: покупка облигации инвестором
    def test_release_add_investor(self):
        release = Release("SBER-2026")
        investor = Investor("Анна")

        release.add_investor(investor)

        self.assertEqual(release.get_investor_names(), ["Анна"])
        self.assertEqual(investor.get_release_ids(), ["SBER-2026"])

    #  Тест 3: один инвестор владеет несколькими выпусками
    def test_investor_multiple_releases(self):
        investor = Investor("Иван")
        r1 = Release("GAZ-2025")
        r2 = Release("VTB-2026")

        r1.add_investor(investor)
        r2.add_investor(investor)

        self.assertEqual(investor.get_release_ids(), ["GAZ-2025", "VTB-2026"])


if __name__ == "__main__":
    unittest.main()
