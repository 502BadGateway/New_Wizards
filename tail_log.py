def log_print(string):
    tail_file.write(string)
    print string
    return

def init(fileName):
    print = log_print 
    tail_file = open(fileName, 'w')
    return True

