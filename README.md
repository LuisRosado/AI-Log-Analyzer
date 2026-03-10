# AI Log Analyzer

AI Log Analyzer is a lightweight observability tool that analyzes
application logs using AI.

It parses logs, detects patterns, calculates error statistics, and uses
a local LLM to generate root cause analysis and recommendations.

The project runs locally using **Flask + Ollama + Phi-3 Mini**.

------------------------------------------------------------------------

![Image](https://github.com/user-attachments/assets/65e0124c-ae7f-4ffc-8f7f-ad2f1d99c490)

## Features

-   Log parsing and pattern detection
-   Error rate and timeout analysis
-   AI-generated root cause analysis
-   Severity classification
-   Debugging recommendations
-   File upload support for log files
-   Local AI processing (no external APIs required)

------------------------------------------------------------------------

## Architecture

Frontend\
↓\
Flask API\
↓\
Log parser\
↓\
Pattern detection\
↓\
Statistics engine\
↓\
AI reasoning (Ollama + Phi-3)

------------------------------------------------------------------------

## Tech Stack

**Backend** - Python - Flask - Flask-CORS

**AI** - Ollama - Phi-3 Mini

**Frontend** - HTML - CSS - Vanilla JavaScript

------------------------------------------------------------------------

## Installation

Clone the repository:

``` bash
git clone https://github.com/YOUR_USERNAME/AI-Log-Analyzer.git
cd AI-Log-Analyzer
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Install Ollama

Install Ollama from:

https://ollama.com

Then download the model:

``` bash
ollama pull phi3:mini
```

------------------------------------------------------------------------

## Running the Application

You need **two terminals**.

### Terminal 1 -- Start Ollama

``` bash
ollama serve
```

This starts the local AI model server.

### Terminal 2 -- Start the backend

``` bash
python backend/app.py
```

Flask will start on:

    http://localhost:5000

------------------------------------------------------------------------

## Open the Application

If running locally:

    http://localhost:5000

If running in Codespaces, open the forwarded port **5000**.

------------------------------------------------------------------------

## Example Log Input

    ERROR database timeout
    ERROR database timeout
    ERROR database timeout
    WARNING retrying connection

------------------------------------------------------------------------

## Example Output

**Summary**\
The service experienced repeated database timeouts.

**Root Cause**\
Database performance or network latency issues.

**Severity**\
HIGH

**Recommendations** - Investigate database performance - Optimize
queries - Review database configuration - Check network connectivity

------------------------------------------------------------------------

## Project Structure

    AI-Log-Analyzer
    │
    ├── backend
    │   ├── app.py
    │   ├── analyzer.py
    │   ├── ai_analysis.py
    │   ├── log_parser.py
    │   └── pattern_detector.py
    │
    ├── frontend
    │   └── index.html
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Future Improvements

-   Log anomaly detection
-   Error spike detection
-   Interactive charts dashboard
-   Drag-and-drop log upload
-   Multi-language log support

------------------------------------------------------------------------

## License

MIT License
