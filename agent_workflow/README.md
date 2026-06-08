Writer-Reviewer Multi-Agent Workflow
==================================

This small app demonstrates a multi-agent workflow (Writer + Reviewer).

Run:

```bash
python agent_workflow/main.py "Write a short article about sustainable gardening"
```

Output: plain text containing the refined content after collaboration.

Files:
- agent_workflow/agents/writer.py - Writer agent implementation
- agent_workflow/agents/reviewer.py - Reviewer agent implementation
- agent_workflow/workflow.py - Orchestrator that runs the agents
- agent_workflow/main.py - Simple CLI runner
