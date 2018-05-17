from rules.rule import Rule


class ParagraphRule(Rule):
    type = 'paragraph'

    def condition(self, block):
        return True
