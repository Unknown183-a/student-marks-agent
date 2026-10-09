
from marks_agent import analyze_marks
from advisor_agent import suggest_improvements


def run_pipeline(marks):
    # Agent 1
    analysis = analyze_marks(marks)

    # Agent 2
    recommendations = suggest_improvements(marks)

    return {
        "analysis": analysis,
        "recommendations": recommendations
    }


def main():
    marks = {}

    n = int(input("How many subjects? "))

    if n <= 0:
        print("Enter at least one subject.")
        return

    for _ in range(n):
        subject = input("Subject name: ").strip()
        score = float(input(f"Marks in {subject} (0-100): "))

        if not subject or subject in marks or not 0 <= score <= 100:
            print("Invalid subject or marks. Restart the program.")
            return

        marks[subject] = score

    result = run_pipeline(marks)

    print("\n--- STUDENT REPORT ---")
    print("Total:", result["analysis"]["total"])
    print("Average:", result["analysis"]["average"])
    print("Lowest subject:", result["analysis"]["lowest_subject"])
    print("Lowest marks:", result["analysis"]["lowest_marks"])

    print("\n--- RECOMMENDATIONS ---")
    for recommendation in result["recommendations"]:
        print("-", recommendation)


if __name__ == "__main__":
    main()
