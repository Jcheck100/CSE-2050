def calcGrade(my_dict):
    total_grade = my_dict["particpation"]*.1 + my_dict["exams"]*.6 + my_dict["homework"]*.15 + my_dict["labs"]*.15
    return(total_grade)

my_dict = {
    "particpation": 80,
    "exams": 76,
    "labs": 90,
    "homework": 90
}

print(calcGrade(my_dict))



