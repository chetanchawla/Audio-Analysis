
# coding: utf-8

# In[2]:


#Importing the Libraries
import os
import subprocess


# In[41]:


Basepath='C:/Users/asd/Desktop/videoAds/' #Basepath is the folder path that contain the txt files
List = open(Basepath+"titless.txt", encoding='utf-8').readlines() #titless.txt is a txt file which stores the names of al the videos in utf8 encoding and is read into List.
#alternatively, you can use the os.listdir() command to list all the videos' name in the directory
List2=[] 
#List2 saves the names in form of a list
for i in range(len(List)):
    List2.append(List[i].split("\n")[0])
# print(Basepath+"Extracted Videos/"+list2[2]+".mp4")
print(Basepath+"Extracted Videos/"+List2[2]+".mp4")


# In[146]:


#List3 is the list of video names with all utf8 encoding removed. Note that this was not being followed directly by the Utf8 to Ascii conversion
#Hence a separate loop is created here which takes in account only the ascii characters. 
List3=[]
for i in range(1000):
    List3.append(''.join([x for x in List2[i] if (ord(x) < 128 and not(ord(x)==58) and not(ord(x)==46) and not(ord(x)==35) and not(ord(x)==34) and not(ord(x)==124) and not(ord(x)==39) and not(ord(x)==59) and not(ord(x)==47) and not(ord(x)==42)and not(ord(x)==37) and not(ord(x)==36) and not(ord(x)==44))]))
#To find out the utf characters' , the following 2 blocks of code were used


# List3 is the list of video names with all utf8 encoding removed. Note that this was not being followed directly by the Utf8 to Ascii conversion.
# 
# Hence a separate loop is created here which takes in account only the ascii characters.
# 
# To find out the utf characters' , the following 2 blocks of code were used

# In[149]:


#This block of code is used to check all the alphabets present in our titles and print them
inp = set()
for j in range(1000):
    for x in List3[j]:
        if x not in inp:
            inp.add(x)
inp2=sorted(list(inp))
print(inp2)
print(len(inp2))


# In[128]:


#This block of code is used to check where the outlying character lies.
# for j in range(1000):
#     for x in List3[j]:
#         if x=='+':
#             print(j)
# print(List3[395])


# In[160]:


#This block of code is used to rename the code in a minimal fashion
#Each video is replaced by a number corresponding its position in the folder
#This is done because the subprocess command does not allow utf-8 characters as well as spaces in the naming
for i in range(1,1000):
    try:
        os.rename(List3[i]+".mp4", str(i)+'.mp4')
    except:
        continue


# In[163]:


#this is the for loop for extracting the audio files from the videos. Specify the number of videos.
number=1000
for i in range(number):
    command = "ffmpeg -i "+str(i)+".mp4"+" -ab 160k -ac 2 -ar 44100 -vn "+str(i)+".wav"
    subprocess.call(command, shell=True)

