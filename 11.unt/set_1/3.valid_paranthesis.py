# Valid Paranthesis


class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        stack = []

        for item in s:
            if item in ["(", "{", "["]:
                stack.append(item)
            elif item == ")":
                if not stack:
                    return False

                if stack[-1] != "(":
                    return False

                stack.pop()

            elif item == "}":
                if not stack:
                    return False

                if stack[-1] != "{":
                    return False

                stack.pop()

            elif item == "]":
                if not stack:
                    return False

                if stack[-1] != "[":
                    return False

                stack.pop()

            return stack == []