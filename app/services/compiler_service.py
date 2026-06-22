import subprocess
from pathlib import Path

from app.services.session_manager import Session

class CompilerService:
    def compile(self, session: Session):

        session_dir = Path("tmp") / session.id
        session_dir.mkdir(parents=True, exist_ok=True)
        source_file = session_dir / "main.cpp"
        binary_file = session_dir / "app"

        with open(source_file, "w") as file:
            file.write(session.code)

        result = subprocess.run(
            ["g++", source_file, "-o", binary_file],
            capture_output=True,
            text=True
        )

        print("returncode: ", result.returncode)
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)

        return result.stdout + result.stderr