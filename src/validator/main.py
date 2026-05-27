
from validator.crew import Validator


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'A Clothing Brand of Football Jerseys',
    }

    try:
        Validator().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")



