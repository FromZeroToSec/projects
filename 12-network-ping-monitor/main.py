import subprocess

result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
print(result.stdout)
