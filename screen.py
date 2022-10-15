def disp_main():
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
	
def clear():
	print('''  
	   ''' *30)