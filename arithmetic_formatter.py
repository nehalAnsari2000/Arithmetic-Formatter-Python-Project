  
# Function to check errors in the problems
def problem_validation_checker(first_operands, operators, second_operands):
    # Checking for operator other than + and -
    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    # Checking for only digits
    for first_operand in first_operands:
        if not first_operand.isdigit():  # Better than try-except
            return 'Error: Numbers must only contain digits.'
    for second_operand in second_operands:
        if not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'

    # Checking for number of digits, not more than 4
    for first_operand in first_operands:
        if len(first_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    for second_operand in second_operands:
        if len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    return True  # If no errors, return True


def arithmetic_arranger(problems, show_answers=False):
    # checking for number of problems, it should not be more than 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # creating separate list for first operand, operator and second operand 
    first_operands = [i.split(' ')[0] for i in problems]
    operators= [i.split(' ')[1] for i in problems]
    second_operands = [i.split(' ')[2] for i in problems]

    # checking for validation of problems
    response = problem_validation_checker(first_operands, operators, second_operands)
    if response == True:
        # performing operations and storing it in a list
        operations = []
        i = 0
        while i<len(problems):
            if operators[i] == '+':
              operations.append(int(first_operands[i]) + int(second_operands[i]))
              i+=1
            elif operators[i] == '-':
              operations.append(int(first_operands[i]) - int(second_operands[i])) 
              i+=1
            else :
                i+=1

        # Calculating column width
        column_widths = []
        i = 0
        while i < len(problems):
          column_widths.append(max(len(first_operands[i]), len(second_operands[i])) + 2)
          i+=1
        
        # Main Logic for printing the formatter
        i = 0
        first_line = ''
        second_line = ''
        third_line = ''
        fourth_line = ''
    
        while i < len(problems):
            first = first_operands[i]
            second = second_operands[i]
            res = str(operations[i])
            width = column_widths[i]
            
            no_of_spaces_f = width - len(first)      # calculating first line
            j=1
            while j <= no_of_spaces_f:
                first_line += ' '
                j+=1
            first_line += first
            if i < len(problems) - 1:    # This condition is for making sure that spaces should not append at the end of of line
                first_line += '    '
            
            no_of_spaces_s = width - len(second) - 1     # calculating second line
            j=1
            second_line += operators[i]
            while j <= no_of_spaces_s:
                second_line += ' '
                j+=1
            second_line += second
            if i < len(problems) - 1:
                second_line += '    '                

            third_line += ('-' * width)         # calculating third line
            if i < len(problems) - 1:
                third_line += '    '

            no_of_spaces_fourth = width - len(res)      #calculating fourth line
            j=1
            while j <= no_of_spaces_fourth:
                fourth_line += ' '
                j+=1
            fourth_line += res
            if i < len(problems) - 1:
                fourth_line += '    '          

            i+=1
       
        if show_answers == True:
            return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
        else:
            return first_line + '\n' + second_line + '\n' + third_line 
    else:
        return response
    
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
