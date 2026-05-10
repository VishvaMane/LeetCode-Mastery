class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # decide which column we need to check
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2   # ruleKey == "name"

        count = 0

        # check every item
        for item in items:
            # if current item's selected field matches ruleValue
            if item[idx] == ruleValue:
                count += 1

        return count