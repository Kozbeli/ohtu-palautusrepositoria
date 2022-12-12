from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.query = matcher

    def playsIn(self, team):
        return QueryBuilder(All(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(All(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(All(self.query, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(All(self.query, Or(*matchers)))

    def build(self):
        return self.query