# task-tracker


Modules list:

- Qt
- Matplolib
- PyWin32


Installing PyWin32 with Python 3.4:

PyWin32 doesn't have a proper 3.4 Installer, so you have to change a few things to get it to work.

- Download PyWin32 Here: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py3.4.exe/download?use_mirror=hivelocity
- Then you have to copy the contents of C:\Python34\Lib\site-packages\pywin32_system32 (should be 2 DLLs) into the directory C:\Python34\Lib\site-packages\win32
- Hopefully this will be fixed in the future :)


Requirements:

 - track tasks/process's
 - graph/visualize them
 - group and rank/level them


Initial Issues:

- Title Windows of Browsers and Windows Explorer change based on what website and directory (respectively) are open

-- Need to compile a common program list so we can parse the title strings to see what program is actually being used, in addition to what site is open. (Probably only need to do this for browsers. I am testing more programs.)