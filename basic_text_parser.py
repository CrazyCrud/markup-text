import sys
from parser import Parser
import rules
import handlers


class BasicTextParser(Parser):
    def __init__(self, output_handler):
        Parser.__init__(self, output_handler)
        self.addRule(rules.ListRule())
        self.addRule(rules.ListItemRule())
        self.addRule(rules.TitleRule())
        self.addRule(rules.HeadingRule())
        self.addRule(rules.ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = handlers.HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)
