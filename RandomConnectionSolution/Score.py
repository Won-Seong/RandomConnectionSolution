import Student
from tabulate import tabulate
from dbInfo import cursor

def stu_parsing(set_of_student_id):
    string = "("
    for x in set_of_student_id:
        string += "'" + x + "',"
    string = string[0: len(string) - 1]
    string += ')'
    return string

def mbti_score(mbti_one, mbti_two):
    sql = f"SELECT * FROM mbti_score WHERE mbti_one = '{mbti_one}' and mbti_two = '{mbti_two}';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result : return result["mu_score"]
    else : return 0

def interest_score(student_1_id , student_2_id):
    sql = f""" 
    SELECT interest_id 
    FROM student_interest
    WHERE student_id LIKE '{student_1_id}' AND interest_id IN (
    SELECT interest_id
    FROM student_interest
    WHERE student_id LIKE '{student_2_id}');
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return len(result) 

def two_student_score(student_1, student_2):
    asdf = mbti_score(student_1["MBTI"] , student_2["MBTI"])
    asdf += interest_score(student_1["student_id"], student_2["student_id"])
    asdf -= abs(student_1["birth"].year - student_2["birth"].year)
    if(student_1["place"] == student_2["place"]) : asdf += 1
    return asdf
    
     

if __name__ == "__main__":
    mbti_score("ENFJ" , "INFJ")
    interest_score("11112222","11112222")
    Student.student_info('11112222')
    two_student_score(Student.student_info('11112222') , Student.student_info('11113333'))
