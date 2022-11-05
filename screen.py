import tasks

def disp_main(tasks, filter='all'):
    print('='*21, 'Task Manager', '='*21)
    disp_list(tasks, filter)
    print()
    list_commands()

def list_commands():
    print('(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit')
    print('(S)how completed  (X)neXt page (P)revious page')
    print()

def disp_list(tasks, filter='all', max=5):
    if len(tasks):
        i = 1
        for task in tasks:
            print_task(i, task)
            i += 1
            # if i > max:
            #     print('. . .')
            #     break
    else:
        print()
        print('No tasks available...')
        print()
    
def print_task(idx, task):
    # print('task:',task)
    _, title, date, time, status = task

    if status == 'completed':
        title = '-'*3 + title + '-'*3
        
    print(f'{idx:<2} - {title:<30} {date:<15} {time:<10}')    

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
    
def clear():
	print('''  
	   ''' *30)