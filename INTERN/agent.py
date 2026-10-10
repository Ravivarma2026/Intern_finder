
import gradio as gr
from dotenv import load_dotenv
from langchain.agents import create_agent

from llm import create_llm
from shared_tools import search_internships, web_search_tool
from system_prompts import SYSTEM_PROMPT_LOCAL_TOOLS

load_dotenv()

llm = create_llm()

tools = [
    search_internships,
    web_search_tool
]

internship_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT_LOCAL_TOOLS
)


def run_agent(role, location, work_mode, student_year, course):
    if not role or not role.strip():
        return "Please enter an internship role or keyword."

    user_prompt = f"""
    Find internship opportunities for a college student.

    Internship role or keywords: {role}
    Preferred location: {location}
    Preferred work mode: {work_mode}
    Current year of study: {student_year}
    Course or department: {course}

    Search for relevant internship listings and provide company names,
    locations, stipends, durations, eligibility, deadlines, application
    links, and potential future career opportunities where available.

    Do not require a resume. Do not invent missing information.
    """

    try:
        response = internship_agent.invoke({
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        })

        for message in reversed(response["messages"]):
            if getattr(message, "type", "") == "ai" and message.content:
                if isinstance(message.content, str):
                    return message.content

                return str(message.content)

        return "The agent did not return a final answer."

    except Exception as exc:
        return (
            f"An error occurred: {type(exc).__name__}: {exc}\n\n"
            "Check that Ollama is running, the model is installed, "
            "and the search dependencies are available."
        )


def deploy_agent():
    with gr.Blocks(title="Internship Finder Agent") as app:
        gr.Markdown("# Internship Finder Agent")
        gr.Markdown(
            "Discover internship opportunities for college students. "
            "No resume required."
        )

        with gr.Row():
            role = gr.Textbox(
                label="Internship Role / Keywords",
                placeholder="Python, AI/ML, Web Development"
            )
            location = gr.Textbox(
                label="Preferred Location",
                value="India",
                placeholder="Chennai, Bengaluru, Remote"
            )

        with gr.Row():
            work_mode = gr.Dropdown(
                label="Work Mode",
                choices=["Any", "Remote", "Hybrid", "On-site"],
                value="Any"
            )
            student_year = gr.Dropdown(
                label="Year of Study",
                choices=[
                    "Any",
                    "1st year",
                    "2nd year",
                    "3rd year",
                    "Final year"
                ],
                value="3rd year"
            )

        course = gr.Textbox(
            label="Course / Department",
            value="CSE",
            placeholder="B.E. CSE, B.Tech IT, ECE"
        )

        find_button = gr.Button(
            "Find Internships",
            variant="primary"
        )

        output = gr.Markdown()

        find_button.click(
            fn=run_agent,
            inputs=[
                role,
                location,
                work_mode,
                student_year,
                course
            ],
            outputs=output
        )

    app.launch()


if __name__ == "__main__":
    deploy_agent()
