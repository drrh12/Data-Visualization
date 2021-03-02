# Design a NFA with 3 states that accept {ab, abc}*

print("Insert below the string: ")
s = str(input())


def q0(s):
    if not s: return "accept"  # Accepting state.
    if s[0] == "a": return q1(s[1:])
    return "reject"


def q1(s):
    if not s: return "reject"
    # NFA, must try both edges.
    if (s[0] == "b" and q0(s[1:]) == "accept" or
        s[0] == "b" and q2(s[1:]) == "accept"):
        return "accept"
    return "reject"


def q2(s):
    if not s: return "reject"
    if s[0] == "c": return q0(s[1:])
    return "reject"


q0(s)
