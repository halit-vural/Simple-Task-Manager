import tasks
import screen

data = []
filter = 'all'

def main():
    global data
    global filter
    cmd = ''
    
    data = tasks.get_list(filter)
    
    while cmd != 'Q':
        screen.clear()
        tasks_to_list = screen.disp_main(data, filter)
        # print('length:', len(tasks_to_list))
        cmd = get_command('>> ')
        execute(cmd, tasks_to_list)

def get_command(msg):
    cmd = ''
    while cmd == '':
        cmd = input(msg)
    return cmd.upper()

def execute(command, on_tasks):
    global data
    global filter
    
    if command == 'N':  
        if len(data):            # if has any records
            new_index = int(data[-1][0]) + 1        # last item's index + 1
        else:
            new_index = 1        # no records
            
        new_task = tasks.new(new_index)
        # print('new:',new_task)
        if new_task:
            data += [new_task]
            # print(data)
            
    elif command == 'C':               # complete/uncomplete
        # print(data)
        idx = input("Select task:")
        if idx != '':
            idx = int(idx)
            # print('selected task:', on_tasks[idx-1][0])
            selected_task = on_tasks[idx-1][0]
            task_id = selected_task[0]
            # print('task id: ', task_id)
            data = tasks.complete(data, task_id)
            
    elif command == 'S':            # show/clear completed
        if filter == 'all':
            filter = 'hide'             # disp_main has a filter
        else:
            filter = 'all'            # display all items

    # elif command == 'F':            # focus today's tasks
    #     focus = True
        
    elif command == '#':
        tasks.cancel()
    elif command == 'Q':
        print('Goodbye.')
    else:
        print('The command not available.')






main()

