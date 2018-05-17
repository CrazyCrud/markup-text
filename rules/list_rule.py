from rules.list_item_rule import ListItemRule


class ListRule(ListItemRule):
    type = 'list'
    inside_list = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside_list and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside_list = True
        elif self.inside_list and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside_list = False
        return False
