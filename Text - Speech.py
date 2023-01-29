# Python Program to Convert Text File to Speech File.
# We use a module called gTTs.
from gtts import gTTS  # Google text - Speech
text = 'Hello Savarapu Deepak,How are You and welcome to our company as a Python Developer.'
language = 'en'
obj = gTTS(text=text, lang=language, slow=False)
obj.save('gTTs.mp3')