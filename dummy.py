print('Opening dummy.txt')
#open dummy.txt to read it as "in_stream" (in_stream is the variable)
with open('dummy.txt', 'r') as in_stream:
    print('Opening output.txt')
#open output.txt to write in it, call it "out_stream"
    with open('output.txt', 'w') as out_stream:
#for every line in the dummy.txt input file
#enumerate will keep it going line-by-line, but will return an index of the line called as well
        for line_index, line in enumerate(in_stream):
#call the strip method on each line. This will remove whitespace at the end of each line.
            line = line.strip()
#call the split method on each line. This splits the string into a list, where each word is one element in the list.
            word_list = line.split()
#call the sort method on the list from the previous line. 
            word_list.sort()
#for every element of the word list, write it out to out_stream
            for word in word_list:
                out_stream.write('{0}\t{1}\n'.format(line_index, word))
print("Done!")
print('dummy.txt is closed?', in_stream.closed)
print('output.txt is clsoed?', out_stream.closed)
