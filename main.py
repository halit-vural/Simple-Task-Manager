import tasks
import screen

data = []

def main():
    global data
    cmd = ''
    data = tasks.get_list('all')
    
    while cmd != 'Q':
        screen.clear()
        screen.disp_main(data)
        cmd = get_command('>> ')
        execute_command(cmd)

def get_command(msg):
    cmd = ''
    while cmd == '':
        cmd = input(msg)
    return cmd.upper()

def execute_command(command):
    global data
    if command == 'N':  
        if len(data):
            new_index = int(data[-1][0]) + 1        # last item's index + 1
        else:
            new_index = 1
            
        new_task = tasks.new(new_index)
        # print('new:',new_task)
        if new_task:
            data += [new_task]
            # print(data)
            
    elif command == 'C':   
        idx = input("Select task:")
        if idx != '':
            idx = int(idx)
            data[idx-1] = tasks.complete(data, idx-1)
    elif command == '#':
        tasks.cancel()
    elif command == 'Q':
        print('Goodbye.')
    else:
        print('The command not available.')






main()

