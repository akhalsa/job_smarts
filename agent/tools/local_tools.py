# agent/tools.py
import subprocess
import sys
from langchain_core.tools import tool  # or from langchain.tools import tool
from datetime import date
import json
import os
import re
from datetime import datetime
from pathlib import Path

@tool
def run_python_script(script_file_name: str) -> str:
    """Run a Python file with the current interpreter.
    
    Execution logs are saved to: agent/workspace/logs/{script_name}_{timestamp}.log
    
    Input:
        script_file_name: name of a script in the workspace folder. i.e. retrieve_jobs.py
    Output:
        Captured stdout/stderr and the return code.
    """
    # Build paths
    # NOTE: project_root must be repo root so `python -m agent.workspace.xxx` works.
    # __file__ is agent/tools/local_tools.py, so we need to go up 2 levels to repo root.
    project_root = Path(__file__).resolve().parents[2]
    log_dir = project_root / "agent"/ "workspace" / "logs"
    log_dir.mkdir(exist_ok=True)
    script_name = re.sub(r"\.py$", "", script_file_name)
    script_path = project_root / "agent"/ "workspace" / script_file_name

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{script_name}_{timestamp}.log"
    
    env = os.environ.copy()
    env['PYTHONPATH'] = str(project_root)
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(project_root),
            env=env
        )
        
        # Format output
        log_content = [
            f"=" * 60,
            f"Script: {script_file_name}",
            f"Script Executed With: python {script_path}",
            f"Executed: {datetime.now().isoformat()}",
            f"Return Code: {result.returncode}",
            f"=" * 60,
        ]
        
        if result.stdout:
            log_content.append("\n--- STDOUT ---")
            log_content.append(result.stdout)
        
        if result.stderr:
            log_content.append("\n--- STDERR ---")
            log_content.append(result.stderr)
        
        # Write to log file
        with open(log_file, 'w') as f:
            f.write('\n'.join(log_content))
        
        # Return to agent
        out = [f"returncode={result.returncode}"]
        if result.stdout:
            out.append("STDOUT:\n" + result.stdout)
        if result.stderr:
            out.append("STDERR:\n" + result.stderr)
        out.append(f"\n📝 Full log saved to: {log_file}")
        
        return "\n".join(out)
        
    except Exception as e:
        error_msg = f"Error running {script_file_name}: {e!r}"
        # Still try to log the error
        with open(log_file, 'w') as f:
            f.write(f"EXECUTION ERROR\n{error_msg}\n")
        return error_msg + f"\n📝 Error logged to: {log_file}"
