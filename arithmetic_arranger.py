import re


def validateOperatorsAndNumbers(string_to_check):
    if '*' in string_to_check or '/' in string_to_check:
        return "Error: Operator must be '+' or '-'."
    elif re.search("[a-zA-Z]", string_to_check):
        return "Error: Numbers must only contain digits."
    else:
        return ""


def findOperator(string_to_evaluate):
    if '+' in string_to_evaluate:
        return '+'
    elif '-' in string_to_evaluate:
        return '-'
    else:
        return "Error: This shouldn't happen"


def checkOperation(elements_to_evaluate):
    if len(elements_to_evaluate) != 3 or elements_to_evaluate[1] not in ['+', '-']:
        return "Error: Invalid expression"
    elif len(elements_to_evaluate[0]) > 4 or len(elements_to_evaluate[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        return ""


def arithmetic_arranger(problems, print_results=False):
    """
    A function that takes a string with arithmetic operations and prints them in multiple lines format
    :param problems: a string containing addition and substractions of 4 digit numbers
    :param print_results: a boolean indicating whether or not the results should be computed and printed.
    :return:
    """
    column_separator = " " * 4
    if len(problems) > 5:
        return "Error: Too many problems."
    invalid_input = validateOperatorsAndNumbers("".join(problems))
    if invalid_input:
        return invalid_input
    first_line = ""
    second_line = ""
    dashed_line = ""
    results = ""
    for expression in problems:
        expression_elements = expression.split()
        invalid_operation = checkOperation(expression_elements)
        if invalid_operation:
            return invalid_operation
        current_total = eval(expression)
        operation_length = max(len(expression_elements[0]), len(expression_elements[2]))
        if first_line == "":
            first_line += "  {0: >{1}}".format(expression_elements[0], operation_length)
            second_line += "{0} {1: >{2}}".format(expression_elements[1], expression_elements[2], operation_length)
            dashed_line += "-" * (operation_length + 2)
            results += " {0: >{1}}".format(current_total, operation_length + 1)
        else:
            first_line += "{0}  {1: >{2}}".format(column_separator, expression_elements[0], operation_length)
            second_line += "{0}{1} {2: >{3}}".format(column_separator, expression_elements[1], expression_elements[2],
                                                     operation_length)
            dashed_line += column_separator + "-" * (operation_length + 2)
            results += "{0} {1: >{2}}".format(column_separator, current_total, operation_length + 1)
    if print_results:
        return "\n".join([first_line, second_line, dashed_line, results])
    else:
        return "\n".join([first_line, second_line, dashed_line])
