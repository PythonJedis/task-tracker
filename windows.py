from win32ui import GetForegroundWindow
from win32process import GetCurrentProcess
import wmi
import ctypes, subprocess
from ctypes import byref, c_int
import time

GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId

c = wmi.WMI()

def test(wait):
	# We wait 3 seconds so you have time to switch to a different GetWindowText
	time.sleep(wait)
	window = GetForegroundWindow()
	hwnd = window.GetSafeHwnd()
	
	length = GetWindowTextLength(hwnd)
	buff = ctypes.create_unicode_buffer(length + 1)
	processID = c_int()
	threadID = GetWindowThreadProcessId(hwnd,byref(processID))

	print(threadID)
	for i in c.Win32_Process(ProcessID = threadID):
		print(i.ProcessID)

	#window.SetWindowText("Testing")
	title = window.GetWindowText()
	return title

title = test(3)
print(title)