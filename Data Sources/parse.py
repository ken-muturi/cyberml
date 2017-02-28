input_file_name = ''
output_file_name = ''

file = open(data_file_name,'r')
output = open(output_file_name,'w')

for line in file:
    if line not in ('<1>\n','<2>\n','<3>\n','**EOF**\n', '**SOF**\n'):
        print(line, end='')

# Problem, any command using -args is on a new line...
