class ReviewerAgent:
    """Simple Reviewer agent that provides concise, actionable feedback
    and a cleaned/refined version of the content.
    """

    def review(self, content: str) -> dict:
        suggestions = []
        if "can be tightened" in content or "can be tightened further" in content:
            suggestions.append("Tighten phrasing and remove hedging words.")
        if "Introduce the topic" in content:
            suggestions.append("Turn guidance into a short paragraph rather than section labels.")

        # Produce a simple refined version by applying basic substitutions
        refined = content.replace("Initial draft outlining key ideas. It is concise and focused but can be tightened further.",
                                  "Initial draft outlining key ideas. It is focused and actionable.")
        refined = refined.replace("Overview:\nIntroduce the topic and why it matters.",
                                  "Overview: A brief introduction explaining why this topic matters.")
        refined = refined.replace("Details:\nExplain main points and provide actionable steps or examples.",
                                  "Details: Concrete points with actionable steps and examples.")

        # Compact whitespace
        refined = "\n\n".join(p.strip() for p in refined.split("\n\n"))

        feedback = "\n".join(f"- {s}" for s in suggestions) if suggestions else "- Minor wording and structure improvements suggested."
        return {"feedback": feedback, "refined": refined}
