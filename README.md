# Word-Break-Problem
Solution to Word Break Problem<br/>
See also [Link to our youtube video](https://www.youtube.com/watch?v=_9LD5fKJ-90/)

***What we doing ?***<br/>
Our algorithm  try create a correct sentence from the input string without space

***Damerau_Levenshtein_distance_Algo.py***<br/>
An algorithm that calculates the percentage of a similarity between the original sentence and the new sentence we created.While get a grade on the actions of adding, removing and replacing characters that required to perform in order to convert the sentence we created to be 100% similar to the original sentence.

***Local_Dictionary.py***<br/>
By default read all the books under the folder Read_Texts_Files:
    1.Alice_in_wonderland.txt
    2.The_Game_of_thrones.txt
    2.Harrey_Poter_book_1.txt
    3.Harrey_Poter_book_4.txt
    4.Harrey_Poter_book_5.txt
return: dic that include all the words that appear in the attachments file + the longest word length in a dictionary
we create a Counter array of all the words from that book to be our local dictionary


