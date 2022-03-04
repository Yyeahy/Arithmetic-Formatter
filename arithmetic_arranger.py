def arithmetic_arranger(problems, answer=False):
    arranged_problems = str()
    firstl_list = []
    restl_list = []
    r_list = []
    str_len = []

    try:
        for problem in problems:

            if answer == True:
                result = eval(problem)
                r_list.append(str(result))

            problem = problem.split()
            index = 0

            for x in problem:

                if index == 0:
                    firstl_list.append(x)

                else:
                    restl_list.append(x)

                index += 1
    except SyntaxError:
        print("Error: Numbers must only contain digits.")

    except NameError:
        print("Error: Numbers must only contain digits.")

    else:
        for firstl in firstl_list:

            if len(firstl) > 4:
                arranged_problems = "Error: Numbers cannot be more than four digits."

        len_firstl = len(firstl_list)
        len_restl = len(restl_list)
        error_1 = False
        error_2 = False
        error_3 = False

        for i in range(len_restl):

            if i % 2 == 0:

                if restl_list[i] != "+" and restl_list[i] != "-":
                    error_1 = True
                    break
            else:

                if restl_list[i].isdigit() == False:
                    error_2 = True
                    break

                else:

                    if len(restl_list[i]) > 4:
                        error_3 = True
                        break

        if len_firstl > 5:
            arranged_problems = "Error: Too many problems."
        elif len_firstl <= 5 and error_1 == True:
            arranged_problems = "Error: Operator must be '+' or '-'."
        elif len_firstl <= 5 and error_2 == True:
            arranged_problems = "Error: Numbers must only contain digits."
        elif len_firstl <= 5 and error_3 == True:
            arranged_problems = "Error: Numbers cannot be more than four digits."
        else:
            index = 1

            for i in range(len_firstl):
                len_1 = len(firstl_list[i])
                len_2 = len(restl_list[index])

                if len_1 >= len_2:
                    s_len = len_1 + 2

                elif len_1 < len_2:
                    s_len = len_2 + 2

                str_len.append(s_len)

                if i == len_firstl - 1:
                    arranged_problems += firstl_list[i].rjust(s_len) + "\n"

                else:
                    arranged_problems += firstl_list[i].rjust(s_len) + " " * 4
                index += 2

            index = 0
            for i in range(len_restl):

                if i % 2 == 0:
                    arranged_problems += restl_list[i]

                else:
                    if i == len_restl - 1:
                        arranged_problems += restl_list[i].rjust(
                            str_len[index] - 1) + "\n"
                    else:
                        arranged_problems += restl_list[i].rjust(
                            str_len[index] - 1) + " " * 4
                        index += 1

            for i in range(len_firstl):

                if i == len_firstl - 1:
                    if answer == True:
                        arranged_problems += "-" * str_len[i] + "\n"
                    else:
                        arranged_problems += "-" * str_len[i]
                else:
                    arranged_problems += "-" * str_len[i] + " " * 4

            if answer == True:

                for i in range(len(r_list)):
                    if i == len(r_list) - 1:
                        arranged_problems += r_list[i].rjust(str_len[i])
                    else:
                        arranged_problems += r_list[i].rjust(
                            str_len[i]) + " " * 4

    return arranged_problems
