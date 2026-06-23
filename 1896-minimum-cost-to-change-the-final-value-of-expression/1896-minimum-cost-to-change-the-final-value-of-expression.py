class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def merge(a, op, b):
            az, ao = a
            bz, bo = b

            if op == '&':
                keep0 = min(az + min(bz, bo), bz + min(az, ao))
                keep1 = ao + bo

                flip0 = 1 + (az + bz)
                flip1 = 1 + min(ao + min(bz, bo), bo + min(az, ao))
            else:  # op == '|'
                keep0 = az + bz
                keep1 = min(ao + min(bz, bo), bo + min(az, ao))

                flip0 = 1 + min(az + min(bz, bo), bz + min(az, ao))
                flip1 = 1 + (ao + bo)

            return (min(keep0, flip0), min(keep1, flip1))

        vals = []
        ops = []

        def reduce_once():
            b = vals.pop()
            a = vals.pop()
            op = ops.pop()
            vals.append(merge(a, op, b))

        for ch in expression:
            if ch == '0':
                vals.append((0, 1))
            elif ch == '1':
                vals.append((1, 0))
            elif ch == '(':
                ops.append(ch)
            elif ch in '&|':
                while ops and ops[-1] in '&|':
                    reduce_once()
                ops.append(ch)
            else:  # ')'
                while ops and ops[-1] != '(':
                    reduce_once()
                ops.pop()

        while ops:
            reduce_once()

        z, o = vals[0]
        return max(z, o)