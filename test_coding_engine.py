from coding.executor import execute_solution
from coding.evaluator import evaluate_solution
from coding.test_cases import DEFAULT_TEST_CASES


candidate_code = """
def solution(numbers):
    return sum(numbers)
"""


execution = execute_solution(candidate_code)

if not execution["success"]:
    print("❌ Code execution failed:")
    print(execution["error"])

else:
    solution = execution["solution"]

    result = evaluate_solution(
        solution,
        DEFAULT_TEST_CASES
    )

    print("\n================================")
    print("SKILLBRIDGE CODING ENGINE")
    print("================================")

    print(f"Total Tests : {result['total_tests']}")
    print(f"Passed      : {result['passed_tests']}")
    print(f"Failed      : {result['failed_tests']}")
    print(f"Score       : {result['score']}%")

    print("\nTest Results:")

    for test in result["results"]:
        status = "✅ PASS" if test["passed"] else "❌ FAIL"

        print(
            f"{status} | "
            f"Input: {test['input']} | "
            f"Expected: {test['expected']} | "
            f"Actual: {test['actual']}"
        )