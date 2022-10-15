import tasks
import screen

def main():
	cmd = ' '
	while cmd != 'Q':
		screen.clear()
		screen.disp_main()
		cmd = input()
		cmd = cmd.upper()
		if cmd == 'N':
			tasks.new()
		elif cmd == 'C':
			tasks.complete()
		elif cmd == '#':
			tasks.cancel()
		elif cmd == 'Q':
			print('Goodbye.')
		else:
			print('The command not available.')

main()

