# Word-Break-Problem
Solution to Word Break Problem<br/>
See also [Link to our youtube video](https://www.youtube.com/watch?v=_9LD5fKJ-90/)

***What we doing ?***<br/>
Our algorithm  try create a correct sentence from the input string without space

***Damerau_Levenshtein_distance_Algo.py***<br/>
An algorithm that calculates the percentage of a similarity between the original sentence and the new sentence we created.While get a grade on the actions of adding, removing and replacing characters that required to perform in order to convert the sentence we created to be 100% similar to the original sentence.

***Local_Dictionary.py***<br/>
By default read all the books under the folder Read_Texts_Files:<br/>
    1.Alice_in_wonderland.txt<br/>
    2.The_Game_of_thrones.txt<br/>
    2.Harrey_Poter_book_1.txt<br/>
    3.Harrey_Poter_book_4.txt<br/>
    4.Harrey_Poter_book_5.txt<br/>
<br/>Return: dic that include all the words that appear in the attachments file + the longest word length in a dictionary
we create a Counter array of all the words from that book to be our local dictionary

***WBP_Main.py***</br>
The main file in the project, gives a solution to the word break problem, any string of characters that is entered as input, it will try to decompose the string into a proper sentence in the English language.

Example of running the code:

**Source sentence:**
Then, just when things were looking very serious for Frank, the report on the Riddles’ bodies came back and changed everything. The police had never read an odder report. A team of doctors had examined the bodies and had concluded that none of the Rid­dles had been poisoned, stabbed, shot, strangled, suffocated, or (as far as they could tell) harmed at all. In fact (the report continued, in a tone of unmistakable bewilderment), the Riddles all appeared to be in perfect health — apart from the fact that they were all dead. The doctors did note

**input string without space:**
thenjustwhenthingswerelookingveryseriousforfrankthereportontheriddlesbodiescamebackandchangedeverythingthepolicehadneverreadanodderreportateamofdoctorshadexaminedthebodiesandhadconcludedthatnoneoftheriddleshadbeenpoisonedstabbedshotstrangledsuffocatedorasfarastheycouldtellharmedatallinfactthereportcontinuedinatoneofunmistakablebewildermenttheriddlesallappearedtobeinperfecthealthapartfromthefactthattheywerealldeadthedoctorsdidnote

**Our algorithm will produced the following sentence, which he thinks is most similar to the original sentence:**
then just when things were looking very serious for frank there port on the riddles bodies came back and changed everything the police had never read an odder report a team of do to shade a mined the bodies and had concluded that none of the riddles had been poisoned stabbed shots rang led suffocated or as far as they could tell harmed at all in fact there port continued in at one of unmistakable be wilder men the riddles all appeared to be in perfect he a hap a from the fact that they were all dead the do to did note


**We can also see the level of accuracy of our algorithm and statistics**
![image](https://user-images.githubusercontent.com/50228442/131125614-7af6e680-3c89-47da-ab70-e987dc6abbc0.png)


**Threshold_value_of_our algo the determine if the The string can not be divided to correct sentence or not**</br>
threshold level=0.066</br>
    if 0.066 >=percentage_Algo_1_missed_chars ---> missing percentage is smaller than the threshold level ---> Result:The string can be divided into a proper sentence
    </br>else: ---> missing percentage is bigger than the threshold level ---> Result:The string can not be divided</br>
    


***Project By Netanel and Dolev***

