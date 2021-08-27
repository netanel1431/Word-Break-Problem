import os
import time

def Main_Create_Local_Dictionary():
    """
    By default read all the books under the folder Read_Texts_Files:
    1.Alice_in_wonderland.txt
    2.The_Game_of_thrones.txt
    2.Harrey_Poter_book_1.txt
    3.Harrey_Poter_book_4.txt
    4.Harrey_Poter_book_5.txt

    :return:
    dic that include all the words that appear in the attachments file + the longest word length in a dictionary
    """

    start_time = time.time()
    current_path = os.path.dirname(os.path.abspath(__file__)) #get my location path with os lib
    dic = {} # my local dic
    file_names=[] # all the file names from the folder Read_Books_For_Study
    #read all the text files (books) from in the folder Read_Texts_Files
    for filename in os.listdir((os.path.join(current_path, "Read_Books_For_Study"))):
        file_names.append(os.path.join((os.path.join(current_path, "Read_Books_For_Study")),filename))

    #for each text file/book we add his words to our dic
    for path in file_names:
        with open(path, "r", encoding="utf8") as file:
            data = (file.read().splitlines())
            count=0
            for sentence in data:
                if sentence=="" or sentence== " " or sentence=="\n":
                    continue
                # remove special chars
                sentence=(sentence.replace(".\n", '').replace(',', ' ').replace("’", "").replace("­"," ").replace("'","").replace("\\"," ").replace('\n', '').replace("*","").replace(")","").replace("(","").replace("-"," ").replace(":","").replace("—"," ").replace("…","").replace('!','').replace("‘", "").replace('?', '').replace(';', '').replace('-', ' ').replace("“", "").replace(".", "").replace("”", "")).split()
                for word  in sentence:
                    count=count+1 # count all the words
                    word=word.lower()
                    if word not in dic.keys(): # for each word from the text file push to my local dic , if the words is allready in the dic just increase his value by +1
                        dic[word] = 1
                    else:
                        dic[word] = dic.get(word) + 1

    #The only one-letter words in English are a and I -- Remove all one letter that can not be a word
    abc_letters=["B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for _char in abc_letters:
        if _char.lower() in dic:
            dic.pop(_char.lower())

    #Get the longest word length in a dictionary
    keysList = []
    for key in dic:
        keysList.append(key)
    max_word_len=len(max(keysList,key=len))

    print("--- %s seconds Time taken for reading the local dictionary ---Main_Read_Texts_Files---" % (time.time() - start_time))

    return dic,max_word_len


