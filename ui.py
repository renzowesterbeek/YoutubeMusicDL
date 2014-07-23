import pafy
from Tkinter import *

# input.get()
# output.set()

def getDownloadList(musicfile):
	# Gets all the urls from musicfile
	musicFile = open(musicfile, "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def downloadAudio(files):
	for url in files:
		audio = pafy.new(url)

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def downloadVideo(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

def switchType():
	type = typeSelect.get()
	return type

urlList = []
def addURL():
	url = urlInput.get()
	urlList.append(url)
	outputName = "output" + url
	outputName = StringVar()
	outputName.set(url)
	outputNameLabel = Label(app, textvariable=outputName)
	outputNameLabel.pack()
	urlInput.delete(0, END)

def download():
	if switchType() == "Video":
		downloadVideo(urlList)
	else:
		downloadAudio(urlList)
	status.set("Done")

# Basic window configuration #
app = Tk()
app.geometry("400x400")
app.title("Python Youtube Downloader")

# Instructions text #
welcomeText = IntVar()
welcomeText.set("Input YouTube url(s) 1 by 1")
welcome = Label(app, textvariable=welcomeText)
welcome.pack()

# Radiobutton #
typeSelect = StringVar()
R1 = Radiobutton(app, text="Video", variable=typeSelect, value="Video", command=switchType)
R1.pack(anchor=CENTER)
R1.deselect()
R2 = Radiobutton(app, text="Audio", variable=typeSelect, value="Audio", command=switchType)
R2.pack(anchor=CENTER)
R2.select()

# User input #
urlInput = Entry(app)
urlInput.pack()

# Button #
addButton = Button(app, text="Add", command=addURL)
addButton.pack()

# Output Labels #
output = StringVar()
output.set("")
outputLabel = Label(app, textvariable=output)
outputLabel.pack()

# Button #
downloadButton = Button(app, text="Download", command=download)
downloadButton.pack()

# Status Labels #
status = StringVar()
status.set("")
statusLabel = Label(app, textvariable=status)
statusLabel.pack()

app.mainloop()