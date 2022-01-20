import Student
from tabulate import tabulate
from dbInfo import cursor

def MBTI_Score():
    sql = """ SELECT o.mbti_one, mbti as mbti_two, o.score FROM (SELECT from_student_id, mbti as mbti_one, to_student_id, score
        FROM score, students WHERE from_student_id = students.student_id) as o , students WHERE o.to_student_id = students.student_id;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, headers = 'keys'))

if __name__ == "__main__":
    MBTI_Score()