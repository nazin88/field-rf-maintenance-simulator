# Field RF / Telecom Maintenance Simulator

This project simulates real-world workflows used by Field RF and telecommunications technicians to respond to alarms, diagnose issues, perform corrective maintenance, and restore equipment to operational status.

The focus is on **field operations**, not theoretical RF modeling.

---

## What This Project Demonstrates

- Alarm-driven maintenance workflows
- Field troubleshooting and fault isolation
- Corrective vs preventive maintenance logic
- Restoration of service with verification steps
- Accurate documentation and service logging
- Independent field decision-making under time pressure

---

## Simulated Environment

The simulator represents multiple field sites such as:
- Central hubs
- Tower sites (including lighting systems)
- Roadside or cabinet-based communications equipment

Each site generates alarms with:
- Severity levels
- Symptoms
- Probable causes
- Service status tracking

---

## How It Works

1. Alarms are loaded from a structured dataset
2. The technician can:
   - Acknowledge alarms
   - Review symptoms and probable causes
   - Record root cause and corrective action
   - Verify restoration and close tickets
3. All actions are logged for traceability and documentation

---

## Why This Is Relevant

Field RF and telecom roles require fast response, structured troubleshooting, and clear documentation.  
This simulator mirrors how real maintenance tickets are handled in live environments, including time-sensitive outages and restoration to service.

---

## Run Locally

**Requirements**
- Python 3.10+

**Install dependencies**
```bash
pip install -r requirements.txt

