"""
PyDeloy - Python to EXE Converter
User Guide
"""

APP_NAME = "PyDeloy"

def get_guide_text():
    """Trả về hướng dẫn sử dụng"""
    
    text = """
1. Browse or drag & drop your .py file
2. Check "Single file output" for one .exe (optional)
3. Check "No console window" for GUI apps (optional)
4. Select GUI Framework if your app uses one
5. Enter output name for your .exe file
6. Add icon file if needed (optional)
7. Add hidden imports if PyInstaller misses modules
8. Use "Auto detect" to exclude unused modules
9. Click "Convert to EXE" and wait
10. Click "Open Folder" to view your .exe
11. Test your .exe on a system without Python
"""
    return text.strip()