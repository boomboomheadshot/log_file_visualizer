import cx_Freeze
import sys
import matplotlib
import sys
import os 


os.environ["TCL_LIBRARY"] = "C:\\python\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\python\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("log_file_visualizer.py", base=base, icon='ideaforge.ico')]

cx_Freeze.setup(
	name = "Log_File_Analyzer",
	options = {"build_exe":{"packages":["tkinter","matplotlib"],"include_files":["ideaforge.ico","C:\\python\\DLLs\\tcl86t.dll", "C:\\python\\DLLs\\tk86t.dll" ]}},
	version = "0.01",
	description = "Log_File_Visualizer_App",
	executables = executables
	)