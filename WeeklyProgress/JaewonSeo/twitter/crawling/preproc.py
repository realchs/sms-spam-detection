import re

class preproc():
    def __init__(self):
        # self.erase()
        self.addition()

    def erase(self):
        txt1 = open("talk.txt","r",encoding = 'utf-8')
        lines = txt1.readlines()
        txt2 = open("clean_talk.txt", "w",encoding = 'utf-8')
        word = ""
        for line in lines:
            cleaned_text = re.sub('[@]+[0-9a-zA-Z_]+', '',line) # tag erase
            cleaned_text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", '',cleaned_text)
            output_string = re.sub(r'[^\w\s]', '', cleaned_text) # 특수문자 erase
            word += output_string+"\n"
        txt2.write(word)
        
        no_dup_lines = set() # set is O(1), better then list O(n)
        with open("clean_talk.txt", 'r+',encoding = 'utf-8') as fp:
            file_lines = fp.readlines()
            fp.seek(0)
            for line in file_lines:
                if line not in no_dup_lines:
                    fp.write(line)
                    no_dup_lines.add(line)
            fp.truncate()

    def addition(self):
        re_modif = open("clean_talk.txt", "r",encoding = 'utf-8')
        lines = re_modif.readlines()
        word = ""
        for line in lines:
            line = re.sub('RT', '',line)
            line = re.sub('  ', '',line )
            if line != "\n":
                word += line
        re_modif.close()
        txt_re = open("clean_talk.txt", "w",encoding = 'utf-8')
        txt_re.write(word)
        txt_re.close()
        

        


if __name__=="__main__":
    preproc()