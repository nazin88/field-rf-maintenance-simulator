import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sample_alarms.json"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

console = Console()

def load_alarms():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def log_action(entry):
    log_file = LOG_DIR / "service_log.jsonl"
    with log_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def display_alarms(alarms):
    table = Table(title="Field RF / Telecom Alarm Queue")
    table.add_column("Ticket", style="bold")
    table.add_column("Site")
    table.add_column("Equipment")
    table.add_column("Alarm")
    table.add_column("Severity")
    table.add_column("Status")

    for alarm in alarms:
        table.add_row(
            alarm["ticket_id"],
            alarm["site"],
            alarm["equipment"],
            alarm["alarm"],
            alarm["severity"],
            alarm["status"]
        )

    console.print(table)

def main():
    console.print("\n[bold]Field RF / Telecom Maintenance Simulator[/bold]\n")
    alarms = load_alarms()

    while True:
        display_alarms(alarms)

        action = Prompt.ask(
            "Select action",
            choices=["ack", "diagnose", "close", "exit"],
            default="diagnose"
        )

        if action == "exit":
            console.print("Exiting simulator.")
            break

        ticket_id = Prompt.ask("Enter ticket ID").strip().upper()
        alarm = next((a for a in alarms if a["ticket_id"] == ticket_id), None)

        if not alarm:
            console.print("[red]Ticket not found.[/red]\n")
            continue

        timestamp = datetime.now().isoformat(timespec="seconds")

        if action == "ack":
            alarm["status"] = "Acknowledged"
            log_action({
                "timestamp": timestamp,
                "ticket_id": ticket_id,
                "action": "Acknowledged alarm",
                "notes": "Alarm acknowledged; investigation started."
            })
            console.print("[green]Alarm acknowledged.[/green]\n")

        elif action == "diagnose":
            console.print("\n[bold]Symptoms:[/bold]")
            for s in alarm.get("symptoms", []):
                console.print(f" - {s}")

            console.print("\n[bold]Probable causes:[/bold]")
            for c in alarm.get("probable_causes", []):
                console.print(f" - {c}")

            root_cause = Prompt.ask("Enter suspected root cause")
            corrective_action = Prompt.ask("Enter corrective action taken")

            alarm["status"] = "In Progress"

            log_action({
                "timestamp": timestamp,
                "ticket_id": ticket_id,
                "action": "Diagnosis / corrective maintenance",
                "root_cause": root_cause,
                "corrective_action": corrective_action,
                "status": alarm["status"]
            })
            console.print("[green]Diagnosis recorded.[/green]\n")

        elif action == "close":
            verification = Prompt.ask(
                "Enter verification steps (e.g., alarm cleared, signal restored)"
            )

            alarm["status"] = "Restored / Closed"

            log_action({
                "timestamp": timestamp,
                "ticket_id": ticket_id,
                "action": "Service restored and ticket closed",
                "verification": verification,
                "status": alarm["status"]
            })
            console.print("[green]Ticket closed. System restored.[/green]\n")

if __name__ == "__main__":
    main()
