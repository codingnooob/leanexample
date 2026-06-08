class WriterAgent:
    """Simple Writer agent that creates an initial draft and can revise it."""

    def generate(self, prompt: str) -> str:
        title = prompt.strip().capitalize()
        body = (
            f"{title}\n\n"
            "Initial draft outlining key ideas. It is concise and focused but"
            " can be tightened further.\n\n"
            "Overview:\n"
            "Introduce the topic and why it matters.\n\n"
            "Details:\n"
            "Explain main points and provide actionable steps or examples.\n"
        )
        return body

    def revise(self, original: str, review: dict) -> str:
        """Revise the original draft using reviewer feedback.

        If the reviewer provides a `refined` version, adopt it; otherwise
        perform a light cleanup.
        """
        refined = review.get("refined")
        if refined:
            return refined
        return " ".join(original.split())
