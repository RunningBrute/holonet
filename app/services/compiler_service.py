import subprocess

class CompilerService:
    def compile(self, code: str):

        with open("main.cpp", "w") as file:
            file.write(code)

        result = subprocess.run(
            ["g++", "main.cpp", "-o", "main"],
            capture_output=True,
            text=True
        )

        print("returncode: ", result.returncode)
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)

        return result.stdout + result.stderr