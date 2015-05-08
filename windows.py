from win32ui import GetForegroundWindow
import time

def test(wait):
	# We wait 3 seconds so you have time to switch to a different GetWindowText
	time.sleep(wait)
	window = GetForegroundWindow()
	title = window.GetWindowText()
	return title

title = test(3)
print(title)