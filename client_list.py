def main():
    infile = open('clients.txt', 'r')

    seq = 1

    for client in infile:
        client = client.rstrip('\n')
        print(str(seq) + '. ' + client)
        seq += 1

    infile.close()

main()
