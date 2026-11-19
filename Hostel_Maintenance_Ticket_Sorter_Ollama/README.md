# Hostel Maintenance Ticket Sorter — Ollama / Qwen Offline Edition

## One-click Windows setup
1. Extract this ZIP into a writable folder such as Desktop.
2. Double-click `STARTUP.bat` (or run `setup.bat` first).
3. Setup creates a Python virtual environment, installs the Python packages,
   checks/installs Ollama, starts its local service, and downloads `qwen2.5:3b`.
4. After setup, `RUN.bat` runs the ticket sorter. You can use it again without
   downloading the model each time.

## Model and hardware
- Model: `qwen2.5:3b` through Ollama (about 1.9 GB download).
- Intended for CPU-capable Windows PCs; no dedicated GPU or paid API key required.
- The first setup needs internet. After the model is downloaded, inference is local.
- Ollama's local API is `http://127.0.0.1:11434`.
- Model memory use is additional to the download size; close heavy apps if RAM is tight.

## Project files
- `STARTUP.bat`: setup then run.
- `setup.bat`: install/check dependencies and download model.
- `RUN.bat`: run using the already-installed local model.
- `CHECK_OLLAMA.bat`: diagnose local Ollama and list downloaded models.
- `main.py`: classification, validation, routing, duplicate detection and reports.
- `complaints.csv`, `open_tickets.csv`: input examples.

## Reports
The program regenerates `work_orders.csv`, `results.csv`, `needs_info.csv`, and `summary.txt`.

## Important
The model proposes classifications only. Python validates fields and applies safety rules.
A warden must review urgent tickets and all work orders. The tool never closes a ticket.
Room numbers are accepted only when explicitly present in the complaint.

## Troubleshooting
- If `ollama` is not found, finish installing Ollama, reopen Command Prompt, and run `setup.bat`.
- If the API is unavailable, open the Ollama desktop app or run `CHECK_OLLAMA.bat`.
- If the model download is interrupted, run `setup.bat` again; Ollama can resume/cache layers.
- Keep the project folder and model files on a drive with enough free space.


## Browser dashboard
- Run `DASHBOARD.bat` after setup to open the local dashboard in your browser.
- Dashboard address: `http://127.0.0.1:8765`.
- It reads `work_orders.csv`, `results.csv`, and `needs_info.csv`; click Refresh data after running `RUN.bat`.
- It uses Python's standard library only; no additional package or paid API is required.
- Keep the dashboard command window open while viewing it. Press Ctrl+C in that window to stop it.
