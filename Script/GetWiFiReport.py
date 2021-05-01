
def run():
	import win32com.shell.shell as shell

	commands = 'netsh wlan show wlanreport'
	shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

	commands = 'C:\ProgramData\Microsoft\Windows\WlanReport\wlan-report-latest.html'
	shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

#run()