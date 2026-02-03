## Example Output

This simulator demonstrates alarm triage, technician dispatch, escalation handling,
and structured shift logging similar to real NOC and field maintenance workflows.

### Interactive CLI Demo (Dispatch Workflow)

📹 **Recorded demo** showing alarm selection, dispatch, ETA entry, and logging:  
`field-rf-alarm-dispatch-demo.mp4`

### Sample Console Output

Loaded alarms:
- [CRITICAL] Tower A12 | RRU | RRU not responding
- [MAJOR] Hub 7 | Microwave Link | High BER detected

Action selected: DISPATCH  
Dispatch to: Field Tech  
ETA: 2 hours  
Ticket created: TKT-87CFB3

### Shift Log Artifacts

Each action (acknowledge, dispatch, escalate) is logged in structured formats:

- **JSONL (append-only):** `shift_log.jsonl`  
- **CSV (exported for reporting):** `shift_log.csv`

These logs mirror real-world field maintenance and NOC documentation practices,
including timestamps, severity, equipment, dispatch targets, ETAs, notes, and ticket IDs.


