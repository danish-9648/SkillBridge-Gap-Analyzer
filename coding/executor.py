# SkillBridge Coding Assessment Engine
# Candidate code executor


SAFE_BUILTINS = {
    "sum": sum,
    "len": len,
    "min": min,
    "max": max,
    "abs": abs,
    "sorted": sorted,
    "range": range,
    "enumerate": enumerate,
}


def execute_solution(code):
    """
    Execute candidate Python code and return the solution function.

    The candidate code must define:

        def solution(numbers):
            ...
    """

    namespace = {}

    try:
        exec(
            code,
            {
                "__builtins__": SAFE_BUILTINS
            },
            namespace
        )

        solution_function = namespace.get("solution")

        if solution_function is None:
            return {
                "success": False,
                "error": "Your code must contain a function named 'solution'."
            }

        if not callable(solution_function):
            return {
                "success": False,
                "error": "'solution' must be a function."
            }

        return {
            "success": True,
            "solution": solution_function
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }