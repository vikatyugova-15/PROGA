# -*- coding: windows-1251 -*-
from prettytable import PrettyTable
class Issuer:  # эмитент
    def __init__(self, name, rank):
        self.name = name 
        self.rank = rank
        self.investors = set()
        self.issue = []
    
    def add_issue(self, issue):
        self.issue.append(issue)
        issue.issuer = self

    def show_issues(self):
        table = PrettyTable()
        table.field_names = ["Эмитент", "Рейтинг", "ID выпуска"]
        for issue in sorted(self.issue, key=lambda x: x.id):
            table.add_row([self.name, self.rank, issue.id])
        print(table)




class Release:  #выпуск бумаг
    def __init__(self, id):
        self.id = id 
        self.issuer = None 
        self.investors = set()

    def add_investor(self, investor):
        self.investors.add(investor)
        investor.properties.add(self)

    def show_investors(self):
        table = PrettyTable()
        table.field_names = ["ID выпуска", "Инвестор"]
        for inv in sorted(self.investors, key=lambda x: x.name):
            table.add_row([self.id, inv.name])
        print(table)

        

class Investor:  #покупатель
    def __init__(self, name):
        self.name = name 
        self.properties = set()



gazprom = Issuer("Gasprom", "A+")

release1 = Release("GAZ-2025")
release2 = Release("GAZ-2027")

gazprom.add_issue(release1)
gazprom.add_issue(release2)

print(f"Issuer {gazprom.name} released: {[r.id for r in gazprom.issue]}")


release = Release("SBER-2026")
sber = Issuer("Sberbank", "AA")
sber.add_issue(release)

ivan = Investor("Ivan")
anna = Investor("Anna")

release.add_investor(ivan)
release.add_investor(anna)

print(f"Investors, have been bought {release.id}: {[i.name for i in release.investors]}")



gazprom = Issuer("Gasprom", "A+")
sber = Issuer("Sberbank", "AA")

bond1 = Release("GAZ-2025")
bond2 = Release("SBER-2027")

gazprom.add_issue(bond1)
sber.add_issue(bond2)

anna = Investor("Anna")
bond1.add_investor(anna)
bond2.add_investor(anna)

print(f"{anna.name} owe: {[r.id for r in anna.properties]}")


vtb = Issuer("VTB", "A")
bond = Release("VTB-2026")
vtb.add_issue(bond)


ivan = Investor("Ivan")
maria = Investor("Maria")

bond.add_investor(ivan)
bond.add_investor(maria)


print(f"Issuer: {bond.issuer.name} (rank {bond.issuer.rank})")
print(f"Releas: {bond.id}")
print(f"Investors: {[i.name for i in bond.investors]}")

gazprom = Issuer("Газпром", "A+")
sber = Issuer("Сбербанк", "AA")
vtb = Issuer("ВТБ", "A")

bond1 = Release("GAZ-2025")
bond2 = Release("GAZ-2027")
bond3 = Release("SBER-2026")
bond4 = Release("VTB-2026")


gazprom.add_issue(bond1)
gazprom.add_issue(bond2)
sber.add_issue(bond3)
vtb.add_issue(bond4)


ivan = Investor("Иван")
anna = Investor("Анна")
maria = Investor("Мария")


bond1.add_investor(ivan)
bond1.add_investor(anna)
bond3.add_investor(anna)
bond4.add_investor(maria)
bond4.add_investor(ivan)


print("\n Держатели выпуска VTB-2026:")
bond4.show_investors()


print("\n Все выпуски по эмитентам:")
for issuer in sorted([gazprom, sber, vtb], key=lambda x: x.name):
    issuer.show_issues()

print('\n Все эмитенты с ретенгом A и AA:')
for issuer in [i for i in [gazprom, sber, vtb] if i.rank in ('A', 'AA')]:
    issuer.show_issues()