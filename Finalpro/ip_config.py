import sys
if(len(sys.argv)>=3):
	arguments = sys.argv[2]
	arg=arguments.split(':')
	local_ip=arg[0]
	port=arg[1]
else:
	local_ip='127.0.0.1'
	port='8000'
