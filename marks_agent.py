
def analyze_marks(marks):
    total = sum(marks.values())
    average = total / len(marks)

    lowest_subject = min(marks, key=marks.get)

    return {
        "total": total,
        "average": round(average, 2),
        "lowest_subject": lowest_subject,
        "lowest_marks": marks[lowest_subject]
    }
