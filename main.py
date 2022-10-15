def main():
	cmd = ' '
	while cmd != 'Q':
		#clear_screen()
		disp_main_screen()
		cmd = input()
		cmd = cmd.upper()
		if cmd == 'N':
			new_task()
		elif cmd == 'C':
			complete_task()
		elif cmd == '#':
			cancel_task()
		elif cmd == 'Q':
			print('Goodbye.')
		else:
			print('The command not available.')

def disp_main_screen():
	print('''
	================== Task Manager ==================
	''')
	list_tasks()
	list_commands()

def list_tasks():
	print('''
	1 - Laundary               3pm          Today
	2 - Car wash               1pm          Tomorrow''')

def list_commands():
	print('''
	(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit
	(S)how completed  (X)NeXt Page (P)revious Page''')
	print('>>>', end=' ')

def new_task():
	print('new task')
	
def	complete_task():
	print('complete task')

def cancel_task():
	print('cancel task')

def clear_screen():
	print('''  
	   ''' *30)
	

	

main()

