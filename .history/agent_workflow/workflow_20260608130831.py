from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent


def run_workflow(prompt: str) -> str:
    """Run the Writer -> Reviewer -> Writer revision workflow and
    return the final refined content as plain text.
    """
    writer = WriterAgent()
    reviewer = ReviewerAgent()

    initial = writer.generate(prompt)
    review = reviewer.review(initial)
    final = writer.revise(initial, review)

    return final
