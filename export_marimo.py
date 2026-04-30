"""Export marimo notebooks to scripts in parallel."""

import subprocess
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


def export_notebooks(project_dir: Path):
    """Export all marimo notebooks in the given project directory."""
    scripts_dir = project_dir / "scripts"

    if scripts_dir.exists():
        shutil.rmtree(scripts_dir)

    scripts_dir.mkdir(exist_ok=True)

    # Find notebooks in the project directory
    notebooks = [
        f.name
        for f in project_dir.glob("*.py")
        if f.name not in ["main.py", "export_marimo.py"]
    ]

    if not notebooks:
        print(f"⚠️  No notebooks found in {project_dir}")
        return

    def export_notebook(notebook: str) -> tuple[str, bool, str]:
        # 使用相對於專案目錄的路徑
        output_path = f"./scripts/{notebook}"
        cmd = ["uv", "run", "marimo", "export", "script", notebook, "-o", output_path]

        # 關鍵：在專案目錄中執行，使用該專案的 uv 環境
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=project_dir,  # ⭐ 指定工作目錄
        )

        success = result.returncode == 0
        message = result.stderr if not success else ""

        return notebook, success, message

    print(f"🚀 Exporting {len(notebooks)} notebooks from {project_dir.name}...")

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(export_notebook, nb): nb for nb in notebooks}

        for future in as_completed(futures):
            notebook, success, error_msg = future.result()

            if success:
                print(f"✅ {notebook} -> {project_dir.name}/scripts/{notebook}")
            else:
                print(f"❌ Failed to export {notebook}")
                if error_msg:
                    print(f"   {error_msg}")

    print(f"✨ Done with {project_dir.name}!\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 指定專案目錄
        for project in sys.argv[1:]:
            project_path = Path(project)
            if project_path.exists():
                export_notebooks(project_path)
            else:
                print(f"❌ Project not found: {project}")
    else:
        # 當前目錄
        export_notebooks(Path("."))
