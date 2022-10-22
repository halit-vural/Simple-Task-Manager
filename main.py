import tasks
import screen

def main():
    cmd = ' '
    while cmd != 'Q':
        screen.clear()
        screen.disp_main()
        cmd = get_command('>> ')
        execute_command(cmd)

def get_command(msg):
    cmd = input(msg)
    return cmd.upper()

def execute_command(command):
    if command == 'N':   
        tasks.new()
    elif command == 'C':       
        tasks.complete()
    elif command == '#':
        tasks.cancel()
    elif command == 'Q':
        print('Goodbye.')
    else:
        print('The command not available.')

main()

