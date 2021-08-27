#-------------------------------------------------------------------Import-Lib---------------------------------------------------------------
import enchant.checker
from Local_Dictionary import Main_Create_Local_Dictionary
from Damerau_Levenshtein_distance_Algo import *
import os
from os.path import exists
import subprocess
#---------------------------------

#-------------------------------------------------------Functions------------------------------------------------------------------------
def Remove_Special_Chars(source_paragraph):
    paragraph_nasty=source_paragraph
    specialChars = "!#$%^&*()‘”_+-',.@#$%^&*()?”[]…\—`/;:'’{},."
    for specialChar in specialChars:
        paragraph_nasty = paragraph_nasty.replace(specialChar, "")
    paragraph_nasty = paragraph_nasty.replace("\\", " ")
    paragraph_nasty = paragraph_nasty.replace("\\", " ")
    return paragraph_nasty.lower()
def Remove_abc_letters(dic_enchant):
    # The only one-letter words in English are a and I -- Remove all one letter that can not be a word
    abc_letters = ["B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                   "W", "X", "Y", "Z"]
    for _char in abc_letters:
        dic_enchant.remove(_char)
        dic_enchant.remove(_char.lower())
def Get_Input_Paragraph_From_User():
    #get the local path
    my_path=os.getcwd()
    file=os.path.join(my_path,"word_break_file.txt")

    #check if the file:"word_break_file.txt" is exists if yes,delete and create a new one
    if exists(file):
        os.remove(file)
        f = open(file, "a")
        f.write("Please Enter on the next row String without space and we will break it to small words(save and close the file):")
        f.close()
    else:#if the file:"word_break_file".txt is not exists create a new one
        f = open(file, "a")
        f.write("Please Enter on the next row String without space and we will break it to small words(save and close the file):")
        f.close()

    #open the file to the display and wait until user save and close the file
    p=subprocess.Popen(["start", "/WAIT",file], shell=True)
    p.wait()


    #Read the txt file and create from him a big string, also delete the content:"Please Enter on the next row String without space and we will break it to small words(save and close the file):"
    # delete matching content
    content = "Please Enter on the next row String without space and we will break it to small words(save and close the file):"
    input_paragraph=""
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # readlines() includes a newline character
            if line.strip("\n") != content:
                input_paragraph=input_paragraph+line.strip("\n")
    return  input_paragraph
def Create_Summary_Report_File():
    ratio_algo1 = '{:.4f}'.format(ratio)
    Algo_1_missed_chars = len(missed_chars)
    timestr = time.strftime("%Y%m%d")
    my_path = os.getcwd()
    file=open(os.path.join(my_path,"Word_Break_Solution"+timestr+".txt"),'w')
    file.write("Paragraph_input_without_space is:\n")
    file.write(paragraph_nasty_without_space)
    file.write("\n")
    file.write("\nThe length of characters of the incoming string(Without spaces or special chars):")
    file.write(str(len(paragraph_nasty_without_space)))
    file.write("\n\n\n\n\n\n------------------------------word_break_with_local_dic_and_count_manipulate----------------------------\nOur algorithm generated the following statement from the given input:\n\n")
    file.write(new_paragraph)
    missed_chars_string=",".join(missed_chars)
    file.write("\n-----------------------------------------------------------\nMissing characters:\n"+missed_chars_string+"\nThe amount of missing characters:"+str(Algo_1_missed_chars))
    file.write("\n------------------------------------------------------------\nThe ration of compare 1=100% , 0=0% --> :"+str(ratio))
    file.write("\n------------------------------------------------------------\nThe minimal number of insertions, deletions, and symbol substitutions required to transform the two string use transpositions (swapping of adjacent symbols):"+str(swap_chars))


    percentage_Algo_1_missed_chars = float('{:.4f}'.format(float(Algo_1_missed_chars) / float(float_paragraph_nasty_without_space_len)))
    Threshold_value_of_missed_chars=float(0.066)
    file.write("\n\n\n\nOur algorithm has a threshold level of "+str('{:.4f}'.format(Threshold_value_of_missed_chars*100))+"% This is the maximum value of missing characters that our program can define that the input string can be divided correctly")
    file.write("\nWhile running and while trying to compose a proper sentence from the given input string, we reached a missing characters percentage of:" + str('{:.4f}'.format(percentage_Algo_1_missed_chars*100))+"%")
    if Threshold_value_of_missed_chars >=percentage_Algo_1_missed_chars:
        file.write("\n\nOur characters missing percentage is smaller than the threshold level ---> Result:The string can be divided into a proper sentence.")
    else:
        file.write("\n\nOur characters missing percentage is bigger than the threshold level ---> Result:The string can not be divided.")


    file.close()
    os.startfile(os.path.join(my_path, "Word_Break_Solution"+timestr+".txt"))
def WBP_With_Local_Dic_AND_Count_Manipulate(my_local_dic, str_line):
    # `n` stores length of the current substring
    n = len(str_line)
    # Start of the substring that keeps on being checked
    start = 0
    # Actual line that we got
    line = ""
    flag = 0
    # Runs until the end of the string
    while start < n:
        # 'temp' will store our results based on the longest word in the dictionary
        temp_words_candidate = []
        # This for is mad to check for every word that`s possible to get in the string from start to max word length
        for i in range(start + 1, start + max_word_length_for_local_dic if start + max_word_length_for_local_dic <= n else n +1):

            # consider all prefixes of the current string

            prefix = str_line[start:i]

            # if the prefix is found in the dictionary, then add it to the list
            if prefix in my_local_dic and dic_enchant.check(prefix):
                temp_words_candidate.append(prefix)
        # Check if
        #if (flag or len(temp) == 0) and start + max_word_length >= n:
        #    print("Missed some items, but found this string..\r\n\"" + line.strip() + "\"")
        #    return
        if len(temp_words_candidate) == 0:
            # Flag is there to know we missed some sub strings in the way
            missed_chars.append(str_line[start])
            missed_chars_index_location.append(start)
            # Continue the investigation
            start += 1
            continue
        # Here we will take the most count match from dictionary
        max_value_of_word_in_temp= my_local_dic.get(temp_words_candidate[-1]) * len(temp_words_candidate[-1]) * 30
        word_to_line=temp_words_candidate[-1]
        if len(temp_words_candidate)>1:
            for index in range (0, len(temp_words_candidate) - 1):
                if my_local_dic.get(temp_words_candidate[index])>max_value_of_word_in_temp:
                    word_to_line=temp_words_candidate[index]
                    max_value_of_word_in_temp=my_local_dic.get(temp_words_candidate[index])

        line += word_to_line + " "
        # Move to the next first letter that could start a word
        start += len(word_to_line)

    return line
#---------------------------------

if __name__ == '__main__':
    #-------------------------------------------Input source_paragraph , clean and Remove_Special_Chars and spcae-----------------------------
    source_paragraph=Get_Input_Paragraph_From_User()
    paragraph_without_special_chars=Remove_Special_Chars(source_paragraph)
    paragraph_nasty_without_space=paragraph_without_special_chars.replace(" ","")
    #---------------------------------

    #------------------------------------------init the online dic to english lang------------------------------------------------------------
    dic_enchant = enchant.Dict("en_US")
    Remove_abc_letters(dic_enchant)
    max_word_length_for_online_dic=45
    #----------------------------------

    #--------------------------------------init the local dic to english lang----------------------------------------------------------------
    my_own_dic,max_word_length_for_local_dic=Main_Create_Local_Dictionary() #get my local dic
    #----------------------------------


    float_paragraph_nasty_without_space_len=len(paragraph_nasty_without_space)
    missed_chars=[]
    missed_chars_index_location=[]

    #call to our function to run your algorithm and try create a correct sentence from the input string
    new_paragraph=WBP_With_Local_Dic_AND_Count_Manipulate(my_own_dic, paragraph_nasty_without_space)

    #An algorithm that calculates the percentage of a match between the original sentence and the new sentence we created and in addition some actions of adding, removing and replacing characters are required to perform in order for the sentence we created to be 100 percent similar to the original sentence.
    #Note: This can only be done if we know the original sentence
    swap_chars,ratio=damerau_levenshtein_distance(new_paragraph,paragraph_without_special_chars)

    #Calculate data on the incoming string, calculate data on the sentence we created and say whether the string can be divided into a correct sentence or not
    Create_Summary_Report_File()
