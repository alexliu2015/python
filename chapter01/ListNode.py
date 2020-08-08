class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        return

    def has_value(self, data):
        if self.val == data:
            return True
        else:
            return False

    def __eq__(self, otherNode):
        if self.val == otherNode.val:
            return True
        else:
            return False

    def __lt__(self, otherNode):
        if self.val <= otherNode.val:
            return True
        else:
            return False