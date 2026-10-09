
def suggest_improvements(marks):
    recommendations = []

    for subject, score in marks.items():
        if score < 60:
            message = (
                f"{subject}: You scored {score}. "
                "Revise weak concepts and practise questions daily."
            )
        else:
            message = (
                f"{subject}: Good marks! "
                "Keep improving and maintain your performance."
            )

        recommendations.append(message)

    return recommendations
