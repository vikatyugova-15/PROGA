# -*- coding: windows-1251 -*-

class Issuer:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.issues = []

    def add_issue(self, issue):
        self.issues.append(issue)
        issue.issuer = self

    def get_issue_ids(self):
        return sorted(issue.id for issue in self.issues)


class Release:
    def __init__(self, id):
        self.id = id
        self.issuer = None
        self.investors = set()

    def add_investor(self, investor):
        self.investors.add(investor)
        investor.properties.add(self)

    def get_investor_names(self):
        return sorted(inv.name for inv in self.investors)


class Investor:
    def __init__(self, name):
        self.name = name
        self.properties = set()

    def get_release_ids(self):
        return sorted(release.id for release in self.properties)
