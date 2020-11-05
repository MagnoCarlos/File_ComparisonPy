import docx
import os

# This program will compare and find if two strings are equal

def CompareParagraphs(paragraph1,  paragraph2):  # compare two paragraphs each paragraph
    print(paragraph1)
    print(paragraph2)
    print(" ")
    if paragraph1 == paragraph2:
        print("The paragraphs are equal")
    else:
        print("The paragraphs are not equal")


########################################################################################################################
########################################################################################################################
########################################################################################################################

line1 = "1 Passionate Master of Engineering in Electronic Communications seeking a graduate/junior position within the" \
        " fields of electronics, telecommunications, signal processing, control engineering, embedded systems and " \
        "software engineering with aim to become a chartered engineer. Natural leader with innovative and critical " \
        "skills who enjoys pursuing and solving new challenges and has excellent logical and analytical reasoning."

line2 = "1 Passionate Master of Engineering in Electronic Communications seeking a graduate/junior position within the" \
        " fields of electronics, telecommunications, signal processing, control engineering, embedded systems and " \
        "software engineering with aim to become a chartered engineer. Natural leader with innovative and critical " \
        "skills who enjoys pursuing and solving new challenges and has excellent logical and analytical reasoning."

########################################################################################################################
########################################################################################################################
########################################################################################################################

CompareParagraphs(line1, line2)
