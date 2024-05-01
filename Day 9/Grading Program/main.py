student_scores = {
    "Alex": 81,
    "Morgan": 78,
    "Johanna": 99,
    "Sarah": 74
}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        print(f"{student} got A+")
    elif score > 80:
        print(f"{student} got A")
    elif score > 70:
        print(f"{student} got B+")
    elif score > 60:
        print(f"{student} got B")
    else:
        print(f"{student} got fail")
        