# SkillBridge Coding Assessment Engine
# Test case evaluator


def evaluate_solution(solution_function, test_cases):
    """
    Evaluate a candidate solution against multiple test cases.

    Returns:
        {
            "total_tests": int,
            "passed_tests": int,
            "failed_tests": int,
            "score": int,
            "results": list
        }
    """

    results = []
    passed = 0

    for index, test_case in enumerate(test_cases, start=1):

        test_input = test_case["input"]
        expected = test_case["expected"]

        try:
            actual = solution_function(test_input)

            success = actual == expected

            if success:
                passed += 1

            results.append({
                "test_case": index,
                "input": test_input,
                "expected": expected,
                "actual": actual,
                "passed": success
            })

        except Exception as error:

            results.append({
                "test_case": index,
                "input": test_input,
                "expected": expected,
                "actual": None,
                "passed": False,
                "error": str(error)
            })

    total_tests = len(test_cases)

    score = round((passed / total_tests) * 100) if total_tests else 0

    return {
        "total_tests": total_tests,
        "passed_tests": passed,
        "failed_tests": total_tests - passed,
        "score": score,
        "results": results
    }