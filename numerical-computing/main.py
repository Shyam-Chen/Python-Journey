"""Export marimo notebooks to scripts in parallel."""

import subprocess
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


scripts_dir = Path("scripts")

if scripts_dir.exists():
    shutil.rmtree(scripts_dir)

scripts_dir.mkdir(exist_ok=True)


notebooks = [str(f) for f in Path(".").glob("*.py") if f.name != "main.py"]


def export_notebook(notebook: str) -> tuple[str, bool, str]:
    output_path = f"./scripts/{notebook}"
    cmd = ["uv", "run", "marimo", "export", "script", notebook, "-o", output_path]

    result = subprocess.run(cmd, capture_output=True, text=True)
    success = result.returncode == 0
    message = result.stderr if not success else ""

    return notebook, success, message


print(f"🚀 Exporting {len(notebooks)} notebooks...")

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(export_notebook, nb): nb for nb in notebooks}

    for future in as_completed(futures):
        notebook, success, error_msg = future.result()

        if success:
            print(f"✅ {notebook} -> ./scripts/{notebook}")
        else:
            print(f"❌ Failed to export {notebook}")

            if error_msg:
                print(f"   {error_msg}")

print("✨ Done!")
