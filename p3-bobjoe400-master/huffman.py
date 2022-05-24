import os
from huffman_bit_writer import *
from huffman_bit_reader import *
from ordered_list import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return (self.char == other.char) and (self.freq == other.freq)
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    try:
        f = open(filename,'r')
    except:
        raise FileNotFoundError
    count = [0]*256
    str = f.read()
    f.close()
    for i in str:
        count[ord(i)] += 1
    return count

def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    freq_list = OrderedList()
    index = 0
    for freq in char_freq:
        if freq != 0:
            node = HuffmanNode(index,freq)
            freq_list.add(node)
        index +=1
    while freq_list.size() > 1:
        node1 = freq_list.pop(0)
        node2 = freq_list.pop(0)
        nfreq = node1.freq + node2.freq
        nchar = (node2.char,node1.char)[node1.char<node2.char]
        new = HuffmanNode(nchar,nfreq)
        new.left = node1
        new.right = node2
        freq_list.add(new)

    return freq_list.head.next.item

def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    codes = ['']*256
    def c_c_r(node, level):
        if node is None:
            return
        if node.left is None and node.right is None:
            codes[node.char] = level
        if node.left is not None:
            c_c_r(node.left, level+'0')
        if node.right is not None:
            c_c_r(node.right, level+'1')
    c_c_r(node,'')
    return codes

def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    rtn_str = ""
    index = 0
    for i in freqs:
        if i !=0:
            rtn_str += ("%d %d "% (index,i))
        index +=1
    return rtn_str[:-1]

def parse_header(header_string):
    freq = [0]*256
    index = 0
    #import pdb;pdb.set_trace()
    parse = header_string.split()
    while index < len(parse):
        freq[int(parse[index])] = int(parse[index+1])
        index+=2
    return freq

def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take note of special cases - empty file and file with only one unique character'''
    #import pdb; pdb.set_trace()
    freq = cnt_freq(in_file)
    huft = create_huff_tree(freq)
    hdr = create_header(freq)+'\n'
    codes = create_code(huft)

    f = open(out_file,'w')
    name, ext = os.path.splitext(out_file)
    huffbw = HuffmanBitWriter(name+'_compressed'+ext)
    if len(hdr.split(' ')) > 2:
        f.write(hdr)
        huffbw.write_str(hdr)
        i = open(in_file)
        for char in i.read():
            f.write(codes[ord(char)])
            huffbw.write_code(codes[ord(char)])
        i.close()
    elif len(hdr.split(' ')) == 2:
        f.write(hdr)
        huffbw.write_str(hdr)
    f.close()
    huffbw.close()

def huffman_decode(encode_file, decode_file):
    huffbr = HuffmanBitReader(encode_file)
    fout = open(decode_file,'w')
    hdr = huffbr.read_str()
    freq = parse_header(hdr)
    numchar = 0
    for i in freq:
        numchar += i
    huft = create_huff_tree(freq)
    index = 0
    curr = huft
    while index < numchar:
        if curr.left is None and curr.right is None:
            fout.write(chr(curr.char))
            curr = huft
            index+=1
            continue
        curr_bit = huffbr.read_bit()
        if not curr_bit:
            curr = curr.left
        else:
            curr = curr.right
    fout.close()
    huffbr.close()
