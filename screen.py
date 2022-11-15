import tasks as t

def disp_main(items, filter='all'):
    print('='*22, 'Task Manager', '='*22)
    items = disp_list(items, filter)
    print()
    list_commands()
    return items

def list_commands():
    print('(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit')
    print('(S)how completed  (X)neXt page (P)revious page')
    print()

def disp_list(items, filter='all', max=5):
    items_on_screen = []
    if len(items):
        i = 1
        for item in items:            
            if filter == 'hide' and t.is_completed(item):
                # print(item, ' is not added.')
                continue        # finish this cycle and read next item
            # if focus and !items.is_today(item):
            #     continue      # finish this cyctle and do not print if the item is not for today
            
            print_task(i, item)
            items_on_screen += [[item]]        # keep order of the items on screen
            i += 1
            # if i > max:
            #     print('. . .')
            #     break
        for _ in range(i, 20):
            print()            #fill the space with blank lines
    else:
        print()
        print('No items available...')
        print()

    return items_on_screen
    
def print_task(idx, task):
    # print('task:',task)
    _, title, date, time, status = task

    if status == 'completed':
        title = '-'*3 + (title) + '-'*3
        
    print(f'{idx:<2} - {title:<30} {date:<15} {time:<10}')   # tabular format with character counts 

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def clear():
	print('''  
	   ''' *30)