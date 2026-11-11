question = str(input("What is the Great Question of Life?"))
question_lower_case = question.lower()
question_lower_case_spaceless = question_lower_case.replace(" ","")
if question_lower_case_spaceless == str(42) or question_lower_case_spaceless == "forty-two" or question_lower_case_spaceless == "fortytwo":
    print("Yes")
else:
    print("No")
