"""
PyDeloy - Python to EXE Converter
User Guide
"""

APP_NAME = "PyDeloy"
APP_VERSION = "1.0.0"

def get_info_text():
    """Trả về hướng dẫn sử dụng"""
    
    text = """
HOW TO USE PYDELOY

1. SELECT PYTHON FILE
   • Click "Browse..." button or drag & drop .py file into the drop zone
   • File path will be displayed

2. CONFIGURE BASIC OPTIONS
   • Single file output: Create one .exe file (recommended)
   • No console window: Hide console for GUI apps
   • Clean build: Remove old build files before building
   • GUI Framework: Select if your app uses a GUI framework
   • Output name: Name for your .exe file
   • Icon file: Optional .ico icon for your executable

3. ADVANCED OPTIONS (Optional)
   • Hidden imports: Add modules that PyInstaller might miss
   • Exclude modules: Remove unused modules to reduce size
   • Auto detect: Automatically select safe modules to exclude

4. BUILD YOUR EXECUTABLE
   • Click "Convert to EXE" button
   • Monitor progress in the Log tab
   • Wait for completion message

5. GET YOUR EXECUTABLE
   • Click "Open Folder" to view the dist folder
   • Your .exe file is ready to use!

TIPS
• Use --onefile for single portable executable
• Use --noconsole for GUI apps without terminal
• Exclude unused modules to reduce file size
• Test your .exe on a clean system without Python installed

COMMON ISSUES
• Missing modules: Add them in "Hidden imports"
• Large file size: Exclude unused modules in Advanced tab
• Import errors: Make sure all dependencies are installed
"""
    return text.strip()