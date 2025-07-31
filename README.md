# FinancialReseacher Crew

A multi-agent AI system for financial research and analysis, powered by [crewAI](https://crewai.com). This project automates the process of researching and reporting on companies using specialized AI agents and web search tools.

<img width="1785" height="922" alt="image" src="https://github.com/user-attachments/assets/976ab531-26e2-4348-a8b6-685a8705a6bc" />


---

## Features
- **Two specialized agents:**
  - **Researcher:** Gathers and synthesizes up-to-date information about a target company using LLMs and web search (SerperDevTool).
  - **Analyst:** Analyzes the research and produces a comprehensive, professional report.
- **Configurable via YAML:** Easily customize agent roles, goals, and tasks in `config/agents.yaml` and `config/tasks.yaml`.
- **Web search integration:** Uses SerperDevTool for real-time web data.
- **Output:** Generates a detailed report in `output/report.md`.

---

## Installation

1. **Python version:** Requires Python >=3.10 <3.14
2. **Install [UV](https://docs.astral.sh/uv/):**
   ```bash
   pip install uv
   ```
3. **Install dependencies:**
   ```bash
   crewai install
   ```

---

## Configuration

1. **API Keys:**
   - Add your Serper (serpredev) API key to a `.env` file in the project root:
     ```
     SERPER_API_KEY=your_serperdev_api_key_here
     ```
   - If using other LLM providers (e.g., OpenAI), add their keys as needed.

2. **Agents:**
   - Edit `src/financial_reseacher/config/agents.yaml` to define agent roles, goals, and LLMs.

3. **Tasks:**
   - Edit `src/financial_reseacher/config/tasks.yaml` to define the research and analysis workflow.

4. **Custom Logic:**
   - Edit `src/financial_reseacher/crew.py` to add or modify agents, tasks, or tools.
   - The Researcher agent is configured to use SerperDevTool for web search.

---

## How It Works

- **Entry point:** `src/financial_reseacher/main.py`
- **Crew definition:** `src/financial_reseacher/crew.py`
- **Agents:**
  - **Researcher:**
    - Role: Expert Financial Researcher specializing in {company}
    - LLM: gemini/gemini-1.5-flash
    - Tools: SerperDevTool (web search)
  - **Analyst:**
    - Role: Strategic Market Analyst and Financial Report Writer for {company}
    - LLM: gemini/gemini-1.5-flash
- **Tasks:**
  - **research_task:** Conducts thorough research on the company, focusing on status, history, challenges, news, and outlook.
  - **analysis_task:** Analyzes research and produces a structured report (output: `output/report.md`).

---

## Running the Project

From the project root (`crew/financial_reseacher`):
```bash
crewai run
```

This will:
- Launch the crew
- Run the research and analysis tasks for the default company (Apple)
- Output a report to `output/report.md`

---

## Customization
- Change the target company in `main.py` by editing the `inputs` dictionary.
- Add or modify agents and tasks in the YAML config files.
- Integrate additional tools or LLMs as needed in `crew.py`.

---

## Troubleshooting
- **SerperDevTool Import Error:**
  - Make sure you have installed `crewai-tools`:
    ```bash
    pip install crewai-tools
    ```
  - Import with: `from crewai_tools import SerperDevTool`
- **API Quota/Rate Limit:**
  - If you see quota errors, check your API provider dashboard and consider upgrading your plan or reducing request frequency.
- **Internal Server Errors:**
  - These are usually temporary issues with the LLM provider. Retry after some time or check provider status.

---

## Support
- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

---

Let's create wonders together with the power and simplicity of crewAI.
