"""Workshop challenge: find two courses within a budget."""

from config import COURSE_FEES
from tools import calculator


def find_courses_within_budget(budget):
    courses = list(COURSE_FEES.items())

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            code1, fee1 = courses[i]
            code2, fee2 = courses[j]

            total = float(calculator(f"{fee1} + {fee2}"))

            if total <= budget:
                print(f"{code1} + {code2} = Rs. {total:,.0f}")


if __name__ == "__main__":
    print("\n=== CHALLENGE ===\n")

    budget = 30000

    print(f"Budget: Rs. {budget:,}")
    print("Course combinations within budget:")

    find_courses_within_budget(budget)
