from Tasks.a0_my_stack import Stack

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    b = Stack()
    if len(brackets_row) % 2 != 0:
        return False
    for i in brackets_row:
        if i == '(':
            b.push(i)
        if i == ')':
            b.pop()
    if len(b.stack) == 0:
        return True
    return False

print(check_brackets("(()("))

