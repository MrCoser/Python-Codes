from zlib import decompress
import heapq
import os

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None


    def __lt__(self,other):
        return self.freq < other.freq


    def __equal__(self,other):
        return self.freq == other.freq

    

class HuffmannCoding:

    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}

    def __make_frequency_dict(self,text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1


        return freq_dict 

    def __buildHeap(self,freq_dict):

        for key in freq_dict:
            frequency = freq_dict[key]
            bntreenode = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap,bntreenode)


    def __buildTree(self):
        while (len(self.__heap) > 1):
            btn1 = heapq.heappop(self.__heap)
            btn2 = heapq.heappop(self.__heap)
            freq_sum = btn1.freq + btn2.freq
            newNode = BinaryTreeNode(None, freq_sum)
            newNode.left = btn1
            newNode.right = btn2
            heapq.heappush(self.__heap, newNode)
        
        return

    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return

        if root.value is not None:
            self.__codes[root.value] = curr_bits
            self.__reverseCodes[curr_bits] = root.value
            return

        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"1")


    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")        


    def __get_EncodedText(self,text):
        newText = ""
        for char in text:
            newText += self.__codes[char]
        return newText


    def __get_PaddedEncodedText(self,newText):
        padded_amount = 8 - (len(newText) % 8)
        
        for i in range(padded_amount):
            newText += '0'

        padded_info = "{0:08b}".format(padded_amount)
        padded_encoded_text = padded_info + newText
        return padded_encoded_text


    def __getBytesArray(self,paddedText):
        array = []

        for i in range(0,len(paddedText),8):
            byte = paddedText[i:i+8]
            array.append(int(byte,2))


        return array


    def compress(self):
        # Steps to be performed :
        # 1) get file from path
        # 2) read text from file
        # 3) make frequency dictionary using the text
        # 4) construct a heap using frequency_dict
        # 5) construct a binary tree using heap
        # 6) construct the codes from binary tree
        # 7) construct the encoded text using the codes
        # 8) put this encoded text into a binary file
        # 9) return this binary file as output

        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"


        with open(self.path,'r+') as file, open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()
            freq_dict = self.__make_frequency_dict(text)
            self.__buildHeap(freq_dict)
            self.__buildTree()
            self.__buildCodes()

            newText = self.__get_EncodedText(text)
            paddedText = self.__get_PaddedEncodedText(newText)

            newbytes = self.__getBytesArray(paddedText)
            finalbytes = bytes(newbytes)
            output.write(finalbytes)

        print('Compressed')
        return output_path

    
    def __removePadding(self,str):
        padded_info = str[:8]
        extra = int(padded_info, 2)

        text = str[8:]
        text_after_padding_removed = str[:-1*extra]
        return text_after_padding_removed


    def __decodeText(self,actual_text):

        decoded_text = ""
        currBits = ""

        for bit in actual_text:
            currBits += bit
            if currBits in self.__reverseCodes:
                char = self.__reverseCodes[currBits]
                decoded_text += char
                currBits = ""

        return decoded_text 


    def decompress(self, input_path):
        filename, file_ext = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path,'rb') as file, open(output_path,'w') as output:
            bit_string = ""
            byte = file.read(1)

            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            

            actual_text = self.__removePadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)

        return 

# Main function
path = 'C:\\Users\\Prithvijit\\OneDrive\\Documents\\sample.txt'
h = HuffmannCoding(path)
output_path = h.compress()
h.decompress(output_path)  