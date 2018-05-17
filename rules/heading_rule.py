from rules.rule import Rule


class HeadingRule(Rule):
    type = 'heading'

    def condition(self, block):
        return '\n' not in block and not block[-1] == ':'
