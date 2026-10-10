
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

web_search_tool = DuckDuckGoSearchRun()


@tool
def search_internships(
    role: str,
    location: str = "India",
    work_mode: str = "Any",
    student_year: str = "Any",
    course: str = "Any"
) -> str:
    """
    Search the web for internship listings for college students.

    Args:
        role: Internship role or keywords, such as Python, AI/ML,
              web development, cybersecurity, or data analyst.
        location: Preferred city or region, or India.
        work_mode: Remote, Hybrid, On-site, or Any.
        student_year: Student's current year, or Any.
        course: Degree or department, or Any.

    Returns:
        Web search results containing potential internship listings.
    """
    query = (
        f"college student {role} internship "
        f"{location} {work_mode} "
        f"{student_year} {course} "
        "stipend eligibility duration apply official company 2026"
    )

    try:
        results = web_search_tool.invoke(query)
        return str(results) if results else "No internship results found."
    except Exception as exc:
        return f"Internship search failed: {type(exc).__name__}: {exc}"


if __name__ == "__main__":
    print(
        search_internships.invoke({
            "role": "Python",
            "location": "Chennai",
            "work_mode": "Any",
            "student_year": "3rd year",
            "course": "CSE"
        })
    )
