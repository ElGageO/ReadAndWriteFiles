def main():
    outfile = open('philosophers.txt', 'w')

    name1 = 'John Locke'
    name2 = 'David Hume'
    name3 = 'Edmund Burke'

    outfile.write(name1 + '\n')
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')
    
    outfile.close()

def add_my_name():
    outfile = open('philosophers.txt', 'a')

    my_name = 'Gage Reynolds'
    outfile.write(my_name + '\n')

    outfile.close()

main()
add_my_name()
