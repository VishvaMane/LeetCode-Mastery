class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        result = set()

        def expand(expr):
            if '{' not in expr:
                result.add(expr)
                return

            close_idx = expr.find('}')
            open_idx = expr.rfind('{', 0, close_idx)

            prefix = expr[:open_idx]
            suffix = expr[close_idx + 1:]
            options = expr[open_idx + 1:close_idx]

            for option in options.split(','):
                expand(prefix + option + suffix)

        expand(expression)
        return sorted(result)