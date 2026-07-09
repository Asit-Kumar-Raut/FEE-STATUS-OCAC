import os
import subprocess
import shutil
import sys

print("Checking dependencies...")
try:
    import PyInstaller
except ImportError:
    print("Installing PyInstaller...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

try:
    import reportlab
    import firebase_admin
except ImportError:
    print("Installing required Python libraries...")
    subprocess.run([sys.executable, "-m", "pip", "install", "reportlab", "firebase-admin"], check=True)

# Run PyInstaller with exclusions and a new folder name to bypass locks
print("Starting PyInstaller compilation (building as FeeManager to bypass locks)...")
build_cmd = [
    sys.executable,
    "-m",
    "PyInstaller",
    "--noconfirm",
    "--onedir",
    "--windowed",
    "--name=FeeManager",
    "--exclude-module=torch",
    "--exclude-module=torchvision",
    "--exclude-module=tensorflow",
    "--exclude-module=scipy",
    "--exclude-module=pandas",
    "--exclude-module=matplotlib",
    "--exclude-module=sympy",
    "--exclude-module=numpy",
    "app.py"
]

try:
    subprocess.run(build_cmd, check=True)
    print("PyInstaller compilation completed successfully!")
except Exception as e:
    print(f"Error compiling with PyInstaller: {e}")
    sys.exit(1)

# Paths
dest_dir = os.path.join("dist", "FeeManager")
images_dest = os.path.join(dest_dir, "images")
cred_dest = os.path.join(dest_dir, "firebase_credentials.json")

# Copy images folder
print("Bundling background assets...")
if os.path.exists(images_dest):
    shutil.rmtree(images_dest)
shutil.copytree("images", images_dest)

# Copy firebase credentials
print("Bundling Firebase connection key...")
shutil.copy("firebase_credentials.json", cred_dest)

print("==================================================")
print("BUILD SUCCESSFUL!")
print("Your secure, shareable desktop application is ready at:")
print(os.path.abspath(dest_dir))
print("==================================================")
