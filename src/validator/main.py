from validator.crew import Validator


def run():
    """
    Run the crew.
    """

    inputs = {
        "topic": "A Clothing Brand of Football Jerseys",
    }

    try:
        result = Validator().crew().kickoff(inputs=inputs)

        tasks_output = result.tasks_output

        ceo_output = tasks_output[0].raw
        marketer_output = tasks_output[1].raw
        developer_output = tasks_output[2].raw
        # marketer_critique_output = tasks_output[3].raw
        # developer_critique_output = tasks_output[4].raw
        # ceo_defense_output = tasks_output[5].raw
        vc_output = tasks_output[3].raw

        final_report = f"""
            # Startup Validation Report

            {ceo_output}

            ---

            {marketer_output}

            ---

            {developer_output}

            ---

            {vc_output}
"""

        with open("final_report.md", "w", encoding="utf-8") as f:
            f.write(final_report)

        print("Final report generated: final_report.md")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")