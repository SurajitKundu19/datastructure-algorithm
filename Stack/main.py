from collections import deque


def reverse_string(text: str):
    stack_text = deque()
    for c in text:
        stack_text.append(c)
    rev_str = ""
    while stack_text:
        rev_str += stack_text.pop()
    return rev_str


def is_balanced(text: str) -> str:
    paren = {"(": ")", "{": "}", "[": "]"}
    closing = [")", "}", "]"]
    stack_paren = deque()
    out = True
    for c in text:
        if c in paren.keys():
            stack_paren.append(c)
        if c in closing:
            if not stack_paren or paren[stack_paren.pop()] != c:
                return False
    if stack_paren:
        return False
    return out


if __name__ == "__main__":
    rev = reverse_string("Hi there")
    print(rev)

    is_bal = is_balanced("(}")
    print(is_bal)
