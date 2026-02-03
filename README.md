# Field RF / Telecom Maintenance Simulator (Python)

A Python-based command-line simulator that models real-world telecom and RF field maintenance workflows.  
The tool simulates alarm triage, technician dispatch, escalation handling, and structured shift logging—similar to processes used by NOCs and Field RF Technicians responding to live network events.

---

## Key Capabilities

- Alarm monitoring and prioritization by severity (CRITICAL, MAJOR, MINOR)
- Structured alarm data handling (site, equipment, description)
- Interactive CLI for alarm selection and response
- Technician dispatch with ETA and work notes
- Escalation and acknowledgment workflows
- Automatic shift logging in JSONL and CSV formats

---

## Real-World Relevance

This project mirrors common responsibilities in telecom field operations, including:

- Responding to system alarms within defined SLAs
- Diagnosing RF and network equipment issues
- Dispatching field technicians with ETAs
- Logging corrective maintenance actions
- Maintaining accurate operational records for reporting and audits

The simulator is designed to reflect how Field RF Technicians and NOC staff interact with alarms, tickets, and maintenance documentation in production environments.

---

## Technology Stack

- Python 3
- JSON / JSONL
- CSV reporting
- pathlib (cross-platform file handling)
- Command-line interface (CLI)

---

## 🎥 Interactive CLI Demo (Dispatch Workflow)

Recorded screen capture demonstrating:

- Alarm selection
- Technician dispatch
- ETA entry
- Dispatch notes
- Automatic shift log creation

▶️ **Watch the demo video:**  
[Field RF Alarm Dispatch Demo](2026-02-02%2023-10-33.mp4)

---

## Sample Console Output

