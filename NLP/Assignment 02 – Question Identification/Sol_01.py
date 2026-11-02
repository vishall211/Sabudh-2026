"""Solution entry point for Question Identification Assignment.

Delegates execution to Question_Identification.py.
"""
import runpy
from pathlib import Path

if __name__ == "__main__":
    script_path = Path(__file__).resolve().parent / "Question_Identification.py"
    runpy.run_path(str(script_path), run_name="__main__")
