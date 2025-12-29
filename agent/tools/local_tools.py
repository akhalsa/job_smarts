# agent/tools.py
import subprocess
import sys
from langchain_core.tools import tool  # or from langchain.tools import tool
from datetime import date
import json
import os
from datetime import datetime
from pathlib import Path

@tool
def run_python_script(path: str) -> str:
    """Run a Python file with the current interpreter.
    
    Execution logs are saved to: agent/logs/{script_name}_{timestamp}.log
    
    Input:
        path: Absolute or agent-relative path to a .py file.
    Output:
        Captured stdout/stderr and the return code.
    """
    from datetime import datetime
    import os
    
    # Create logs directory
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Generate log filename
    script_name = Path(path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{script_name}_{timestamp}.log"
    
    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True,
            timeout=120,
        )
        
        # Format output
        log_content = [
            f"=" * 60,
            f"Script: {path}",
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
        error_msg = f"Error running {path}: {e!r}"
        # Still try to log the error
        with open(log_file, 'w') as f:
            f.write(f"EXECUTION ERROR\n{error_msg}\n")
        return error_msg + f"\n📝 Error logged to: {log_file}"
