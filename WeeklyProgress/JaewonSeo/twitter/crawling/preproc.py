import re

class preproc():
    def __init__(self):
        self.erase()

    def erase(self):
        txt1 = open("talk.txt","r",encoding = 'utf-8')
        lines = txt1.readlines()
        txt2 = open("clean_talk.txt", "w",encoding = 'utf-8')
        word = ""
        for line in lines:
            cleaned_text = re.sub('[a-zA-z]','',line)
            output_string = re.sub(r'[^\w\s]', '', cleaned_text)
            word += output_string+"\n"
        txt2.write(word)
        
        openFile = open("clean_talk.txt", "r",encoding = 'utf-8')
        writeFile = open("updatedFile.txt", "w",encoding = 'utf-8')
        tmp = set()
        for txtLine in openFile:
            writeFile.write(txtLine)
            tmp.add(txtLine)
        openFile.close()
        writeFile.close()
        

        


if __name__=="__main__":
    preproc()