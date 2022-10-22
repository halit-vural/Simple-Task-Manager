import tasks

def disp_main(filter='all'):
    print('='*20, 'Task Manager', '='*20)
    tasks.list(filter)
    print()
    list_commands()

def list_commands():
    print('(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit')
    print('(S)how completed  (X)neXt page (P)revious page')
    print()

def clear():
	print('''  
	   ''' *30)